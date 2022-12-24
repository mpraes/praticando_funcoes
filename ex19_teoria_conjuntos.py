conjunto_a = [1,3,5,7,9,11,13,15,17,19,21]
conjunto_b = [2,4,6,7,9,10,12,14,17,18,22]

# com essa função quero encontrar dois valores em pelo menos um dos conjuntos

def valor_em_conjunto(valor1, valor2):
    if valor1 in conjunto_a and valor2 in conjunto_b:
        print(f"Os valores {valor1} e {valor2} foram encontrados em ambos os conjuntos")
    elif valor1 in conjunto_a and valor2 in conjunto_b:
        print(f"O valor {valor1} foi encontrado em ambos os conjuntos, mas o valor {valor2} não")
    elif valor2 in conjunto_a and valor1 in conjunto_b:
        print(f"O valor {valor2} foi encontrado em ambos os conjuntos, mas o valor {valor1} não")
    else:
        print(f"Nenhum dos dois valores foi encontrado em nenhum dos conjuntos. Tente novamente!")


valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))

valor_em_conjunto(valor1,valor2)

