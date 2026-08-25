senha = input('Digite a sua senha: ')

maiuscula = False
minuscula = False
tamanho_valido = len(senha) >= 8
lista=[',','.',':',';','!','?']
caractere = False
for c in lista:
    if c in lista:
        caractere = True
for c in senha:
    if c.isupper():
        maiuscula = True
    if c.islower():
        minuscula = True
if maiuscula and minuscula and tamanho_valido and caractere:
    print('Sua senha é válida')
else:
    print('Senha inválida')


