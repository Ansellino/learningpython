def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()

"""
Output:
Sebelum fungsi dieksekusi.
Hello, world!
Setelah fungsi dieksekusi.

Penjelasan dari contoh di atas adalah berikut.

1. Pertama, kita mendefinisikan sebuah fungsi bernama my_decorator. Dekorator ini menerima sebuah fungsi func sebagai parameternya.
2. Dalam fungsi my_decorator, kita mendefinisikan fungsi wrapper(). Fungsi wrapper() bertindak sebagai "pembungkus" yang menambahkan perilaku sebelum dan setelah eksekusi dari fungsi func.
3. Setelah itu, fungsi  my_decorator mengembalikan (return) fungsi wrapper sebagai hasilnya. Return ini juga menyebabkan fungsi wrapper dijalankan.
4. Kemudian, kita mendefinisikan fungsi say_hello(). Fungsi ini akan menjadi target dekorasi.
5. Untuk mendekorasi say_hello(), kita menggunakan simbol "@" diikuti dengan nama dekorator, yaitu @my_decorator sebelum mendefinisikan fungsi say_hello.
6. Jadi, secara alur, ketika fungsi say_hello() dipanggil, sebenarnya yang dieksekusi adalah fungsi wrapper() yang menjadi hasil dari dekorasi. Oleh karena itu, pesan "Sebelum fungsi dieksekusi." dicetak terlebih dahulu, kemudian fungsi say_hello() dieksekusi dan mencetak "Hello, world!", lalu akhirnya, pesan "Setelah fungsi dieksekusi." dicetak.
Dekorator sangat berguna untuk menambahkan fungsionalitas tambahan pada suatu fungsi atau metode tanpa harus mengubah kode asli dari fungsi tersebut. Anda bisa membaca lebih dalam mengenai dekorator pada laman ini.
"""