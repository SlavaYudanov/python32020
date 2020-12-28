def Fact(N):
  if N > 0:
    return N * Fact(N - 1)
  else:
    return 1

print(Fact(5))







