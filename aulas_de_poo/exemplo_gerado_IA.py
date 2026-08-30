# exemplo de codigo ruim gerado por IA

# Dependência externa (variável global)
saldo = 100

def processar_pagamentos(valores):
    global saldo

    total = 0

    # Mutabilidade: altera a lista recebida
    valores.append(999)

    for valor in valores:
        total += valor

    # Dependência externa: altera estado global
    saldo -= total

    # Efeito colateral: imprime na tela
    print(f"Pagamento realizado. Saldo restante: {saldo}")

    return total


# Exemplo corrto de codigo gerado por IA

def somar_lista(numeros):
    soma = 0

    for numero in numeros:
        soma += numero

    return soma


#implemetação de uma função pura que não depende de variáveis externas e não altera o estado global

def calcular_quadrado(numero):
    return numero * numero

