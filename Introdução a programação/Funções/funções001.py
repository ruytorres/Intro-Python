def par_ímpar(num):
    if num % 2 == 0:
        return "O número {} é par".format(num)
    else:
        return "O número {} é impar".format(num)
num= int(input('Digite um numero para verificar se ele é par ou ímpar: '))
print(par_ímpar(num))
