#nama : Refal isya' rasya pratama
#kelas:XI-TKJ 1
#no.absen:23
#soal:Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan dengan eksponen tertentu.

def hitung_pangkat(bilangan, eksponen):
    hasil = 1
    for _ in range(eksponen):
        hasil *= bilangan
    return hasil

# Contoh penggunaan
bilangan = float(input("Masukkan bilangan: "))
eksponen = int(input("Masukkan eksponen: "))
hasil_pangkat = hitung_pangkat(bilangan, eksponen)
print(f"Hasil dari {bilangan}^{eksponen} adalah {hasil_pangkat}")
