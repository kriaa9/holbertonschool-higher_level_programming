#!/usr/bin/env bash
set -euo pipefail

chmod +x 19-copy_list.py
for file in *-main.py; do
    [[ -e "$file" ]] || continue
    chmod +x "$file"
done

echo "Executable permissions updated."
