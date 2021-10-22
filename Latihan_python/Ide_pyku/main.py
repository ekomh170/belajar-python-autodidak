import os
import py_compile

os.system('cls')

print("\nApps Sederhana")
print("By  : Eko Muchamad Haryono\n")

Judul1 = "1. Kalkulator Sederhana"
Judul2 = "2. Kalkulator Suhu Sederhana"

print(Judul1)
print(Judul2)

data = int(input("Masukan Data 1 :"))

os.system('cls')

if data == 1:
    pass
    print("======Kalkulator Sederhana======= ")

    kali = "kali"
    bagi = "bagi"
    tambah = "tambah"
    kurang = "kurang"
    pangkat = "pangkat"
    persen = "persen"
    floor = "floor"

    print("\nNama Operasi Hitung :")
    print(kali)
    print(bagi)
    print(tambah)
    print(kurang)
    print(pangkat)
    print(persen)
    print(floor, "\n")

    op = input("Masukan Nama Operasi Hitung :")
    a = int(input("Masukan Angka Pertama :"))
    b = int(input("Masukan Angka Kedua :"))

    #   Operator Perkalian  *
    if kali == op:
        pass
        hasil = a * b
        print(a, '*', b, '=', hasil)

    elif bagi == op:
        pass
        #   Operator Pembagian  /
        hasil = a / b
        print(a, '/', b, '=', hasil)

    elif tambah == op:
        pass
        #   Operator Pertambahan  +
        hasil = a + b
        print(a, '+', b, '=', hasil)

    elif kurang == op:
        pass
        #   Operator Pengurangan  -
        hasil = a - b
        print(a, '-', b, '=', hasil)

    elif pangkat == op:
        pass
        #   Operator  Pangkat  **
        hasil = a ** b
        print(a, '**', b, '=', hasil)

    elif persen == op:
        pass
        #   Operator Persen  %
        hasil = a % b
        print(a, '%', b, '=', hasil)

    elif floor == op:
        pass
        #   Operator Floor Division  //
        hasil = a // b
        print(a, '//', b, '=', hasil)

    else:
        print("Operator Tidak Terdefinisikan Mohon Coba Lagi")

# ===========KONDISI 2 ====================
elif data == 2:
    print("\nProgram Konversi Temperatur\n")

    celcius = "celcius"
    reamur = "reamur"
    fahrenheit = "fahrenheit"
    kelvin = "kelvin"

    print("Nama Suhu - Suhu Yang Telah Teridentifikasi :")
    print(celcius)
    print(reamur)
    print(fahrenheit)
    print(kelvin)

    cek_suhu = input('Nama Suhu Yg Di Cek :')
    # CELCIUS
    # celcius(C)
    if celcius == cek_suhu:
        pass
        celcius = float(input('Masukan angka suhu dalam celcius :'))
        print("Suhu adalah ", celcius, "C")

        # reamur(R)
        reamur = (4/5) * celcius
        print("Suhu adalah ", reamur, "R")

        # fahrenheit
        fahrenheit = ((9/5) * celcius) + 32
        print("Suhu adalah", fahrenheit, "F")

        # kelvin
        kelvin = celcius + 273
        print("Suhu adalah", kelvin, "K")
        # CELCIUS

    elif reamur == cek_suhu:
        pass
        # CELCIUS
        # celcius(C)
        celcius = float(input('Masukan suhu dalam celcius :'))
        print("Suhu adalah ", celcius, "C")

        # reamur(R)
        reamur = (4/5) * celcius
        print("Suhu adalah ", reamur, "R")

        # fahrenheit
        fahrenheit = ((9/5) * celcius) + 32
        print("Suhu adalah", fahrenheit, "F")

        # kelvin
        kelvin = celcius + 273
        print("Suhu adalah", kelvin, "K")
        # CELCIUS

    elif fahrenheit == cek_suhu:
        pass
        # CELCIUS
        # celcius(C)
        celcius = float(input('Masukan suhu dalam celcius :'))
        print("Suhu adalah ", celcius, "C")

        # reamur(R)
        reamur = (4/5) * celcius
        print("Suhu adalah ", reamur, "R")

        # fahrenheit
        fahrenheit = ((9/5) * celcius) + 32
        print("Suhu adalah", fahrenheit, "F")

        # kelvin
        kelvin = celcius + 273
        print("Suhu adalah", kelvin, "K")
        # CELCIUS

    elif kelvin == cek_suhu:
        pass
        # CELCIUS
        # celcius(C)
        celcius = float(input('Masukan suhu dalam celcius :'))
        print("Suhu adalah ", celcius, "C")

        # reamur(R)
        reamur = (4/5) * celcius
        print("Suhu adalah ", reamur, "R")

        # fahrenheit
        fahrenheit = ((9/5) * celcius) + 32
        print("Suhu adalah", fahrenheit, "F")

        # kelvin
        kelvin = celcius + 273
        print("Suhu adalah", kelvin, "K")
        # CELCIUS

    else:
        print("Suhu Tidak Teridentifikasi")

else:
    print("Data Tidak Di Ketahui")
