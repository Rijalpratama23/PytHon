# Meminta input dari pengguna
bilangan1 =int(input("Masukkan bilangan pertama: "))
bilangan2 =int(input("Masukkan bilangan kedua: "))
bilangan3 =int(input("Masukkan bilangan ketiga: "))

# Menentukan bilangan mana yang lebih kecil
bilangan_terkecil = bilangan1
if bilangan2 < bilangan_terkecil:
    bilangan_terkecil = bilangan2
if bilangan3 < bilangan_terkecil:
    bilangan_terkecil = bilangan3

# Menampilkan hasil
print("Bilangan terkecil adalah:", bilangan_terkecil)
