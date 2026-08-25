matriz= [[0 for c in range(3)] for l in range(3)]
for l in range(3):
    for c in range(3):
        matriz[l][c]=int(input('Digite o valor [{}][{}]'.format(l,c)))
print(matriz)
