def IsPower5(K):
  Res = 5
  while Res < K:
    Res = Res * 5
    if Res == K:
      return 'true'
    else:
      return 'false'

print(IsPower5(125))
print(IsPower5(100))








