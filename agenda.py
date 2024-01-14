contatos = []

def mostrar_menu():
    print("\n### Menu ###")
    print("1. Adicionar contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar como favorito")
    print("5. Visualizar lista de contatos favoritos")
    print("6. Apagar contato")
    print("0. Sair")

def adicionar_contato():
    contato = {}
    contato['nome'] = input('Nome do contato: ')
    contato['telefone'] = input('Telefone do contato: ')
    contato['email'] = input('Email do contato: ')
    contato['favorito'] = False
    contatos.append(contato)
    print('Contato adicionado com sucesso.')

def visualizar_contatos():
    print('\nLista de Contatos:')
    for index, contato in enumerate(contatos):
        print(f"{index} - {contato['nome']} ({'Favorito' if contato['favorito'] else 'Não Favorito'})")

def editar_contato():
    visualizar_contatos()
    index = int(input('Digite o índice do contato que deseja editar: '))
    if 0 <= index < len(contatos):
        novo_nome = input('Novo nome: ')
        novo_telefone = input('Novo telefone: ')
        novo_email = input('Novo email: ')
        contatos[index]['nome'] = novo_nome
        contatos[index]['telefone'] = novo_telefone
        contatos[index]['email'] = novo_email
        print('Contato editado com sucesso.')
    else:
        print('Índice inválido.')

def marcar_desmarcar_favorito():
    visualizar_contatos()
    index = int(input('Digite o índice do contato que deseja marcar/desmarcar como favorito: '))
    if 0 <= index < len(contatos):
        contatos[index]['favorito'] = not contatos[index]['favorito']
        print('Contato marcado/desmarcado como favorito.')
    else:
        print('Índice inválido.')

def visualizar_favoritos():
    favoritos = [contato for contato in contatos if contato['favorito']]
    print('\nLista de Contatos Favoritos:')
    for favorito in favoritos:
        print(f"- {favorito['nome']}")

def apagar_contato():
    visualizar_contatos()
    index = int(input('Digite o índice do contato que deseja apagar: '))
    if 0 <= index < len(contatos):
        del contatos[index]
        print('Contato apagado com sucesso.')
    else:
        print('Índice inválido.')

while True:
    mostrar_menu()
    opcao = input('\nEscolha uma opção (0-6): ')

    if opcao == '1':
        adicionar_contato()

    elif opcao == '2':
        visualizar_contatos()

    elif opcao == '3':
        editar_contato()

    elif opcao == '4':
        marcar_desmarcar_favorito()

    elif opcao == '5':
        visualizar_favoritos()

    elif opcao == '6':
        apagar_contato()

    elif opcao == '0':
        print('Saindo do aplicativo. Até logo!')
        break

    else:
        print('Opção inválida. Tente novamente.')
