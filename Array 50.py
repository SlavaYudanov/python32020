N = int(input())
a = []
for i in range(N):
  a.append(int(input()))
  n = 0
for i in range(0,N-1) :
  for j in range(i+1,N) :
    if a[i] > a[j] :
      n += 1
print("колл-во инверсий:", n)





