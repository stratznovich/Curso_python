"""Implemente um programa que calcule o ano de nascimento
 de uma pessoa a partir de sua idade e do ano atual."""


ano = int(input('ano atual: '))
idade = int(input('idade atual: '))
soma = ano - idade
print(f'resultado: {soma}')
if soma < 1990:
    print('vc esta ficando velhinho meu amigo :)')
else:
    print('ainda vc esta vivendo a beta da vida ')
