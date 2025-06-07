class MyClass:
    def __init__(self):
        self._private_var = 42   # Variabel non publik dengan awalan satu garis bawah
        self._secret_list = [1, 2, 3]  # Variabel non publik lainnya

    def _private_method(self):
        print("Ini adalah method non publik")

    def public_method(self):
        print("Ini adalah method publik")
        self._private_method()  # Method publik dapat memanggil method non publik