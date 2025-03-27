belanja = int(input("Masukan total belanja anda: "))
keterangan = ""

if belanja > 60_000:
    diskon = belanja * 10/100
    total = belanja - diskon
    keterangan = "Selamat anda mendapat diskon, karena berbelanja lebih dari 60 ribu rupiah"
    
else:
    total = belanja
    keterangan = "Anda tidak mendapat diskon karena berbelanja kurang dari 60 riburupiah"
    
print ("total belanjaan anda adalah %i rupiah"%total + keterangan)