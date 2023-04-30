def ler_numero():
  while True:
        try:
            n = int(input("Insira um número inteiro: "))
            break
            
        except ValueError:
            print("Valor inválido. Tente novamente.")
  return n

def imprime_resultados(n, positivo, par):
    if positivo:
        print(f"{n} é um número positivo.", end=" ")
    else:
        print(f"{n} é um número negativo.", end=" ")
    if par:
        print(f"{n} é um número par.")
    else:
        print(f"{n} é um número ímpar.")

def menu():
    print("Escolha uma opção:")
    print("1 - Verificar se um número é positivo")
    print("2 - Verificar se um número é par")
    print("3 - Verificar se um número é primo")
    print("0 - Sair")
    opcao = input("Opção: ")
    return opcao

    