def hitung_ipk():
    # Daftar mata kuliah
    matakuliah = ["Algoritma", "Perancangan Objek", "Kalkulus", "Etika Profesi", "Databases", "English"]
    total_sks = 0
    total_bobot = 0

    # Meminta input nilai dan sks untuk setiap mata kuliah
    for matkul in matakuliah:
        nilai = float(input(f"Masukkan nilai untuk {matkul}: "))
        sks = int(input(f"Masukkan jumlah SKS untuk {matkul}: "))

        # Menghitung bobot nilai
        if nilai < 30:
            bobot = 0
        elif nilai <= 34:
            bobot = 1
        elif nilai <= 39:
            bobot = 1.25
        elif nilai <= 44:
            bobot = 1.5
        elif nilai <= 49:
            bobot = 1.75
        elif nilai <= 54:
            bobot = 2
        elif nilai <= 59:
            bobot = 2.25
        elif nilai <= 64:
            bobot = 2.5
        elif nilai <= 69:
            bobot = 2.75
        elif nilai <= 74:
            bobot = 3
        elif nilai <= 79:
            bobot = 3.5
        elif nilai <= 84 :
            bobot = 3.5
        elif nilai <= 89:
            bobot =3.73
        else:
            bobot = 4

        total_sks += sks
        total_bobot += bobot * sks

    # Menghitung IPK
    ipk = total_bobot / total_sks

    return ipk

# Memanggil fungsi untuk menghitung IPK
semester_ipk = hitung_ipk()
print(f"IPK Anda untuk semester ini adalah: {semester_ipk}")