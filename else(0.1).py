""""Calculo de distância x passagem"""
distancia = float(input('Qual a distancia você pretende percorrer em km: '))
passagem = 0
if (distancia <= 200):
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print(f'A distância que você quer percorrer é de: {distancia:.1f}Km, o Valor da passagem vai ficar: R${passagem:.1f}')