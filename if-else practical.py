x = int(input("Введите число x: "))
y = int(input("Введите число y: "))

if x == 0:
   print("error")
else: 
   z = int(y / x)
   print(x, y, z)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
s = (a * b)
if s > 500:
   s = s * 0.9
   print(s)
else:
   print(s)


