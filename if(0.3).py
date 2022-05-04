""""Calculo do imposto de renda"""
salario = float(input('Digite o seu salario: '))
base = salario #troca necessaria para manter a integridade dos valores declarados na variavel salario, anteriormente
imposto = 0
if (base > 3000):
    imposto = imposto + ((base - 3000) * 0.35) #Calculamos 35% do valor superior a 3000
    base = 3000 #atualizaremos o valor de: base pra 3k, pois o que ultrapassa esse valor já foi tarifado
if (base > 1000):
    imposto = imposto + ((base - 1000) * 0.20)
    print(f'Salário: R${salario:6.2f}, imposto a pagar: R${imposto:6.2f}')#Calculamos 20% do valor superior a 1000