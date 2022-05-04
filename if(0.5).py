salario = float(input('Qual o seu saçário: '))
base = salario
aumento = 0
if base > 1250:
    aumento = (base * 0.10)
if base <= 1250:
    aumento = (base * 0.15)
aumento_salarial = salario + aumento
print(f'O salario foi de R${salario:6.2f}, para: R${aumento_salarial:6.2f}, com o aumento de salario de: R${aumento}%')