# OPERASI ARITMATIKA

print("====Kalkulator Sederhana==== ")

a = int(input("Masukan Data 1 :"))
b = int(input("Masukan Data 2 :"))

#   Operator Pertambahan  *
hasil = a * b
print(a, '*', b, '=', hasil)

#   Operator Pertambahan  /
hasil = a / b
print(a, '/', b, '=', hasil)

#   Operator Pertambahan  +
hasil = a + b
print(a, '+', b, '=', hasil)

#   Operator Pertambahan  -
hasil = a - b
print(a, '-', b, '=', hasil)

#   Operator Pertambahan  **
hasil = a ** b
print(a, '**', b, '=', hasil)

#   Operator Pertambahan  %
hasil = a % b
print(a, '%', b, '=', hasil)

#   Operator Floor Division  //
hasil = a // b
print(a, '//', b, '=', hasil)

# Prioritas operasi, Operational precedence
'''
    1. ()
    2. eksponen **
    3. perkalian dan modulus
    4.  pertambahan dan pengurangan
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', hasil)

hasil = (x + y) * z
print('(', x, '+', y, ') *', z, '=', hasil)
