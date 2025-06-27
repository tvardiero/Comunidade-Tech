from participantes import participantes
from eventos import eventos
contagem = {}
for evento in eventos:
    for p in evento['participantes']:
        contagem[p['codigo']] = contagem.get(p['codigo'], 0) + 1

mais_ativos_ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

# Exibir
for codigo, total in mais_ativos_ordenado:
    p = next(filter(lambda p: p['codigo'] == codigo, participantes), None)
    if p:
        print(f"{p['nome']} participou de {total} evento(s)")

        tema_alvo = "IA"
interessados = list(filter(lambda p: tema_alvo in p['preferencias'], participantes))
for p in interessados:
    print(f"{p['nome']} gosta do tema {tema_alvo}")

from collections import Counter

temas = list(map(lambda e: e["tema"], eventos))
contagem_temas = Counter(temas)

temas_ordenados = sorted(contagem_temas.items(), key=lambda x: x[1], reverse=True)
for tema, qtd in temas_ordenados:
    print(f"Tema: {tema}, Frequência: {qtd}")