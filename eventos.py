from eventos_dados import eventos_tech
def criar_evento(nome, data, tema):
    event = {
        "nome": nome,
        "data": data,
        "tema": tema,
        "participantes": []
    }
    eventos_tech.append(event)

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
print(eventos_tech)