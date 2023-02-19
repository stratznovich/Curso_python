valor = float(input('preco do produto:'))
desconto = valor - valor * 0.10
print(f'total a pagar com desconto: {desconto}')
print(f'Parcelas em 3x: {(valor / 3)}')
print(f'comissao a vista: {0.05 * desconto}')
print(f'comissao a prazo: {0.05 * valor}')
