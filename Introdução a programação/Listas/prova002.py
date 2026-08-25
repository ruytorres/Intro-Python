lista=[]
negativa=[]
nao_negativa=[]
n=int(input('Digite um número entre 0 e 51 para definir o tamanho da lista:'))
if n > 0 and n < 51:
    for c in range(1,n+1):
        x=int(input('Digite o temor de número {} da lista:'.format(c)))
        if x >= 0:
            lista.append(x)
            nao_negativa.append(x)
        elif x < 0:
            negativa.append(x)
print('A lista negativa é {} e contém {} valores'.format(negativa,len(negativa)))
print('A lista não negativa é {} e contém {} valores'.format(nao_negativa,len(nao_negativa)))


