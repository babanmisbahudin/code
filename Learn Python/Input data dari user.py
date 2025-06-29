# Salah satu contoh data yang akan di input user biasanya mengandung pertanyaan.

data = input("Nama Anda:")
print("Nama Anda adalah :", data) #format input data str

data_int =int(input("Umur Anda:")) 
print("Umur Anda adalah :", data_int) #format input data int

data_float =float (input("Berat Badan Anda:"))
print("Berat Badan Anda adalah :", data_float) #format input data float

biner = bool(int(input("Masukan nilai boolean (0 atau 1): ")))
print("data = ",biner,"type =",type(biner)) #format input data bool