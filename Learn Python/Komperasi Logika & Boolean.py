# Membuat gabungan area rentang dan angka +++++3 dan 10++++++


inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 \natau lebih besar dari 10 :1 ->"))

# ++++3--------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# -----------10++++++
# Memeriksa angka lebih besar dari 10
isLebihBesarDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihBesarDari)

# +++++3-------10+++++
isCorrect = isKurangDari or isLebihBesarDari
print("angka yang dimasukkan:", isCorrect)

print("====================================")

# ------3++++++10------- (Kasus Irisan)
inputUser = float(input("Masukkan angka yang bernilai lebih dari 3 \ndan kurang dari 10 : ->"))

# ------3++++++++++++++ lebih dari 3
isLebihDari = (inputUser > 3)
print("Lebih dari 3 =", isLebihDari)

# +++++++10---------- kurang dari 10
isKurangDari = (inputUser < 10)
print("Kurang dari 10 =", isKurangDari)