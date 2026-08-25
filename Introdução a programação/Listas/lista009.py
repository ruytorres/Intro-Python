lista = []
media=0
soma=0
while True:
    x = int(input('Digite um valor: '))
    if x >= 0:
        lista.append(x)
        soma += x
        print('A média móvel é {}'.format(soma/len(lista[-5::])))
    elif x < 0:
        break
print('A média final é {}'.format(soma/len(lista[-5::])))