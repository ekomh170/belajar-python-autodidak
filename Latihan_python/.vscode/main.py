# a= 10 , a adalah variable dengan
# nilai 10 tipe data nya adalah int / interger  = Angka
from ctypes import c_double, c_long, c_char

data_interger = 1

# tipe data : Angka Satuan Int yang tidak ada koma
print("data : ", data_interger)
print("- tipe data nya  : ", type(data_interger))
print()

# tipe data : angka koma Float
data_float = 1.5

print("data : ", data_float)
print("- tipe data nya  : ", type(data_float))
print()

# tipe data : Kumpulan Karakter str(string)
data_string = "Ucup  1.5"

print("data : ", data_string)
print("- tipe data nya  : ", type(data_string))
print()

# tipe data : Binery True/False (Boolean)
data_bool = False

print("data : ", data_bool)
print("- tipe data nya  : ", type(data_bool))
print()

# tipe data khusus
# bilangan kompleks
data_complex = complex(5, 6)

print("data : ", data_complex)
print("- tipe data nya  : ", type(data_complex))
print()

# tipe data dari bahas C

data_c_double = c_double(10.5)

print("data : ", data_c_double)
print("- tipe data nya  : ", type(data_c_double))
print()
