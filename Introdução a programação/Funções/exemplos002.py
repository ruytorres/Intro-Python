def saudar_usuario(nome, turno):
    return 'Boa {}, {}!'.format(turno, nome)
nome=(input('Digite seu nome: '))
turno=(input('Digite seu turno: '))
print(saudar_usuario(nome, turno))