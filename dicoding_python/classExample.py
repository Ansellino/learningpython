class Mobil:
    # Atribut kelas
    warna = "Merah"

mobil1 = Mobil()
print(mobil1.warna)

mobil2 = Mobil()
print(mobil2.warna)

# Mengubah atribut kelas
Mobil.warna = "Hitam"

print(mobil1.warna)
print(mobil2.warna)

"""
Output:
Merah
Merah
Hitam
Hitam
"""