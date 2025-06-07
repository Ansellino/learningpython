def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

"""
Parameter ini menampung jumlah argumen posisi yang bervariasi saat pemanggilan fungsi.
Parameter ini ditentukan dengan menggunakan sintaks *args.
Output:
<class 'tuple'>
6
"""