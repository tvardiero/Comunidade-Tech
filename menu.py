from eventos import eventos
from participantes import participantes
from datetime import datetime


# ---------- Funções Existentes Mantidas ----------

def encontrar_participante_por_codigo(codigo):
    return next((p for p in participantes if p["codigo"] == codigo), None)

def listar_eventos():
    for e in eventos:
        print(f"\nEvento: {e['nome']}")
        print(f"  Data: {e['data']}")
        print(f"  Tema: {e['tema']}")
        print(f"  Participantes: {len(set(e['participantes']))}")

def listar_participantes_evento(nome_evento):
    evento = next((e for e in eventos if e["nome"] == nome_evento), None)
    if not evento:
        print("Evento não encontrado.")
        return

    print(f"\nParticipantes do evento: {evento['nome']}")
    for codigo in set(evento["participantes"]):
        p = encontrar_participante_por_codigo(codigo)
        if p:
            print(f" - {p['nome']} ({p['email']})")

# ---------- Novas Funcionalidades ----------

def adicionar_evento():
    nome = input("Nome do evento: ")
    if any(e['nome'] == nome for e in eventos):
        print("Já existe um evento com esse nome.")
        return

    data = input("Data (AAAA-MM-DD): ")
    tema = input("Tema: ")
    eventos.append({
        "nome": nome,
        "data": data,
        "tema": tema,
        "participantes": []
    })
    print("Evento adicionado com sucesso.")

def remover_evento():
    nome = input("Nome do evento a remover: ")
    for i, e in enumerate(eventos):
        if e['nome'] == nome:
            eventos.pop(i)
            print("Evento removido.")
            return
    print("Evento não encontrado.")

def adicionar_participante():
    try:
        codigo = int(input("Código do participante: "))
        if encontrar_participante_por_codigo(codigo):
            print("Já existe um participante com esse código.")
            return
        nome = input("Nome completo: ")
        email = input("Email: ")
        preferencias = input("Preferências (separadas por vírgula): ").split(',')

        participantes.append({
            "codigo": codigo,
            "nome": nome,
            "email": email,
            "preferencias": [p.strip() for p in preferencias]
        })
        print("Participante adicionado.")
    except ValueError:
        print("Código inválido.")

def atualizar_email_participante():
    try:
        codigo = int(input("Código do participante: "))
        participante = encontrar_participante_por_codigo(codigo)
        if participante:
            novo_email = input("Novo e-mail: ")
            participante["email"] = novo_email
            print("E-mail atualizado.")
        else:
            print("Participante não encontrado.")
    except ValueError:
        print("Código inválido.")

def remover_participantes_duplicados():
    for evento in eventos:
        antes = len(evento["participantes"])
        evento["participantes"] = list(set(evento["participantes"]))
        depois = len(evento["participantes"])
        if antes != depois:
            print(f"Removidos {antes - depois} duplicados do evento: {evento['nome']}")

def listar_eventos_com_poucos_participantes():
    print("\nEventos com menos de 2 participantes:")
    for e in eventos:
        if len(set(e["participantes"])) < 2:
            print(f" - {e['nome']} ({len(e['participantes'])} participante(s))")

def buscar_eventos_por_tema_data():
    tema = input("Tema desejado: ").lower()
    data_inicio = input("Data início (AAAA-MM-DD): ")
    data_fim = input("Data fim (AAAA-MM-DD): ")
    print("\nEventos encontrados:")
    for e in eventos:
        if tema in e["tema"].lower():
            try:
                data_evento = datetime.strptime(e["data"], "%Y-%m-%d").date()
                if datetime.strptime(data_inicio, "%Y-%m-%d").date() <= data_evento <= datetime.strptime(data_fim, "%Y-%m-%d").date():
                    print(f" - {e['nome']} em {e['data']} ({e['tema']})")
            except ValueError:
                print("Formato de data inválido.")
                break

# ---------- Menu Expandido ----------

def menu():
    while True:
        print("\n=== Sistema Comunidade Tech ===")
        print("1. Listar eventos")
        print("2. Listar participantes de um evento")
        print("3. Buscar participante por código")
        print("4. Participantes mais ativos")
        print("5. Temas mais frequentes")
        print("6. Adicionar evento")
        print("7. Remover evento")
        print("8. Adicionar participante")
        print("9. Atualizar e-mail de participante")
        print("10. Remover duplicados de participantes")
        print("11. Listar eventos com poucos participantes")
        print("12. Buscar eventos por tema e faixa de datas")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        opcoes = {
            '1': listar_eventos,
            '2': lambda: listar_participantes_evento(input("Nome do evento: ")),
            '3': adicionar_evento,
            '4': remover_evento,
            '5': adicionar_participante,
            '6': atualizar_email_participante,
            '7': remover_participantes_duplicados,
            '8': listar_eventos_com_poucos_participantes,
            '9': buscar_eventos_por_tema_data
        }

        if escolha == '0':
            print("Saindo do sistema...")
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print("Opção inválida!")