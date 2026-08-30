# Paradigma funcional pureza e composição de funções



def fatorial_iter(n):
    res = 1 
    for i in range(1, n + 1):
         res *= i
    return res


# def fatorial_recursivo(n):
#     if n == 0: return 1
#     else:
#         return n * fatorial_recursivo(n - 1)
    

# print(fatorial_recursivo(10))

print(fatorial_iter(5))