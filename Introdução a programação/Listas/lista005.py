a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão:'))
q = int(input('Digite a quantidade de termos: '))
lista = []
for c in range (1+q+1):
    x = a1 + (c-1)*r
    lista.append(x)
print(lista)







