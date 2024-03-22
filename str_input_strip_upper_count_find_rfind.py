frase = str(input('Digite uma frase: ')).upper().strip()
print(frase.count('A'),'vezes aparece a letra (A) na frase elaborada. Aparece a primeira vez na posição', (frase.find('A')+1),' e aparece por último na posição', (frase.rfind('A')+1),'.')
