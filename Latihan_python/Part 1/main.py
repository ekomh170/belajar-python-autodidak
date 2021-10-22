import time
start_time = time.time()

print("Hello")
print("World")
print("Hello World")

a = 10
b = 20

print(a + b)

for i in range(1, 1000):
    a = 10

print(time.time() - start_time, "detail waktu")
# Kita bisa mengcompile python 3 ke
# yang nama nya bytecode
# alasan kita membuat kedalam bytcode agar kode kita menjadi
# lebih secure dan aman
# cara nya : python -m py_compile NamaSouceCodeAnda
