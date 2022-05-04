""""O maior e o menor numero entre tres numeros"""
a = int(input(' Entre com um numero inteiro: '))
b = int(input(' Entre com um numero inteiro: '))
c = int(input(' Entre com um numero inteiro: '))
if a > b > c:
     print(f'{a}') #maior
if b > a > c:
     print(f'{b}')
if c > b > a:
     print(f'{c}')
     if a < b < c: #menor
        print(f'{a}')
     if b < a < c:
        print(f'{b}')
     if c < b < a:
        print(f'{c}')
