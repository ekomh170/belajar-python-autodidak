print()
A = "Aku Mau Belajar"
B = 3.8
C = "Python"

print(A, C, B)
print("Aku Belajar Casting", C, B)
print("==================================")

# Belajar Casting
# Merubah dari tipe ke tipe lain
# tipe data = int, float, str, bool

print("====INTERGER====")

data_int = 9
print("data = ", data_int, ", type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)


print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))
print()

print("====Float====")

data_float = 10.9
print("data = ", data_float, ", type = ", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))
print()

print("====Bool====")

data_bool = False
print("data = ", data_bool, ", type = ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)

print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_str, ", type = ", type(data_str))
print()

print("====STR====")

data_str = "0"

data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)

print("data = ", data_int, ", type = ", type(data_int))
print("data = ", data_float, ", type = ", type(data_float))
print("data = ", data_str, ", type = ", type(data_str))
print("data = ", data_bool, ", type = ", type(data_bool))
print()
