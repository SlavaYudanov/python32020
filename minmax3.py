N = int(input("Введите количество прямоугольников"))
m = 0
for i in range (N):
a = int(input("Введите стороны прямоугольника"))
b = int(input())
P = 2*(a+b)
if (i==1):
m = P
if (P > m):
m = P
print(m)








