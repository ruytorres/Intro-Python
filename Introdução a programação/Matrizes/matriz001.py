#Declarar todos os valores como zero
matriz=[[0 for c in range(4)] for l in range (2)]
soma_coluna=0
produto=1

#Substituir a matriz por valores reais declarados pelo usuário
for l in range(2):
    for c in range(4):
        matriz[l][c] = int(input('Digite o valor [{}][{}]: '.format(l,c)))

        if matriz[l][c]!=0:
            produto = produto * matriz[l][c]
print(produto)
print(matriz)

#Maior da linha, declarar o maior antes de começar o for em C
for l in range(2):
    maior_da_linha= matriz[l][0]
    for c in range(4):
        if matriz[l][c]>maior_da_linha:
            maior_da_linha= matriz[l][c]

    print(maior_da_linha)

#Inverter l com c para poder contar cara valor na soma
for c in range(4):
    soma_da_coluna= matriz[0][0]
    for l in range(2):
        soma_da_coluna+= matriz[l][c]
        media_da_coluna= soma_da_coluna/4

print(media_da_coluna)