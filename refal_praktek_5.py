#nama : Refal isya' rasya pratama
#kelas:XI-TKJ 1
#no.absen:23
#soal:Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.



def fibonacci(n):
    if n <= 0:
        return "Input harus lebih besar dari 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Contoh penggunaan
n = int(input("Masukkan nilai n untuk bilangan Fibonacci ke-n: "))
hasil_fibonacci = fibonacci(n)
print(f"Bilangan Fibonacci ke-{n} adalah {hasil_fibonacci}")