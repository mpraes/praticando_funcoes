conjunto_a = [1,2,3,4,5]
conjunto_b = [1,3,5,6,7]

def valor_em_conjunto(valor):
    if valor in conjunto_a and conjunto_b:
        print(f"O valor {valor} foi encontratdo dentro dos dois conjuntos")
    elif valor in conjunto_a:
        print(f"O valor {valor} está dentro do Conjunto A")
    elif valor in conjunto_b:
        print(f"O valor {valor} está dentro do Conjunto B")
    else:
        print(f"Não tem o valor {valor} em nenhum dos conjuntos. Tente novamente!")

valor_em_conjunto(10)

