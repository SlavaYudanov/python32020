n = int(input("введите число чисел в последовательности"))
a = []
imn = 0
imx = 0
for i in range(n):
a.append(int(input()))
mn = a[0]
mx = a[0]
for i in range (n):
if a[i]<=mn:
mn = a[i]
imn = i
if a[i]>mx:
mx = a[i]
imx = i
print(mn,imn)
print(mx,imx)









