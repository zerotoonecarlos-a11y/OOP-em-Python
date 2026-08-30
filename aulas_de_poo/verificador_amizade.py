# Cadastro dos gostos de duas pessoas
carlos = {"filmes", "programação", "jogos", "jiu-jitsu", "pizza"}
ana = {"pizza", "programação", "livros", "filmes", "música"}

def avaliar_amizade(pessoa1, pessoa2):
    # Descobre os gostos em comum
    gostos_em_comum = pessoa1.intersection(pessoa2)

    # Regra da amizade
    if len(gostos_em_comum) >= 3:
        return True, gostos_em_comum
    else:
        return False, gostos_em_comum


amizade, gostos = avaliar_amizade(carlos, ana)

print("Gostos em comum:", gostos)

if amizade:
    print("O sistema diz: Existe potencial de amizade.")
else:
    print("O sistema diz: Poucos gostos em comum.")