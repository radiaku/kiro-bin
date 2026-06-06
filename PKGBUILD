# Maintainer: AlphaLynx <alphalynx at alphalynx dot dev>

pkgname=kiro-bin
_name="${pkgname%-bin}"
pkgver=0.12.301
pkgrel=1
epoch=1
pkgdesc='The AI IDE for prototype to production'
arch=('x86_64')
url='https://kiro.dev/'
# By downloading and using Kiro, you agree to the following:
#   AWS Customer Agreement: https://aws.amazon.com/agreement/
#   AWS Intellectual Property License: https://aws.amazon.com/legal/aws-ip-license-terms/
#   Service Terms: https://aws.amazon.com/service-terms/
#   Privacy Notice: https://aws.amazon.com/privacy/
license=('LicenseRef-Kiro')
makedepends=('openssl')
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
    'perl'
    'python'
    'systemd-libs'
)
provides=("$_name")
conflicts=("$_name")
options=('!debug' '!strip')
_baseurl=https://prod.download.desktop.kiro.dev/releases/stable/linux-x64/signed/$pkgver/tar
source=(
    "$_name-$pkgver.tar.gz::$_baseurl/kiro-ide-$pkgver-stable-linux-x64.tar.gz"
    "$_name-$pkgver-certificate.pem::$_baseurl/certificate.pem"
    "$_name-$pkgver-signature.bin::$_baseurl/signature.bin"
    "$_name.desktop"
    "$_name-url-handler.desktop"
    "$_name-workspace.xml"
    "Kiro-LICENSE.txt"
)
b2sums=('4ee7be0a4592901f99372e3496dfd87b3f0ac42d9abaaf0f84ed95c0e7fcd8001a12a6675bed27e43e0e59b8a815ea565147bab8428d52d8be408182337c66f5'
        '4cba4d51523a883653b28e04abc4a0e444d7672636153be9c99058b4469137ab2c591466d9452c5471e1577c6ce9a54edca28f14c01e6d66b36b72eb53f92bc8'
        '434d8ef9a919aecb02d40abfc166d4a5b4ca4a430e25ba9aefa90eb194032986d27b3e8d5c5d9817d76dadfae91a27f6d8a9a24a61117990e12653746a4f1cef'
        'd7afb1d5c54c8789e21e0f598837af95f52ea6e8f99708d38c7166b926022ce88cfd246b5fc530f5f1dbfbde1b4633658e441af7356cdee289013e363bd7eab8'
        '7c4eca51844645ee6e642be3cdeb3120ebd4fe308d7f60236b2118536bf5717aff23bb71a308978e491275cdb2ef2e78a295d1554553add681071b909d72ac6b'
        'c422bc883f40209fb165740fdf339911de868acc8a72033730ac07e3c5fd76604737b7efe0b4f894b70520dbd214c5504bd34c284e7c1f0a4438f1f35eee0dbb'
        '4fee11387ffa92e8fba85ca53dcd51906efb5aa0d581002510a66e63916e439c836539de374db5e5b5a4470a1790b6dc0348e7ceb555a8de4dd5210b6c0f7a01')

verify() {
    cd "$SRCDEST"
    openssl x509 -pubkey -noout -in $_name-$pkgver-certificate.pem > kiro-pubkey.pem
    openssl dgst -sha256 -verify kiro-pubkey.pem -signature $_name-$pkgver-signature.bin \
        $_name-$pkgver.tar.gz
}

package() {
    install -dm755 "$pkgdir/opt/Kiro"
    cp -a Kiro/* "$pkgdir/opt/Kiro"
    chmod 4755 "$pkgdir/opt/Kiro/chrome-sandbox"

    install -dm755 "$pkgdir/usr/bin"
    ln -s /opt/Kiro/bin/$_name "$pkgdir/usr/bin/$_name"

    install -Dm644 Kiro-LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"

    install -dm755 "$pkgdir/usr/share/pixmaps"
    ln -s /opt/Kiro/resources/app/resources/linux/code.png "$pkgdir/usr/share/pixmaps/$_name.png"

    install -dm755 "$pkgdir/usr/share/bash-completion/completions"
    install -dm755 "$pkgdir/usr/share/zsh/site-functions"
    ln -s /opt/Kiro/resources/completions/bash/$_name \
        "$pkgdir/usr/share/bash-completion/completions/$_name"
    ln -s /opt/Kiro/resources/completions/zsh/_$_name \
        "$pkgdir/usr/share/zsh/site-functions/_$_name"

    install -Dm644 $_name.desktop \
        "$pkgdir/usr/share/applications/$_name.desktop"
    install -Dm644 $_name-url-handler.desktop \
        "$pkgdir/usr/share/applications/$_name-url-handler.desktop"
    install -Dm644 $_name-workspace.xml \
        "$pkgdir/usr/share/mime/packages/$_name-workspace.xml"
}
