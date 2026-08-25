lista=[]
lista_negativa=[]
lista_nao_negativa=[]
n=int(input('Digite um número entre 0 a 51 para ser o tamanho da lista:'))
if n<51 and n>0:
    for c in range(1,n+1):
        x=int(input('Digite o termo de número {} da lista'.format(c)))
        lista.append(x)
        if x>=0:
            lista_nao_negativa.append(x)
        else:
            lista_negativa.append(x)
print(lista, lista_negativa, lista_nao_negativa)
