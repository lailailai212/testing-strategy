#!/usr/bin/env bash
# Generate a self-signed Root CA certificate (PEM) for PKI "Import Root Cert" testing.
#
# Usage:
#   bash scripts/pki/generate_test_root_ca.sh
#   CN="My Root CA" OUT_DIR=/tmp bash scripts/pki/generate_test_root_ca.sh
#
# Output (default):
#   scripts/pki/fixtures/test-root-ca.pem   ← upload to OBIS PKI
#   scripts/pki/fixtures/test-root-ca.key   ← keep local, do NOT upload

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT_DIR="${OUT_DIR:-${SCRIPT_DIR}/fixtures}"
KEY_BITS="${KEY_BITS:-2048}"
DAYS="${DAYS:-3650}"
CN="${CN:-Test Root CA}"
O="${O:-QA Test}"
C="${C:-CN}"
KEY_FILE="${KEY_FILE:-${OUT_DIR}/test-root-ca.key}"
PEM_FILE="${PEM_FILE:-${OUT_DIR}/test-root-ca.pem}"

if ! command -v openssl >/dev/null 2>&1; then
  echo "error: openssl not found in PATH" >&2
  exit 1
fi

# Git Bash on Windows converts "/CN=..." to "C:/Program Files/Git/CN=...".
# Disable MSYS path conversion for this invocation only.
if [[ "${MSYSTEM:-}" == MINGW* ]] || [[ "${OSTYPE:-}" == msys* ]]; then
  export MSYS2_ARG_CONV_EXCL="*"
fi

mkdir -p "${OUT_DIR}"

echo "Generating Root CA key (${KEY_BITS} bits)..."
openssl genrsa -out "${KEY_FILE}" "${KEY_BITS}"

echo "Generating self-signed Root CA certificate..."
openssl req -x509 -new -nodes \
  -key "${KEY_FILE}" \
  -sha256 \
  -days "${DAYS}" \
  -out "${PEM_FILE}" \
  -subj "/CN=${CN}/O=${O}/C=${C}"

echo
echo "=== Certificate ==="
openssl x509 -in "${PEM_FILE}" -noout -subject -dates
echo
echo "=== Output files ==="
echo "  PEM (upload): ${PEM_FILE}"
echo "  KEY  (local): ${KEY_FILE}"
echo
echo "Upload ${PEM_FILE} when creating PKI Root Cert via Import Root Certificate."
