def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))
"""
Parameter ini dapat menampung jumlah keyword argument yang bervariasi saat pemanggilan fungsi. 
Parameter ini ditentukan dengan menggunakan sintaks **kwargs yang berperan sebagai dictionary (seperti tipe datanya).
Argumen pada pemanggil fungsi akan berperan sebagai value dan parameter (identifier) berperan sebagai key.
Output:
nama: Dicoding, usia: 17, pekerjaan: Python Programmer,
"""