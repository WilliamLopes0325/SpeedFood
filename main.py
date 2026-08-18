import random
from produtos import exibir_cardapio, obter_produto
from pedidos import adicionar_item, visualizar_carrinho, calcular_total, limpar_carrinho, listar_itens, remover_item
from clientes import cadastrar_cliente
from datetime import datetime

data_hora = datetime.now()

while True:

    print("\n" + "=" * 40)
    print("🍔 SPEEDFOOD")
    print("=" * 40)

    print("1 - Ver Cardápio")
    print("2 - Adicionar Produto")
    print("3 - Ver Carrinho")
    print("4 - Remover Produto")
    print("5 - Finalizar Pedido")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        exibir_cardapio()

    elif opcao == "2":

     while True:

        exibir_cardapio()

        try:
            codigo = int(
                input("\nDigite o código do produto: ")
            )

            produto = obter_produto(codigo)

            if produto:
                adicionar_item(produto)
            else:
                print("\n❌ Produto não encontrado.")
                continue

            while True:

                continuar = input(
                    "\nAdicionar outro produto? (S/N): "
                ).upper()

                if continuar in ["S", "N"]:
                    break

                print("\n❌ Digite apenas S ou N.")

            if continuar == "N":
                break

        except ValueError:
            print("\n❌ Digite apenas números.")

    elif opcao == "3":
        visualizar_carrinho()

    elif opcao == "4":

        itens = listar_itens()

        if not itens:
            print("\n🛒 Carrinho vazio.")
            continue

        print("\nItens do carrinho:")

        for i, item in enumerate(itens):
            print(f"{i + 1} - {item['nome']}")

        try:

            indice = int(
                input(
                    "\nDigite o número do item para remover: "
                )
            ) - 1

            remover_item(indice)

        except ValueError:
            print("\n❌ Digite apenas números.")

    elif opcao == "5":

        total = calcular_total()

        if total == 0:
            print("\n🛒 Carrinho vazio.")
            continue

        print("\n" + "=" * 40)
        print("📋 FINALIZAR PEDIDO")
        print("=" * 40)

        cliente = cadastrar_cliente()

        data_hora = datetime.now()
        numero_pedido = random.randint(1000, 9999)

        print("\nForma de Pagamento")
        print("1 - PIX")
        print("2 - Cartão")
        print("3 - Dinheiro")

        pagamento = input("Escolha uma opção: ")

        formas_pagamento = {
            "1": "PIX",
            "2": "Cartão",
            "3": "Dinheiro"
        }

        forma_escolhida = formas_pagamento.get(
            pagamento,
            "Não informada"
        )

        print("\n" + "=" * 40)
        print("✅ PEDIDO FINALIZADO")
        print("=" * 40)

        print(f"Pedido Nº: {numero_pedido}")
        print(f"Data: {data_hora.strftime('%d/%m/%Y %H:%M')}")

        print(f"Cliente: {cliente['nome']}")
        print(f"Telefone: {cliente['telefone']}")
        print(f"Endereço: {cliente['endereco']}")

        print(
            f"\nQuantidade de itens: "
            f"{len(listar_itens())}"
        )

        print("\nItens do Pedido:")

        contagem = {}

        for item in listar_itens():

            nome = item["nome"]

            if nome not in contagem:
               contagem[nome] = {
                   "quantidade":0,
                   "preco": item["preco"]
               }
            
               contagem[nome]["quantidade"] += 1

        for nome, dados in contagem.items():

            subtotal = (
                dados["quantidade"] * 
                dados["preco"]
            )

            print(
                f"-{dados['quantidade']}x "
                f"{nome}"
                f"(R$ {subtotal:.2f})".replace("." , ",")
            )

        print(f"Pagamento: {forma_escolhida}")
        print(f"(Total: R$ {total:.2f})".replace("." , ","))

        print("\n🚚 Pedido enviado com sucesso!")

        limpar_carrinho()

    elif opcao == "6":

        if len(listar_itens()) > 0:
            print("\n❌ Pedido cancelado.")
            limpar_carrinho()

        print("\n👋 Obrigado por utilizar o SpeedFood!")
        break

    else:
        print("\n❌ Opção inválida.")