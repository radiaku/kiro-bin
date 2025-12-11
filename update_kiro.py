#!/usr/bin/env python3
"""Update kiro-bin PKGBUILD and .SRCINFO to a new version."""

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path
from urllib.request import urlopen, urlretrieve

BASE_URL = "https://prod.download.desktop.kiro.dev/releases/stable/linux-x64/signed"
METADATA_URL = "https://prod.download.desktop.kiro.dev/stable/metadata-linux-x64-stable.json"


def b2sum(filepath: Path) -> str:
    """Calculate BLAKE2b hash of a file."""
    h = hashlib.blake2b()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def download_file(url: str, dest: Path) -> None:
    """Download a file from URL."""
    print(f"Downloading {url}...")
    urlretrieve(url, dest)


def get_urls(version: str) -> dict[str, str]:
    """Get download URLs for a version."""
    base = f"{BASE_URL}/{version}/tar"
    return {
        "tarball": f"{base}/kiro-ide-{version}-stable-linux-x64.tar.gz",
        "certificate": f"{base}/certificate.pem",
        "signature": f"{base}/signature.bin",
    }


def update_pkgbuild(version: str, sums: dict[str, str]) -> None:
    """Update PKGBUILD with new version and checksums."""
    pkgbuild = Path("PKGBUILD")
    content = pkgbuild.read_text()

    # Update version
    content = re.sub(r"pkgver=[\d.]+", f"pkgver={version}", content)

    # Update b2sums (first 3 entries)
    pattern = r"(b2sums=\()'[a-f0-9]+'\s+'[a-f0-9]+'\s+'[a-f0-9]+'"
    replacement = rf"\1'{sums['tarball']}'\n        '{sums['certificate']}'\n        '{sums['signature']}'"
    content = re.sub(pattern, replacement, content)

    pkgbuild.write_text(content)
    print("Updated PKGBUILD")


def update_srcinfo(version: str, sums: dict[str, str]) -> None:
    """Update .SRCINFO with new version and checksums."""
    srcinfo = Path(".SRCINFO")
    content = srcinfo.read_text()

    # Update version
    content = re.sub(r"pkgver = [\d.]+", f"pkgver = {version}", content)

    # Update source URLs
    content = re.sub(
        r"source = kiro-[\d.]+\.tar\.gz::.*?\.tar\.gz",
        f"source = kiro-{version}.tar.gz::{BASE_URL}/{version}/tar/kiro-ide-{version}-stable-linux-x64.tar.gz",
        content,
    )
    content = re.sub(
        r"source = kiro-certificate\.pem::.*?certificate\.pem",
        f"source = kiro-certificate.pem::{BASE_URL}/{version}/tar/certificate.pem",
        content,
    )
    content = re.sub(
        r"source = kiro-[\d.]+-signature\.bin::.*?signature\.bin",
        f"source = kiro-{version}-signature.bin::{BASE_URL}/{version}/tar/signature.bin",
        content,
    )

    # Update b2sums (first 3)
    lines = content.split("\n")
    new_lines = []
    b2sum_count = 0
    sums_order = ["tarball", "certificate", "signature"]

    for line in lines:
        if line.strip().startswith("b2sums = ") and b2sum_count < 3:
            new_lines.append(f"\tb2sums = {sums[sums_order[b2sum_count]]}")
            b2sum_count += 1
        else:
            new_lines.append(line)

    srcinfo.write_text("\n".join(new_lines))
    print("Updated .SRCINFO")


def get_latest_version() -> str:
    """Fetch the latest version from metadata."""
    print(f"Fetching latest version from {METADATA_URL}...")
    with urlopen(METADATA_URL) as response:
        data = json.loads(response.read())
        return data["version"]


def main():
    parser = argparse.ArgumentParser(description="Update kiro-bin package to a new version")
    parser.add_argument("version", nargs="?", help="Version to update to (e.g., 0.7.21). If omitted, fetches latest.")
    args = parser.parse_args()

    version = args.version
    if not version:
        version = get_latest_version()
        print(f"Latest version: {version}")
    urls = get_urls(version)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)
        files = {
            "tarball": tmppath / "kiro.tar.gz",
            "certificate": tmppath / "certificate.pem",
            "signature": tmppath / "signature.bin",
        }

        # Download files
        for key, url in urls.items():
            download_file(url, files[key])

        # Calculate checksums
        print("Calculating checksums...")
        sums = {key: b2sum(path) for key, path in files.items()}

        for key, checksum in sums.items():
            print(f"  {key}: {checksum[:16]}...")

    # Update files
    update_pkgbuild(version, sums)
    update_srcinfo(version, sums)

    print(f"\nDone! Updated to version {version}")
    print("You may want to run 'makepkg --printsrcinfo > .SRCINFO' to regenerate .SRCINFO")


if __name__ == "__main__":
    main()
