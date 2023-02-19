#------------------Leitura de Dados----------------------------------

print('Preencha os campos abaixo com o horário atual')

h = int(input('Hora: '))

m = int(input('Minuto: '))

s = int(input('Segundo: '))

d = int(input('\nDuração do evento (segundos): '))


#----Determinação do Horário de Término do Evento---

s_final = (s + d) % 60

m_final = ( m + (s+d)//60 ) % 60

h_final = ( h + ( m + (s+d)//60 )//60 ) % 24

#----Apresentação do Horário de Término do Evento---

print(f'O fim do evento se dará às {h_final}h {m_final}min e {s_final} segundos')

#-----------------Fim do Programa-------------------------------------