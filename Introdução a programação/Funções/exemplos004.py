def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3)/3
n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
n3=int(input('Digite outro numero: '))
if calcular_media(n1,n2,n3) >= 7:
    print('Você ficou com {} de média e está aprovado. Parabéns!'.format(calcular_media(n1,n2,n3)))
else:
    print('Você ficou com {} de média e deverá fazer exame.'.format(calcular_media(n1,n2,n3)))
