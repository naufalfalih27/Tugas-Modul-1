#mencari satu angka Fibonacci pada posisi ke-n
def fibonacci_ke(n):
    a, b = 0, 1
    for i in range(n):
        #update nilai: a jadi b, dan b jadi hasil penjumlahan a + b    
        a, b = b, a + b
    return a

#mencetak seluruh barisan Fibonacci sampai suku ke-n
def Barisan_Fibonacci(n):
    a, b = 0, 1
    barisan = [] #list kosong untuk menampung angka
    for i in range(n):
        a, b = b, a + b
        barisan.append(a) #memasukkan angka hasil penjumlahan ke dalam list
    print("Barisannya:", barisan)

n = int(input("Test sampai suku ke berapa ? "))

hasil = fibonacci_ke(n)
print("Angka Fibonacci ke-", n, "adalah:", hasil)

Barisan_Fibonacci(n)