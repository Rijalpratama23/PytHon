#menentukan kriteria kelulusan 
mtk = int(input("masukan nilai Matematika: "))
ips = int (input("masukan nilai ips: "))
ipa = int(input("masukan nilai ipa: "))
indo = int(input("masukan nilai B.indo: "))
english = int(input("masukan nilai english"))

penilaianA = (english+mtk+indo)/3
penilaianB = (mtk+ips+ipa+indo+english)/5

if  penilaianA >=75 :
    hasil = "Lulus"
elif penilaianB >=70 :
    hasil = "Lulus"
elif mtk ^ english >=90 :
    hasil = "Lulus"
else :
    hasil = "Tidak Lulus"

print("anda",hasil,"pada ujian ini")

 