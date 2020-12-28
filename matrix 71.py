M = int(input())
N = int(input())
A = []
MAT = []

for i in range(0, M):
  for i in range(0, N):
    A.append(int(input()))
  MAT.append(A)
  A = []

k = MAT[0][0]
n = 0

for i in range(M):
  print(MAT[i])

for i in range(0, M):
  for j in range(0, N):
    if MAT[i][j] < k:
      k = MAT[i][j]
      n = j

for i in range(0, M):
  MAT[i].append(MAT[i][n])

print(n)
for i in range(M):
  print(MAT[i])






