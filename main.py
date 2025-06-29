from participantes import participantes_ev
from eventos_dados import eventos_tech
def adicionar_participante_ao_evento(codigo_participante, nome_evento):
    # Verifica se o participante existe
    if codigo_participante not in participantes_ev:
        print(f"Participante {codigo_participante} não encontrado.")
        return

    # Busca o evento e adiciona o participante
    for evento in eventos_tech:
        if evento["nome"] == nome_evento:
            if codigo_participante not in evento["participantes"]:
                evento["participantes"].append(codigo_participante)
                print(f"Participante {codigo_participante} adicionado ao evento '{nome_evento}'.")
            else:
                print(f"Participante {codigo_participante} já está inscrito no evento.")
            return