# OPERASI ARITMATIKA
import os
import py_compile

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
