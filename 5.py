n = int(input("Enter number of terms:"))
a = 1
b = 2
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
