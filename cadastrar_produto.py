produtos = []

def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$ "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    for produto in produtos:
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Estoque: {produto['quantidade']}")
        print("-" * 20)

while True:
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")