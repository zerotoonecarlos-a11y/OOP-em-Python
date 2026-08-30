# Herança e Polimorfismo 

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        #raise NotImplementedError("Subclasses devem implementar este método.")
        return "Som genérico de animal"


class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"


class Gato(Animal):
    def fazer_som(self):
        return "Miau!"




class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        return "O veículo está se movendo."



class Carro(Veiculo):
    def mover(self):
        return "O carro está dirigindo na estrada."


class Aviao(Veiculo):
    def mover(self):
        return "O avião está voando no céu."


print("Exemplo de Herança e Polimorfismo:\n")

lista_veiculos = [Carro("Toyota", "Corolla"), Aviao("Boeing", "737")]

for veiculo in lista_veiculos:
    print(f"{veiculo.marca} {veiculo.modelo}: {veiculo.mover()}")
    
