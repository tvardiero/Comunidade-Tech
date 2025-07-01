from participantes import participantes_ev
from eventos import eventos_tech

participants_add = []
participants_add.extend(participantes_ev)

def adicionar_participante(codigo, nome, email, preferencias): #Função para verificar se participante já existe
    if codigo in participantes_add:
        print(f"Participante com código '{codigo}' já existe.") 
        return

    participantes_add[codigo] = {
        "nome": nome,
        "email": email,
        "preferencias": preferencias
    }
    print(f"Participante '{nome}' adicionado com sucesso!")

def listar_participantes_por_evento(nome):
    evento = None

    # Busca o evento pelo nome usando for
    for e in eventos_tech:
        if e['nome'] == nome:
            evento = e
            break  # Encerra o loop quando encontrar

    if not evento:
        print(f"Evento '{nome}' não encontrado.")
        return

    
    print(f"\nParticipantes inscritos no evento '{evento['nome']}':")

    if not evento["participantes"]:
        print("Nenhum participante inscrito.")
        return

    for codigo in evento["participantes"]:
        if codigo in participantes_ev:
            participante = participantes_ev[codigo]
            print(f"- {participante['nome']} ({participante['email']})")
        else:
            print(f"- Participante com código {codigo} não encontrado nos dados.")

def buscar_participante_por_codigo(codigo):
    if codigo in participantes_ev:
        participante = participantes_ev[codigo]
        print(f"\n--- Dados do Participante ---")
        print(f"Código: {participante['codigo']}")
        print(f"Nome: {participante['nome']}")
        print(f"E-mail: {participante['email']}")
        print(f"Preferências temáticas: {', '.join(participante['preferencias'])}")
    else:
        print(f"Participante com código '{codigo}' não encontrado.")