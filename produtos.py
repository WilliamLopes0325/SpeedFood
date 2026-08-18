# produtos.py

produtos = {
    1: {"nome": "X-Burguer", "preco": 18.00, "categoria": "Lanche"},
    2: {"nome": "X-Salada", "preco": 20.00, "categoria": "Lanche"},
    3: {"nome": "X-Bacon", "preco": 23.00, "categoria": "Lanche"},
    4: {"nome": "Batata Pequena", "preco": 10.00, "categoria": "Fritas"},
    5: {"nome": "Batata Média", "preco": 15.00, "categoria": "Fritas"},
    6: {"nome": "Batata Grande", "preco": 20.00, "categoria": "Fritas"},
    7: {"nome": "Refrigerante Lata", "preco": 8.00, "categoria": "Bebidas"},
    8: {"nome": "Refrigerante 600ml", "preco": 12.00, "categoria": "Bebidas"},
    9: {"nome": "Água", "preco": 4.00, "categoria": "Bebidas"},
}


def exibir_cardapio():
    print("\n" + "=" * 40)
    print("🍔      SPEEDFOOD - CARDÁPIO")
    print("=" * 40)

    categoria_atual = ""

    for codigo, produto in produtos.items():

        if produto["categoria"] != categoria_atual:
            categoria_atual = produto["categoria"]
            print(f"\n📋 {categoria_atual.upper()}")

        print(
           f"{codigo} - {produto['nome']:<20} R$ {produto['preco']:.2f}"
        )


def obter_produto(codigo):
    return produtos.get(codigo)