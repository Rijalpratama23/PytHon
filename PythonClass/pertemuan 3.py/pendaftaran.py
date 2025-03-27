nama = str(input("Masukan Nama : "))
tempatLahir = str(input("Masukan Tempat Lahir : "))
tanggalLahir = int(input("Masukan Tanggal Lahir : "))
tahunLahir = int(input("Masukan Tahun Lahir : "))
jenisKelamin = str(input("Masukan Jenis Kelamin Anda : "))
nilaiEnglish = int(input("Masukan Nilai English : "))
nilaiMtk = int(input("Masukan Nilai Matematika : "))
nilaiIndo = int(input("Maasukan Nilai B.Indonesia : "))

nilaiRataRata = (nilaiEnglish + nilaiMtk + nilaiIndo)/3

if tahunLahir <1999: 
    hasil = "Anda tidak diterima karena masalah umur"
elif nilaiRataRata >=80 and jenisKelamin == "laki-laki":
    hasil = "Anda  Diasarankan Masuk Teknik Informatika"
elif nilaiRataRata >=80 and jenisKelamin == "perempuan":
    hasil = "Anda Disarankan Masuk Sistem Informasi"
else :
    hasil = "Anda Disarankan Masuk DKV"
   
print(hasil)