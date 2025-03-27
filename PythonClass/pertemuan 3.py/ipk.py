def skorToBobot (nilai) :
    if nilai >= 90:
        return 4.00 
    elif nilai >= 85:
        return 3.75
    elif nilai >= 80:
        return 3.50
    elif nilai >= 75:
        return 3.25
    elif nilai >= 70:
        return 3.00 
    elif nilai >= 65:
        return 2.75
    elif nilai >= 60:
        return 2.50
    elif nilai >= 55:
        return 2.25
    elif nilai >= 50:
        return 2.00
    elif nilai >=45:
        return 1.75
    elif nilai >=40:
        return 1.50
    elif nilai >= 35:
        return 1.25
    elif nilai >= 30:
        return 1.00
    else :
        return 0.00
    
algoritma = float(input("Masukan nilai akhir mata kuliah Algoritma anda : "))
sksAlgoritma = int(input("Masukan jumlah SKS : "))
totalAlgoritma = sksAlgoritma * skorToBobot(algoritma)

perancanganObjek = float(input("Masukan nilai akhir mata kuliah PBO anda : "))
sksPerancanganObjek = int(input("Masukan jumlah SKS : "))
totalPerancanganObjek = sksPerancanganObjek * skorToBobot(perancanganObjek)

kalkulus = float(input("Masukan nilai akhir mata kuliah Kalkulus anda : "))
sksKalkulus = int(input("Masukan jumlah SKS : "))
totalKalkulus = sksKalkulus * skorToBobot(kalkulus)

etikaProfesi = float(input("Masukan nilai akhir mata kuliah Etika Profesi anda : "))    
sksEtika = int(input("Masukan jumlah SKS : "))
totalEtika = sksEtika * skorToBobot(etikaProfesi)

databases = float(input("Masukan nilai akhir mata kuliah Database anda : "))
sksDatabases = int(input("Masukan jumlah SKS : "))
totalDatabase = sksDatabases * skorToBobot(databases)

english = float(input("Masukan nilai akhir mata kuliah English anda : ")) 
sksEnglish = int(input("Masukan jumlah SKS : "))
totalEnglish = sksEnglish * skorToBobot(english)

totalSks = sksAlgoritma + sksPerancanganObjek + sksKalkulus + sksEtika + sksDatabases + sksEnglish

IPK = (totalAlgoritma + totalPerancanganObjek + totalKalkulus + totalEtika + totalDatabase + totalEnglish) / totalSks

print("Nilai IPK anda adalah", IPK)