#nama : Refal isya' rasya pratama
#kelas:XI-TKJ 1
#no.absen:23
#soal:Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga batas tertentu yang ditentukan pengguna.

def total_deret_ganjil(batas):
    total = 0
    for i in range(1, batas + 1, 2):
        total += i
    return total

# Contoh penggunaan
batas_tertentu = int(input("Masukkan batas tertentu: "))
hasil_total = total_deret_ganjil(batas_tertentu)
print(f"Total deret ganjil hingga batas {batas_tertentu} adalah {hasil_total}")