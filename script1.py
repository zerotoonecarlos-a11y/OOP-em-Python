idade = int(input("Digite sua idade: "))

if idade < 18:
    result = 1
else:
    result = 0
    
if(result == 1):
    print("Entrada não permitida")
else:
    print("Entrada permitida")