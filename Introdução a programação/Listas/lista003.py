n=int(input('Digite o tamanho da lista: '))
lista=[]
for c in range (n):
    x = int(input('Digite o {}° termo da lista: '.format(c+1)))
    if x not in lista:
        lista.append(c)
    else:
        print('Valores repetidos não podem ser atribuídos na lista. Tente novamente!')
print('A lista final é {}'.format(lista))
