# kiro-bin

Arch Linux package for [Kiro](https://kiro.dev/) - The AI IDE for prototype to production.

## Installation

```bash
makepkg -si
```

## Updating to a new version

Use the helper script:

```bash
# Automatically fetch and update to latest version
./update_kiro.py
makepkg -si

# Or specify a version
./update_kiro.py 0.7.21
makepkg -si
```

The script downloads the release, calculates checksums, and updates PKGBUILD and .SRCINFO automatically.

## License

By downloading and using Kiro, you agree to:
- [AWS Customer Agreement](https://aws.amazon.com/agreement/)
- [AWS Intellectual Property License](https://aws.amazon.com/legal/aws-ip-license-terms/)
- [Service Terms](https://aws.amazon.com/service-terms/)
- [Privacy Notice](https://aws.amazon.com/privacy/)
