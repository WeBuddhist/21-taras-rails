#!/usr/bin/env bash
# Mongolian draft 2 — Gemini run primed with the locked Mongolian word list (keyword-standardize).
# Run on your Mac, in Terminal:   bash 3-TRANSFORMATIONS/Translations/Gemini/mn-general/run-mn-general.sh
# The key is never written to disk: it is read from $GEMINI_API_KEY, or asked for (hidden input).
set -euo pipefail
cd "$(dirname "$0")/../../../.."                       # vault root
GM="../Webuddhist-Skills/rails/machine-translate/scripts/gm_translate.py"
SRC="1-SOURCES/Text/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།.md"
OUT="3-TRANSFORMATIONS/Translations/Gemini/mn-general"
[ -f "$GM" ] || { echo "cannot find $GM (Webuddhist-Skills must sit next to the vault)"; exit 1; }
# macOS python.org Python ships without trusted certificates ("CERTIFICATE_VERIFY_FAILED").
# If Python cannot verify HTTPS, give it a certificate bundle: certifi if installed, else one
# built from the Mac's own keychains (this also covers any company certificate installed there).
pyssl_ok() { python3 -c 'import ssl,urllib.request,urllib.error
try: urllib.request.urlopen("https://generativelanguage.googleapis.com/", timeout=15)
except urllib.error.HTTPError: pass
except Exception as e:
    import sys; sys.exit(1 if "CERTIFICATE_VERIFY_FAILED" in str(e) else 0)' ; }
if ! pyssl_ok; then
  CA=$(python3 -c 'import certifi; print(certifi.where())' 2>/dev/null || true)
  if [ -z "$CA" ] && command -v security >/dev/null; then
    CA="${TMPDIR:-/tmp}/gemini-ca-bundle.pem"
    security find-certificate -a -p /System/Library/Keychains/SystemRootCertificates.keychain > "$CA"
    security find-certificate -a -p /Library/Keychains/System.keychain >> "$CA" 2>/dev/null || true
  fi
  export SSL_CERT_FILE="$CA"
  pyssl_ok || { echo "Python still cannot verify HTTPS. Run: open \"/Applications/Python 3.*/Install Certificates.command\" and re-run."; exit 1; }
  echo "certificates: using $SSL_CERT_FILE"
fi

if [ -z "${GEMINI_API_KEY:-}" ]; then read -r -s -p "Gemini API key (hidden): " GEMINI_API_KEY; echo; fi
export GEMINI_API_KEY

# Pick the strongest Gemini Pro model this key can use (override with MODEL=... bash run-mn-general.sh).
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

python3 "$GM" --source "$SRC" --lang mongolian --lang-tag mn --out "$OUT" --model "$MODEL" --thinking high
python3 "$GM" --source "$SRC" --lang mongolian --lang-tag mn --out "$OUT" --model "$MODEL" --thinking high --headings
echo
echo "Done. Output: $OUT/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-mn.md — tell Claude it has finished."
