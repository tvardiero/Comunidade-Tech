eventos = [
    {
        "nome": "Workshop de IA",
        "data": "2025-07-15",
        "tema": "Inteligência Artificial",
        "participantes": [1, 2]
    },
    {
        "nome": "Hackathon Web",
        "data": "2025-08-01",
        "tema": "Web",
        "participantes": [2, 3]
    },
    {
        "nome": "Workshop de IA",
        "data": "2025-07-15",
        "tema": "Inteligência Artificial",
        "participantes": [1, 2]
    },
    {
        "nome": "Hackathon Web",
        "data": "2025-08-01",
        "tema": "Web",
        "participantes": [2, 3]
    }
]
def criar_evento(nome, data, tema):
    return {
        "nome": nome,
        "data": data,
        "tema": tema,
        "participantes": []
    }

def listar_eventos(eventos):
    for e in eventos:
        print(f"{e['nome']} - {e['data']} - Tema: {e['tema']}")

def adicionar_participante(evento, participante):
    if participante not in evento["participantes"]:
        evento["participantes"].append(participante)

def listar_participantes_do_evento(evento):
    for p in evento["participantes"]:
        print(f"{p['nome']} ({p['codigo']})")

criar_evento("Hackaton ético", "20/10", "Morais e ética na hora de agir")
