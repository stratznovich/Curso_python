'''
Três amigos jogaram na loteria. Caso eles ganhem, 
o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. 
Faça um programa que leia quanto cada apostador investiu, 
o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.
'''

premio = 65000000.00

aposta1 = float(input('insira o valor da aposta: '))
aposta2 = float(input('insira o valor da aposta: '))
aposta3 = float(input('insira o valor da aposta: '))
soma1 = aposta1 * (premio / 100)
soma2 = aposta2 * (premio / 100)
soma3 = aposta3 * (premio / 100)
print(premio)
print(f'resultado aposta 1: {soma1}')
print(f'resultado aposta 2: {soma2}')
print(f'resultado aposta 3: {soma3}')
