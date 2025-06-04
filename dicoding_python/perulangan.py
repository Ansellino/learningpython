"""
TODO:
Buatlah sebuah variabel bertipe list bernama "evenNumber" dengan ketentuan:
- variabel tersebut menampung bilangan genap dari 0 hingga 500 (ingat 0 dan 500 termasuk).

Tips:
Anda bisa menggunakan loop dan if atau list comprehension untuk memudahkan.
"""

# TODO: Silakan buat kode Anda di bawah ini

#answer 1

evenNumber = [] 
for i in range(0,501,2):
  evenNumber.append(i)
print(evenNumber)

#answer 2
# Menggunakan loop dan if
evenNumber = []
for i in range(0, 501):  # range(0, 501) akan mencakup angka dari 0 hingga 500
    if i % 2 == 0:  # Memeriksa apakah angka genap
        evenNumber.append(i)

# Atau menggunakan list comprehension (lebih ringkas)
evenNumber = [i for i in range(0, 501) if i % 2 == 0]

# Untuk memverifikasi hasilnya (opsional)
# print(evenNumber)
# print(len(evenNumber))