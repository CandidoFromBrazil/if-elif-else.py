""""Emprestimo bancario"""

valor_da_casa = float(input('Qual o valor da casa que deseja comprar R$: '))
salario_cliente = float(input('Qual o seu salario mensal R$: '))
meses_para_pagar = int(input('parcelado em quantas vezes R$: '))
prestacao_mensal = (salario_cliente * 0.30)
valor_parcelas = (valor_da_casa // meses_para_pagar)
if (valor_parcelas > salario_cliente):
    print('O imprestimo foi recusado')
else:
    print(f'O valor das prestações será de R$: {valor_parcelas:6.2f}')
