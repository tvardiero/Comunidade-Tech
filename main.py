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
        
        from eventos import listar_eventos
from participantes_dados import listar_participantes_por_evento
from participantes_dados import buscar_participante_por_codigo
from eventos import adicionar_participante_em_evento

def mostrar_menu():
    print("-------------MENU-------------")
    print("1. Listar eventos")
    print("2. Listar participantes de um evento")
    print("3. Buscar participante por código")
    print("4. Inscrever participante em evento")
    print("1. Listar eventos")
    print("2. Listar participantes de um evento")
    print("3. Buscar participante por código")
    print("4. Inscrever participante em evento")
    

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        listar_eventos()
    elif opcao == '2':
        nome = input("Digite o nome do evento: ")
        listar_participantes_por_evento(nome)
    elif opcao == '3':
        codigo = input("Digite o código do participante: ")
        buscar_participante_por_codigo(codigo)
    elif opcao == '4':
        adicionar_participante_em_evento()
    elif opcao == '0':
        print("Encerrando sistema.")
        break
    else:
            print("Opção inválida.")
mostrar_menu()    
