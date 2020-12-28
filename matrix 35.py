M = int(input())
N = int(input())#столбик(i)
A = []
MAT = []
k = 0
n = -1

for i in range(0, M):
  for i in range(0, N):
    A.append(int(input()))
    MAT.append(A)
    A = []

for i in range(M):
  print(MAT[i])

for i in range(0, N):
  for j in range(0, M):
    if MAT[j][i] % 2 != 0:
      k = 1
    else:
      k = 0
      break
  if k == 1:
    n = i
    break
    
if n == -1:
  print("таких столбиков нет")
else:
  print(n)







