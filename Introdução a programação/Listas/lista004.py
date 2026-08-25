A=[]
B=[]
An=int(input('Digite o tamanho da lista A:'))
Bn=int(input('Digite o tamanho da lista B:'))
for c in range(An):
    x = int(input('Digite o {}° termo da lista A:'.format(c+1)))
    if x not in A:
        A.append(x)
    else:
        print('Valores duplicados não podem ser atribuídos. Tente novamente até terminar a lista A.')
for c in range(Bn):
    y = int(input('Digite o {}° da lista B:'.format(c+1)))
    if y not in B:
        B.append(y)
    else:
        print('Valores duplicados não podem ser atribuídos. Tente novamente até terminar a lista B')
R = set(A) | set(B)
print(R)
