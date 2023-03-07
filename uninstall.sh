#!/bin/bash
#
# Uninstall script for gosplat
#
# Removes gosplat from users computer

gosplat_dest="$HOME/.local/share/gosplat"
gosplat_binary_dest="$HOME/.local/bin/gosplat"

rm -rf "$gosplat_dest"
rm -f "$gosplat_binary_dest"

echo "Gosplat has been removed, thank you for trying Gosplat!"
