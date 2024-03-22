cidade = str(input('Digite o nome da cidade pra que verifiquemos se ela começa com a nominação dogmática, ''Santo'': ')).strip()
cidadesplit = cidade.split()
print('Santo' in cidadesplit[0].title(),'que contém o nome dogmático, (Santo) como primeira palavra do nome da cidade.')
