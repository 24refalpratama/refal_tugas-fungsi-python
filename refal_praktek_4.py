#nama : Refal isya' rasya pratama
#kelas:XI-TKJ 1
#no.absen:23
#soal:Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.

def hitung_jumlah_digit(bilangan):
    if bilangan < 0:
        bilangan = abs(bilangan)  # Mengambil nilai mutlak jika bilangan negatif

    str_bilangan = str(bilangan)
    jumlah_digit = len(str_bilangan)
    return jumlah_digit

# Contoh penggunaan
bilangan = int(input("Masukkan bilangan: "))
jumlah_digit = hitung_jumlah_digit(bilangan)
print(f"Jumlah digit dari {bilangan} adalah {jumlah_digit}")
