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
