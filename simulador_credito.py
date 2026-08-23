def simular_credito(renda, score, idade):
    
    regra1_atendida = False
    regra2_atendida = False
    regra3_atendida = False
    
    
    if idade < 18:
        return "Não é possível simular crédito para menores de idade."
        regra1_atendida = True
    else:
        return f"A idade não antede a regra de idade mínima, você tem {idade} anos."
        regra1_atendida = False
    
    renda_minima = 2000
    score_minimo = 600
    
    if renda >= renda_minima:
        if score >= score_minimo:
            return "Crédito aprovado!"
            regra2_atendida = True
        else:
            return "Crédito negado devido ao score baixo."
            regra2_atendida = False
    
    if score >= score_minimo:
        return "Crédito negado devido à renda insuficiente."
        regra3_atendida = False
    else:
        return "Crédito negado devido à renda insuficiente e score baixo."
        regra3_atendida = False
    
    if regra1_atendida and regra2_atendida and regra3_atendida:
        return "Todas as regras atendidas. Crédito aprovado!"
    else:
        return "Algumas regras não foram atendidas. Crédito negado."