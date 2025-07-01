from eventos_dados import eventos_base
eventos_tech = []

def criar_evento(nome, data, tema):
    event = {
        "nome": nome,
        "data": data,
        "tema": tema,
        "participantes": []
    }
    eventos_add.append(event)

def listar_eventos():
    for e in eventos_tech:
        print(f"{e['nome']} - {e['data']} - Tema: {e['tema']}")

def adicionar_participante_em_evento(eventos, participantes, nome_evento, codigo_participante):
    # Verifica se o participante existe
    if codigo_participante not in participantes:
        print("Participante não encontrado.")
        return

    # Procura o evento na lista
    for evento in eventos:
        if evento["nome"] == nome_evento:
            if codigo_participante in evento["participantes"]:
                print("Participante já está inscrito neste evento.")
            else:
                evento["participantes"].append(codigo_participante)
                print("Participante adicionado com sucesso ao evento.")
            return

    # Se não encontrar o evento
    print("Evento não encontrado.")
    

# criar_evento("Hackaton ético", "20/10", "Ética na hora de agir")
# print(eventos_tech)








