1. Apa Itu Python?
Python adalah bahasa pemrograman yang:

> Simpel dan mudah dibaca
> Cocok untuk pemula
> Dipakai di web, data science, AI, automasi, dll
> Contoh baris kode:

python
Salin
Edit
print("Halo, dunia!")

2. Variabel & Tipe Data
Gunanya untuk menyimpan nilai.

python
Salin
Edit
nama = "Baban"         # string
umur = 30              # integer
tinggi = 1.75          # float
is_muslim = True       # boolean

3. Operasi Matematika
python
Salin
Edit
a = 10
b = 3
print(a + b)     # 13
print(a // b)    # 3  (floor division)
print(a % b)     # 1  (modulus)

4. Input dan Output
python
Salin
Edit
nama = input("Siapa nama kamu? ")
print("Halo,", nama)

5. Percabangan (if-elif-else)
python
Salin
Edit
umur = 20
if umur >= 17:
    print("Boleh bikin KTP")
else:
    print("Belum cukup umur")

6. Perulangan (loop)
For Loop
python
Salin
Edit
for i in range(5):
    print("Ulang ke-", i)
While Loop
python
Salin
Edit
angka = 0
while angka < 5:
    print(angka)
    angka += 1

7. Fungsi (function)
python
Salin
Edit
def sapa(nama):
    print("Halo", nama)

sapa("Baban")

. List dan Dictionary
List (array)
python
Salin
Edit
buah = ["apel", "jeruk", "mangga"]
print(buah[1])  # jeruk
Dictionary (mirip kamus)
python
Salin
Edit
orang = {"nama": "Baban", "umur": 30}
print(orang["nama"])

9. Import Modul
python
Salin
Edit
import math
print(math.sqrt(16))  # 4.0