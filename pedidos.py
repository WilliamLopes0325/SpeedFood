# pedidos.py

carrinho = []


def adicionar_item(produto):
    carrinho.append(produto)
    print(f"\n✅ {produto['nome']} adicionado ao carrinho!")


def visualizar_carrinho():

    if not carrinho:
        print("\n🛒 Carrinho vazio.")
        return

    print("\n" + "=" * 40)
    print("🛒 CARRINHO DE COMPRAS")
    print("=" * 40)

    itens_agrupados = {}

    for item in carrinho:

        nome = item["nome"]
        preco = item["preco"]

        if nome not in itens_agrupados:
            itens_agrupados[nome] = {
                "quantidade": 0,
                "preco": preco
            }

        itens_agrupados[nome]["quantidade"] += 1

    total = 0

    for nome, dados in itens_agrupados.items():

        subtotal = (
            dados["quantidade"] *
            dados["preco"]
        )

        total += subtotal

        print(
            f"{dados['quantidade']}x "
            f"{nome} - "
            f"R$ {subtotal:.2f}"
        )

    print("-" * 40)
    print(f"💰 Total: R$ {total:.2f}")

def remover_item(indice):

    if 0 <= indice < len(carrinho):

        removido = carrinho.pop(indice)

        print(
            f"\n✅ {removido['nome']} removido do carrinho!"
        )

    else:
        print("\n❌ Item inválido.")

def calcular_total():
    total = 0

    for item in carrinho:
        total += item["preco"]

    return total
def limpar_carrinho():
    carrinho.clear()

def listar_itens():
    return carrinho
    