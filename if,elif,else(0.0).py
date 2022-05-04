""""Escolha de operadores para dois numeros""" #calculadora
numero1 = int(input('Entre com um número inteiro: '))
numero2 = int(input('Entre com um número inteiro: '))
escolha = input('Qual operação você deseja realizar: (multiplicacao, diviso, soma, subtracao): ')
if escolha == 'multiplicacao':
    multiplicacao = (numero1 * numero2)
    print(f'Você optou por: {escolha}')
    print(multiplicacao)
elif escolha == 'divisao':
    divisao = (numero1 / numero2)
    print(f'Você optou por: {escolha}') #retorna <float> por culpa de: '/' <divisao(não inteira)>
    print(divisao)
elif escolha == 'soma':
    soma = (numero1 + numero2)
    print(f'Você optou por: {escolha}')
    print(soma)
elif escolha == 'subtracao':
    subtracao = (numero1 - numero2)
    print(f'Você optou por: {escolha}')
    print(subtracao)

