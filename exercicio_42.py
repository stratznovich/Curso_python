'''Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário 
tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.'''

salario = float(input('insira o salario base:'))
gratificacao = salario + salario * 0.05
print(f'pagamento: {gratificacao - gratificacao * 0.07}')


