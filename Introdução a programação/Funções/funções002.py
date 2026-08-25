def divisivel(A , B):
    if A % B == 0:
        return "1"
    else:
        return "0"
A=int(input('Digite um numero: '))
B=int(input('Digite um numero: '))
print(divisivel(A,B))

