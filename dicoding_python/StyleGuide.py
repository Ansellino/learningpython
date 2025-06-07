'''
# Python Style Guide
## Pycodestyle adalah aplikasi open source (berlisensi MIT/Expat) untuk membantu mengecek kode terkait gaya penulisan kode dengan konvensi PEP8.

pip install pycodestyle 

## Pylint adalah aplikasi open source (berlisensi GPL v2) untuk melakukan analisis kode Python, mengecek untuk kesalahan (error) pemrograman, memaksakan standar penulisan kode dengan mengecek penulisan kode yang tidak baik, serta memberikan saran untuk refactoring sederhana.
pip install pylint

## Flake8 adalah aplikasi open source (berlisensi MIT) yang membungkus sejumlah kemampuan aplikasi lain, seperti pycodestyle, pyflakes, dan (skrip/fitur) lainnya.
pip install flake8

## Black adalah proyek open source yang dikembangkan di repository Python Software Foundation (PSF) dengan lisensi MIT.
pip install black

## YAPF adalah proyek open source yang dikembangkan di repository Google dengan lisensi Apache.
pip install yapf

## autopep8 adalah proyek open source (berlisensi MIT) yang termasuk paling awal untuk memformat kode dengan bantuan lint pycodestyle.
pip install autopep8

## FILES
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )
'''

