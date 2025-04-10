def adicionar_novo_contato(contatos, nome_contato, novo_telefone, novo_email):
    contato = {
        "contato": nome_contato,
        "telefone": novo_telefone,
        "email": novo_email,
        "adicionado": False
    }
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionado com sucesso!")

def ver_contatos(contatos):
    if not contatos:
        print("\nLista de contatos está vazia.")
        return
    
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["adicionado"] else " "
        nome = contato["contato"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. [{status}] {nome}, {telefone}, {email}")
        
def atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["contato"] = novo_nome
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone
        contatos[indice_contato_ajustado]["email"] = novo_email
        print(f"Contato {indice_contato} atualizado para {novo_nome}.")
    else:
        print("Índice de contato inválido.")

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["adicionado"] = True
        print(f"Contato {indice_contato} marcado como favorito.")
    else:
        print("Índice inválido.")

def desfavoritar_contato(contatos, indice_contato):
    for contato in contatos:
        if contato.get("contato") == indice_contato and contato["adicionado"]:
            contato["adicionado"] = False
            print(f"O contato '{indice_contato}' foi desmarcado como favorito.")   
    print(f"Contato '{indice_contato}' não encontrado ou já não estava favoritado.")
    return

def ver_favoritos(contatos):
    favoritos = [c for c in contatos if c["adicionado"]]
    if not favoritos:
        print("\nNenhum contato favoritado.")
        return
    
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(favoritos, start=1):
        nome = contato["contato"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. {nome}, {telefone}, {email}")

def deletar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contato_removido = contatos.pop(indice_contato_ajustado)
        print(f"Contato {contato_removido['contato']} foi removido.")
    else:
        print("Índice de contato inválido.")

# Lista de contatos
contatos = []

while True:
    print("\nLista de contatos:")
    print("1. Adicionar novo contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Desmarcar como favorito")
    print("6. Ver somente contatos favoritos")
    print("7. Deletar contato")
    print("8. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome: ")
        novo_telefone = input("Digite o telefone: ")
        novo_email = input("Digite o email: ")
        adicionar_novo_contato(contatos, nome_contato, novo_telefone, novo_email)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo email do contato: ")
        atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato)

    elif escolha == "5":
        indice_contato = input("Digite o nome do contato que deseja desfavoritar: ")
        desfavoritar_contato(contatos, indice_contato)

    elif escolha == "6":
        ver_favoritos(contatos)

    elif escolha == "7":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja excluir: ")
        deletar_contato(contatos, indice_contato)

    elif escolha == "8":
        print("Programa finalizado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
