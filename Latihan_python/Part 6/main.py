print("\nProgram Konversi Temperatur")

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
