max=10
min=2
def intervalo(min,max,x):
    while True:
        x = float(input('Digite um numero: '))
        if x > min and x < max:
            return "O número está dentro do intervalo esperado"

        print('O valor não está no intervalo esperado. Tente novamente.')
print(intervalo(min,max,10))