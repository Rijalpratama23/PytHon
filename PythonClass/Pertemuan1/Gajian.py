#Menghitung Gaji
hari_kerja = int(input("berapa banyak hari kerja anda: "))
gaji_bulanan = int(input("masukan gaji pokok: "))
transpor = int(input("masukan uang transport pokok: "))
makan = int(input("masukan uang pokok: "))
total_transport = transpor * hari_kerja
total_makan = makan * hari_keerja 
lembur = int(input("lembur anda berapa jam: "))

if lembur <= 2:
    total_lembur = lembur * 100_000
    
elif lembur <= 7 :
    lembur = lembur - 2
    total_lembur = (lembur * 150_000) + 200_000

else :
    lembur = lembur - 7 
    total_lembur = (lembur * 150_000) + 950_000

hasil = gaji_bulanan + total_transport + total_makan + total_lembur 
print("total honor anda adalah : " + str(hasil))