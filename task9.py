n = int(input("Введите число : "))
chek = 1
for x in range(1, n+1):
    factorial1 = chek * x
    chek =factorial1
print(factorial1)