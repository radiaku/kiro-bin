# Maintainer: AlphaLynx <alphalynx@protonmail.com>

pkgname=kiro-bin
_name="${pkgname%-bin}"
pkgver=0.1.0
pkgrel=1
pkgdesc="The AI IDE for prototype to production"
arch=('x86_64')
url="https://kiro.dev/"
license=('LicenseRef-AWS-IPL')
depends=(
    'alsa-lib'
    'at-spi2-core'
    'bash'
    'cairo'
    'dbus'
    'expat'
    'gcc-libs'
    'glib2'
    'glibc'
    'gtk3'
    'libcups'
    'libdrm'
    'libx11'
    'libxcb'
    'libxcomposite'
    'libxdamage'
    'libxext'
    'libxfixes'
    'libxkbcommon'
    'libxkbfile'
    'libxrandr'
    'mesa'
    'nodejs'
    'nspr'
    'nss'
    'pango'
)
provides=("$_name")
conflicts=("$_name")
options=(!strip)
source=(
    "$_name-202507140012.tar.gz::https://prod.download.desktop.kiro.dev/releases/202507140012--distro-linux-x64-tar-gz/202507140012-distro-linux-x64.tar.gz"
    "$_name.desktop"
    "$_name-url-handler.desktop"
    "$_name-workspace.xml"
)
b2sums=('39a2b0fb091734fda20e8bbcaa8eb2dbf1a3cf95cdd0dcd06bf9137a2e203a5d1246a409a4a21fb04023d2696f2acda648d2e49c2a730d5cdc86819429734643'
        'e1c5ba95a32cc5f980e583f3ae6d94ed9418069409c6696d4e56088404a9ce83efc0833106b625a93d387fc0ffb1b4174525bb4dfb8a966f510f0389b821f756'
        '2998ee92f434b5e45c34cfa374d7f9a4ba604ec2b0af05f28cc059e81a8af808318a68efacf9f12399d339830f3f9f08a1201d8a89592f1ff9af273209f075fe'
        '0f855638664cd605ec41cd5b03e0e989043b6dcbeae2e0990653b1c8e8526eb567b70bd9c7c17e2a8c19ff2d4ccd49fd8607d667b629a372ee01511021441a6d')

package() {
    install -d "$pkgdir/opt/Kiro"
    cp -r "$srcdir/Kiro/"* "$pkgdir/opt/Kiro"

    install -d "$pkgdir/usr/bin"
    ln -s "/opt/Kiro/$_name" "$pkgdir/usr/bin/$_name"

    mkdir -p "$pkgdir/usr/share/licenses/$pkgname"
    ln -s /opt/Kiro/resources/app/LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"

    mkdir -p "$pkgdir/usr/share/pixmaps"
    ln -s /opt/Kiro/resources/app/resources/linux/code.png "$pkgdir/usr/share/pixmaps/$_name.png"

    mkdir -p "$pkgdir/usr/share/bash-completion/completions"
    ln -s /opt/Kiro/resources/completions/bash/$_name \
        "$pkgdir/usr/share/bash-completion/completions/$name"

    mkdir -p "$pkgdir/usr/share/zsh/site-functions"
    ln -s /opt/Kiro/resources/completions/zsh/_$_name \
        "$pkgdir/usr/share/zsh/site-functions/_$_name"

    install -Dm644 $_name.desktop "$pkgdir/usr/share/applications/$_name.desktop"
    install -Dm644 $_name-url-handler.desktop \
        "$pkgdir/usr/share/applications/$_name-url-handler.desktop"
    install -Dm644 $_name-workspace.xml "$pkgdir/usr/share/mime/packages/$_name-workspace.xml"
}

# vim: set ts=4 sw=4 sts=4 et:
