def cadastrar_cliente():

    while True:

        nome = input("Nome: ").strip()

        if nome.replace(" ", "").isalpha():
            break

        print("\n❌ Digite apenas letras no nome.")

    while True:

        telefone = input("Telefone: ").strip()

        if telefone.isdigit():
            break

        print("\n❌ Digite apenas números no telefone.")

    while True:

        endereco = input("Endereço: ").strip()

        if len(endereco) >= 5:
            break

        print("\n❌ Endereço inválido.")

    return {
        "nome": nome,
        "telefone": telefone,
        "endereco": endereco
    }