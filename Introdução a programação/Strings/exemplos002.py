texto=input('Digite uma frase: ')
texto=texto.lower()
palavras_proibidas=['bobo','corno','ferrado']
for c in palavras_proibidas:
    texto=texto.replace(c,'*'*len(c))
print(texto)