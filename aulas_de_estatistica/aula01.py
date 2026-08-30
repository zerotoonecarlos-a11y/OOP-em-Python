import numpy as np

dados = np.array([1, 2, 3, 4, 5, 10, 22, 40, 13, 35])

amplitude = np.max(dados) - np.min(dados)

print(f"O valor da amplitude é: {amplitude}")

media = np.mean(dados)

print(f"O valor da media é: {media}")

desvio_medio = np.mean(np.abs(dados - media))

print(f"O valor do desvio médio é: {desvio_medio:.2f}")