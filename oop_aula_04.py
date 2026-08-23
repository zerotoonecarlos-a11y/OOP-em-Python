def aplicar_operacao(lista, funcao):
    return [funcao(x) for x in lista]


def dobrar(x):
    return x * 2

def inverter(x):
    return -x


nums = [1, 2, 3, 4, 5]

print("Aplicando operação de dobrar:")
resultado_dobrar = aplicar_operacao(nums, dobrar)
print(f"Resultado: {resultado_dobrar}")

print("Aplicando operação de inverter:")
resultado_inverter = aplicar_operacao(nums, inverter)
print(f"Resultado: {resultado_inverter}")