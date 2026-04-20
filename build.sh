#!/bin/bash
set -e

echo "Cleaning old build artifacts and cache..."
rm -rf src/ pkg/ ~/.cache/makepkg/sources/kiro-bin/

echo "Fetching latest version and updating PKGBUILD..."
./update_kiro.py

echo "Regenerating .SRCINFO from PKGBUILD..."
makepkg --printsrcinfo > .SRCINFO

echo "Building and installing package..."
makepkg -si --skippgpcheck

echo "Done!"
