lista1=[]
lista2=[]
n=int(input('Digite o tamanho da lista: '))
for c in range(1,n+1):
    x=int(input('Digite o termo {} da lista: '.format(c)))
    if x not in lista1:
        lista1.append(x)
    else:
        lista2.append(x)
print(lista1)
print(lista2)

