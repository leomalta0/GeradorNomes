import pprint
from collections import defaultdict

entrada_frase = input("Digite uma frase: ")

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

mapeados = defaultdict(list) # Indica que os caracteres vão entrar em um dictionary
for caractere in entrada_frase:
    caractere = caractere.lower() # Indica que os caracteres vão ser analisados em minúsculo
    if caractere in alfabeto:
        mapeados[caractere].append(caractere) # Adiciona o caractere ao dictionary

print("\n" + entrada_frase + "\n")
pprint.pprint(mapeados, width=110)