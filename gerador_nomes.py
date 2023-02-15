import random
    
def le_arquivos(nomes_arquivo, sobrenomes_arquivo):
    with open(nomes_arquivo, 'r') as f:
        nomes = tuple(f.read().splitlines())
    with open(sobrenomes_arquivo, 'r') as f:
        sobrenomes = tuple(f.read().splitlines())
    
    return nomes, sobrenomes

def gera_nome_aleatorio(nomes, sobrenomes):
    return random.choice(nomes) + ' ' + random.choice(sobrenomes)

def salva_nome_aleatorio(titulo_arquivo, nomes):
    with open(titulo_arquivo, 'w') as f:
        f.write('\n'.join(nomes))

def main():
    print("\n[Seja bem-vindo ao gerador de nomes engraçados!]\n")

    nomes, sobrenomes = le_arquivos('1. Silly Name Generator/lista_de_nomes.txt', 
                                    '1. Silly Name Generator/lista_de_sobrenomes.txt')
    nomes_gerados = []

    while True:
        nome = gera_nome_aleatorio(nomes, sobrenomes)
        nomes_gerados.append(nome)

        print(nome)
        tente_novamente = input("\n[Quer tentar de novo?] Pressione Enter ou n para sair.\n")
        if tente_novamente.lower() == "n":
            break

    salva_nome_aleatorio('nomes_gerados.txt', nomes_gerados)
    print("Nomes aleatórios salvos em 'nomes_gerados.txt'.")

if __name__ == "__main__":
    main()
