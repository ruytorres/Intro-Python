lista=[]
n=10
for c in range(n):
    x=int(input("Digite o numero de posição {} da lista: ".format(c+1)))
    lista.append(x)
print(lista[::-1])

