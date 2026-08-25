lista=[]
min=int(input('Digite um valor:'))
max=int(input('Digite o valor máximo:'))
if max > min:
    for c in range(min,max+1):
        if c % 7 ==0:
            lista.append(c)
else:
    print('O valor max deve ser maior que o primeiro valor digitado. Tente novamente.')
print(lista)

'''
Caso o usuário digite um valor max menor que o min, vai acabar o programa. 
Para aperfeiçoar, devemos usar o while true para ele não encerrar!!
'''
