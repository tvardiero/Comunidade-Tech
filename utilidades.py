from eventos_dados import eventos_tech
def listar_eventos():
    print("\n=== Lista de Eventos ===")
    for evento in eventos_tech:
        print(f"- {evento['nome']} ({evento['data']}) - Tema: {evento['tema']}")

listar_eventos()