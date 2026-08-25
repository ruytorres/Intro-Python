texto=input('Digite uma palavra: ')
texto=texto.lower()
caracteres=[',','.',':',';','!','?']
for c in caracteres:
    texto=texto.replace(c,'')
if texto == texto[::-1]:
    print('A palavra é um palíndromo.')
else:
    print('A palavra não é um palíndromo.')
