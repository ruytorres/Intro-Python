texto=input('Digite uma frase: ')
textoPadrao=texto.upper()
caracteres=[',','.',':',';','!','?']
for c in caracteres:
    textoPadrao=textoPadrao.replace(c,'')
textoSeparado=textoPadrao.split()

print('A quantidada de palavras existentes no texto é de {}'.format(len(textoSeparado)))
print('A quantidade de palavras distintas no texto é de {}'.format(len(set(textoSeparado))))
