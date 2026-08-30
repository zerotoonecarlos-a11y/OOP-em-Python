# idade = int(input("Digite sua idade: "))

# print("Entrada não permitida" if idade < 18 else "Entrada permitida")

# original code
def saudacao(nome):
    print(f"Olá, {nome}!")

nome = input("Digite seu nome: ")
saudacao(nome)
idade = input("Digite sua idade: ")
print("Sua idade é", idade)
if idade.isdigit():
    print("Você digitou um número.")
else:
    print("Você não digitou um número.")
    
    



# refatorado code

def saudacao(nome):
    print(f"Olá, {nome}!")
    
nome = input("Digite seu nome: ")
saudacao(nome)

idade = input("Digite sua idade: ")
    
def verificar_idade(idade): 
    if idade.isdigit():
        print("Sua idade é", idade)
        print("Você digitou um número.")
    else:   
        print("Você não digitou um número.")
    