"""Calculando a ma via de acesso rápido com placa de velocidade max 80"""
velocidade = float(input('Qual a velocidade em km/h esta o seu carro agora: '))
print(f'A sua velocidade é: {velocidade}')
if (velocidade > 80.0):
    print('Você foi multado por excesso de velocidade!')
    if (velocidade <= 90.0):
        print('Sua multa é de: R$50.00')
    if (velocidade == 100.0):
        print('Sua multa é de: R$100.00')
    if (velocidade == 110.0):
        print('Sua multa é de: R$150.00')
    if (velocidade == 120.0):
        print('Sua multa é de: R$200.00')