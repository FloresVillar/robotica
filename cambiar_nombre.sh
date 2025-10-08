#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

CARPETA="${1:-$(pwd)}"

cd "$CARPETA" || exit

for archivo in *;do
 [[ -f "$archivo" ]] || continue
 IFS="_." read -r izq centro der <<< "$archivo"
 [[ -n "${der:-}" && -n "&{izq:-}"  && -n "${centro:-}" ]] || continue
 nuevo_nombre="${centro}_${izq}.${der}"
 mv -- "${archivo}" "${nuevo_nombre}" 
 echo "archivo renombrado"
done
