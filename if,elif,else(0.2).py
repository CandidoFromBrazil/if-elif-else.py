""""Gasto de energia elétrica"""
instalacao = int(input('Qual o tipo de instalação? (1) = Residencial, (2) = comercial, (3) = industrial: '))
Kwh = float(input('Quantos Kwh são consumidos: '))
preco = 0
if (instalacao == 1):
    if(Kwh < 500):
        preco = 0.40
    else :
        preco = 0.65
if (instalacao == 2):
    if (Kwh < 1000):
        preco = 0.55
    else:
        preco = 0.60
if (instalacao == 3):
    if (Kwh < 5000):
        preco = 0.55
    else:
        preco = 0.60
consumo_hora = (Kwh * preco)
print(f'O valor pago por hora pelo consumo de: {Kwh}Kwh, é de: R${consumo_hora:4.2f}')