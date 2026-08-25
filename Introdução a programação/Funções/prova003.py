def calcular_concentração(x,y):
    if x != y:
        return ((2*x)+(3*y))/(x-y)
    else:
        return 'Não é possível calcular a concentração.'
x=int(input('Digite a quantidade em ml de X: '))
y=int(input('Digite a quantidade em ml de Y: '))
print(calcular_concentração(x,y))

