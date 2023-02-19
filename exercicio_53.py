'''
faça um programa para ler as dimensões de um terreno (comprimento c e largura l), 
bem como o preço do metro de tela p.
Imprima o custo para cercar este mesmo terreno com tela.

'''

preco = 35.64
lagura = int(input('largura "m": '))
comprimento = int(input('comprimento "m": ')) 
soma = lagura * comprimento 
resultado = soma * preco

print(f'valor: ${resultado}')
