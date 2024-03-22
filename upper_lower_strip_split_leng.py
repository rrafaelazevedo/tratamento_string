nome = str(input('Digite o nome completo: '))
nomesplit = nome.split()
nomejoin =''.join(nomesplit)
print(' {}, printado no estilo UPPER, (CAIXA ALTA). '
      '\n {}, printado no estilo lower, (caixa baixa).'
      '\n O nome {}, contém {} letras (sem considerar os espaços).'
      '\n O primeiro nome de {} ({}), contém {} letras.'
      '\n'.format(nome.upper(), nome.lower(), nome, len(nomejoin), nome, nomesplit[0], len(nomesplit[0])))