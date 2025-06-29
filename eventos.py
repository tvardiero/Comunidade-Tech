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

def add_particip_ev(evento, codigo_participante):
    if codigo_participante not in evento["participantes"]:
        evento["participantes"].append(codigo_participante) 
    

criar_evento("Hackaton ético", "20/10", "Morais e ética na hora de agir")
print(eventos_tech)

add_particip_ev("Redes e sistemas", 55)

