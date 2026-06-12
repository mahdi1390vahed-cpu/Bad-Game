[app]

title = Guess
package.name = guess
package.domain = ir.SelvA

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

android.api = 34
android.minapi = 21
android.ndk = 25.1.8937393

log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
