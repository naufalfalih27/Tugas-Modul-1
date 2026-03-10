def fibonacci_ke(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def Barisan_Fibonacci(n):
    a, b = 0, 1
    barisan = []
    for i in range(n):
        a, b = b, a + b
        barisan.append(a)
    print("Barisannya:", barisan)

n = int(input("Test sampai suku ke berapa ? "))

hasil = fibonacci_ke(n)
print("Angka Fibonacci ke-", n, "adalah:", hasil)

Barisan_Fibonacci(n)