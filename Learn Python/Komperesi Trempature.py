# Latihan Perhitungan Sederhana Temperatur

# Input suhu dalam Celcius
celcius = float(input("Masukkan suhu dalam Celcius: "))
print("Suhu adalah:", celcius," Celcius")

# Konversi ke Reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur:", reamur, "Reamur")

# Konversi ke Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit:", fahrenheit, "Fahrenheit")

# Konversi ke Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin:", kelvin, "Kelvin")


# PR : farenheit ke kelvin
fahrenheit = float(input("Masukan Suhu Fahrenheit : "))
celcius    = (5/9) * (fahrenheit - 32)
kelvin     = (celcius + 273)
print("Suhu dalam Kelvin : ", kelvin)

# PR : kelvin ke fahrenheit
kelvin     = float(input("Masukan Suhu Dalam kelvin : "))
celcius    = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit : ", fahrenheit)

