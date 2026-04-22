#!/usr/bin/env bash
# _ecom/lib/compliance-filter.sh
# 违禁词扫描 — 被所有内容生成类 skill 调用

DATA_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../data" && pwd)"

# scan_forbidden <text>  → prints JSON {risk_score, action, matches}
scan_forbidden() {
  local text="$1"
  local words_file="$DATA_DIR/forbidden-words.json"
  [ -f "$words_file" ] || { echo '{"error":"no word library"}'; return 1; }
  python3 <<PY
import json, re, sys
with open("$words_file") as f:
    lib = json.load(f)
text = """$text"""
matches = []
for cat, words in lib.items():
    for w in words:
        # exact + phonetic-variant match (simplified)
        if re.search(rf"(?<!\w){re.escape(w)}(?!\w)", text):
            severity = "critical" if cat in ("medical_efficacy", "exaggerated_claims") else "high"
            matches.append({"word": w, "category": cat, "severity": severity})

critical = sum(1 for m in matches if m["severity"] == "critical")
high = sum(1 for m in matches if m["severity"] == "high")
risk_score = min(100, critical * 30 + high * 10)
action = "block" if critical > 0 or risk_score >= 50 else ("warn" if risk_score >= 20 else "pass")
print(json.dumps({"risk_score": risk_score, "action": action, "matches": matches}, ensure_ascii=False))
PY
}

# validate_27_function <claim> <blue_cap_number>
validate_27_function() {
  local claim="$1"
  local cap="$2"
  local funcs_file="$DATA_DIR/27-functions.json"
  local registry="$DATA_DIR/blue-cap-registry.json"
  [ -f "$funcs_file" ] || { echo '{"error":"no 27-function lib"}'; return 1; }
  python3 <<PY
import json
with open("$funcs_file") as f:
    funcs = json.load(f)
try:
    with open("$registry") as f:
        reg = json.load(f)
    registered = reg.get("$cap", {}).get("functions", [])
except Exception:
    registered = []
claim = """$claim"""
result = {"claim": claim, "registered": registered, "matched": [], "verdict": "unknown"}
for f in funcs:
    if f in claim:
        result["matched"].append(f)
        if f in registered:
            result["verdict"] = "exact"
        else:
            result["verdict"] = "broader_or_unrelated"
            break
if not result["matched"]:
    result["verdict"] = "no_27_function_claim"
print(json.dumps(result, ensure_ascii=False))
PY
}
