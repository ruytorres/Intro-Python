lista=[]
def primo(num):

 for c in range(2,num):
        if num % c != 0:
            lista.append(num)
            return lista
        else:
            return 'O número não é primo'
