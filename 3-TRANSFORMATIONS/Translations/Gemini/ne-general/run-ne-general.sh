#!/usr/bin/env bash
# Nepali draft 2 — Gemini run primed with the locked Nepali word list (keyword-standardize).
# Run on your Mac, in Terminal:   bash 3-TRANSFORMATIONS/Translations/Gemini/ne-general/run-ne-general.sh
# The key is never written to disk: it is read from $GEMINI_API_KEY, or asked for (hidden input).
set -euo pipefail
cd "$(dirname "$0")/../../../.."                       # vault root
GM="../Webuddhist-Skills/rails/machine-translate/scripts/gm_translate.py"
SRC="1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md"
OUT="3-TRANSFORMATIONS/Translations/Gemini/ne-general"
[ -f "$GM" ] || { echo "cannot find $GM (Webuddhist-Skills must sit next to the vault)"; exit 1; }
if [ -z "${GEMINI_API_KEY:-}" ]; then read -r -s -p "Gemini API key (hidden): " GEMINI_API_KEY; echo; fi
export GEMINI_API_KEY

# Pick the strongest Gemini Pro model this key can use (override with MODEL=... bash run-ne-general.sh).
if [ -z "${MODEL:-}" ]; then
  MODEL=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "https://generativelanguage.googleapis.com/v1beta/models?pageSize=500" | python3 -c '
import json, re, sys
d = json.load(sys.stdin); best = None
for m in d.get("models", []):
    n = m["name"].split("/")[-1]
    if "generateContent" not in m.get("supportedGenerationMethods", []): continue
    r = re.fullmatch(r"gemini-(\d+(?:\.\d+)?)-pro(-preview)?(?:-[0-9-]+)?", n)
    if not r: continue
    key = (float(r.group(1)), r.group(2) is None, n)   # newest version first, then stable over preview
    best = max(best, key) if best else key
print(best[2] if best else "gemini-3.1-pro-preview")')
fi
echo "model: $MODEL"

python3 "$GM" --source "$SRC" --lang nepali --lang-tag ne --out "$OUT" --model "$MODEL" --thinking high
python3 "$GM" --source "$SRC" --lang nepali --lang-tag ne --out "$OUT" --model "$MODEL" --thinking high --headings
echo
echo "Done. Output: $OUT/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-ne.md — tell Claude it has finished."
