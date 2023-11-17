#nama : Refal isya' rasya pratama
#kelas:XI-TKJ 1
#no.absen:23
#soal:Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.

def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * hitung_faktorial(n - 1)

# Contoh penggunaan
bilangan = int(input("Masukkan bilangan untuk dihitung faktorialnya: "))
hasil_faktorial = hitung_faktorial(bilangan)
print(f"Faktorial dari {bilangan} adalah {hasil_faktorial}")
