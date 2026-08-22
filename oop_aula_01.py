import random



class cliente:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        print(f"Olá, meu nome é {self.nome}")




class gerar_pedido:
    def __init__(self, id):
        self.id = id
        
    def gerar_numero_pedido(self):
        return random.randint(1000, 9999)



class produto:
    def __init__(self, nome):
        self.nome = nome
        
    def mostrar_produto(self):
        print(f"Produto: {self.nome}")


class pedido:
    def __init__(self, cliente, produto, gerar_pedido):
        self.cliente = cliente
        self.produto = produto
        self.id_pedido= gerar_pedido

    def mostrar_pedido(self):
        print(f"Pedido do cliente {self.cliente.nome} para o produto {self.produto.nome} com ID {self.id_pedido.gerar_numero_pedido()}")


c = cliente("João")
p = produto("Camiseta")
gerador = gerar_pedido(1)

pedido1 = pedido(c, p, gerador)
pedido1.mostrar_pedido()