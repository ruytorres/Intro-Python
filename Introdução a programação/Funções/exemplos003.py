def encontrar_maior(x, y):
    if x > y:
        return x
    else:
        return y
x=int(input('Digite um numero: '))
y=int(input('Digite outro numero: '))
print('O maior número é {}'.format(encontrar_maior(x,y)))