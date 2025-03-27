def konversi_suhu():
    """
    Fungsi untuk mengonversi suhu antara Celsius dan Fahrenheit.
    """
    pilihan = input("Masukkan 'C' untuk mengonversi Celsius ke Fahrenheit, atau 'F' untuk mengonversi Fahrenheit ke Celsius: ").upper()

    if pilihan == 'C':
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} derajat Celsius sama dengan {fahrenheit:.2f} derajat Fahrenheit")
    elif pilihan == 'F':
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} derajat Fahrenheit sama dengan {celsius:.2f} derajat Celsius")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

konversi_suhu()