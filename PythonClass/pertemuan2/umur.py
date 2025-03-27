#menentukan panggilan berdasarkan umur
umur = int (input("masukan umur : "))
if umur <=2 :
    print("umur", umur, "disebut bayi")
elif umur >=2 and umur<=5:
    print("umur",umur,"disebut balita")
elif umur >=5 and umur<=12:
    print("umur",umur,"disebut anak-anak")
elif umur>=12 and umur <=17:
    print("umur",umur,"disebut remaja")
elif umur >=17 and umur<=30:
    print("umur",umur,"disebut dewasa")
else:
    print("umur",umur,"disebut orangtua")