A=[]
B=[]
tamanho=10
for c in range(tamanho):
    a=int(input('Digite o {}° termo da lista A'.format(c+1)))
    A.append(a)
for c in range(tamanho):
    b=int(input('Digite o {}° termo da lista B'.format(c+1)))
    B.append(b)
R = A + B
print('A soma da lista A com a lista B é {}'.format(R))
