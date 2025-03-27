def hitung_luas(sisi1, sisi2, sisi3):
    s = (sisi1 + sisi2 + sisi3) / 2
    luas = (s * (s - sisi1) * (s - sisi2) * (s - sisi3)) ** 0.5
    return luas

def hitung_keliling(sisi1, sisi2, sisi3):
    keliling = sisi1 + sisi2 + sisi3
    return keliling

sisi1 = float(input("Masukkan panjang sisi 1: "))
sisi2 = float(input("Masukkan panjang sisi 2: "))
sisi3 = float(input("Masukkan panjang sisi 3: "))

luas = hitung_luas(sisi1, sisi2, sisi3)
keliling = hitung_keliling(sisi1, sisi2, sisi3)

print("Luas segitiga:", luas)
print("Keliling segitiga:", keliling)
