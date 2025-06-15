import time
start_time = time.time()

print("Hello World!")
print("Selamat datang di Python")
print("Python adalah bahasa pemrograman yang mudah dipelajari")

# Komentar khusus python

"""Kita bisa mencomplie python ke dalam bentuk bytecode, caranya buka terminal
python -m py_compile main.py
Hasilnya akan ada folder __pycache__ yang berisi file main.cpython-310.pyc
Kita bisa menjalankan file bytecode tersebut dengan perintah"""

print(time.time() - start_time, "detik")
