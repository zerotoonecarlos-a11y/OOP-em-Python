% Fatos
pai(joao, maria).
mae(maria, pedro).

% Regra
avo(X, Y) :-
    pai(X, Z),
    mae(Z, Y).