from participantes import participantes_ev

def adicionar_participante(codigo, nome, email, preferencias): #Função para verificar se participante já existe
    if codigo in participantes_ev:
        print(f"Participante com código '{codigo}' já existe.") 
        return

    participantes_ev[codigo] = {
        "nome": nome,
        "email": email,
        "preferencias": preferencias
    }
    print(f"Participante '{nome}' adicionado com sucesso!")

