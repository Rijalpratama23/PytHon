#menghitung kelayakan seseorang untuk masuk 
#suatu organisasi

def cek_kelayakan_organisasi_PMR():
     #input data peserta test
    jenis_kelamin = input("Masukkan jenis kelamin (Laki-laki/Perempuan): ").lower()
    berat_badan = float(input("Masukkan berat badan (kg): "))
    tinggi_badan = float(input("Masukkan tinggi badan (cm): "))
    usia = int(input("Masukkan usia: "))
    nilai_akademis = float(input("Masukkan nilai rata-rata akademis: "))
    skill = input("Masukkan skill (Menembak/Memanah/Berkuda): ").lower()
    cacat = input("Apakah memiliki anggota tubuh yang cacat? (Ya/Tidak): ").lower()

    # kriteria
    if cacat == "ya":
        print(" Anda Tidak diterima di Organisasi PMR karena memiliki anggota tubuh yang cacat.")
    elif jenis_kelamin == "perempuan":
        if 45 <= berat_badan <= 50 and tinggi_badan >= 165 and usia < 20:
            print(" Anda Diterima di Organisasi PMR sebagai Anggota.")
        else:
            print("Tidak diterima di Organisasi PMR.")
    elif jenis_kelamin == "laki-laki":
        if berat_badan <= 70 and tinggi_badan >= 170 and usia <= 25:
            print("Diterima di Organisasi PMR sebagai Anggota.")
        elif nilai_akademis >= 90 and usia < 30:
            print("Diterima di Organisasi PMR sebagai Anggota.")
        elif skill in ["menembak", "memanah", "berkuda"]:
            print("Diterima di Organisasi PMR sebagai Anggota.")
        else:
            print("Tidak diterima di Organisasi PMR.")
    else:
        print("Jenis kelamin tidak valid.")

cek_kelayakan_organisasi_PMR()