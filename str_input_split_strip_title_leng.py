nome = str(input('Digite seu nome completo: ')).strip().title()
nomesplit = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nomesplit[0]))
print('Seu último nome é {}'.format(nomesplit[len(nomesplit)-1]))


