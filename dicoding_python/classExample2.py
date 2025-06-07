class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
        
mobil_1 = Mobil('Merah', 'DicodingCar', 160)

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

"""
Output:
Merah
DicodingCar
160
"""