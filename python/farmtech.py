dados = []

CULTURAS = {
    1: {
        "nome": "Café arábica",
        "figura": "retangulo",
        "insumo_padrao": "Fosfato"
    },
    2: {
        "nome": "Tomate para processamento industrial",
        "figura": "triangulo",
        "insumo_padrao": "Fungicida"
    }
}

def mostrar_menu():
    print("\n" + "-" * 50)
    print("       FARMTECH SOLUTIONS - MENU PRINCIPAL")
    print("-" * 50)
    print("1 - Inserir dados")
    print("2 - Listar dados")
    print("3 - Atualizar dado")
    print("4 - Remover dado")
    print("5 - Calcular área")
    print("6 - Calcular insumos")
    print("7 - Sair")
    print("-" * 50)


def ler_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número.")


def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def escolher_cultura():
    print("\nCulturas disponíveis:")
    for chave, info in CULTURAS.items():
        print(f"{chave} - {info['nome']}")
    opcao = ler_inteiro("Escolha a cultura: ")

    if opcao in CULTURAS:
        return opcao
    else:
        print("Cultura inválida. Usando café arábica por padrão.")
        return 1

def calcular_area_retangulo(base, altura):
    return base * altura


def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


def verificar_indice_valido(indice):
    return 0 <= indice < len(dados)

def cadastrar_dados():
    print("\n" + "-" * 50)
    print("CADASTRO DE DADOS")
    print("-" * 50)

    cultura_escolhida = escolher_cultura()
    cultura_nome = CULTURAS[cultura_escolhida]["nome"]
    figura = CULTURAS[cultura_escolhida]["figura"]
    insumo_padrao = CULTURAS[cultura_escolhida]["insumo_padrao"]

    base = ler_numero("Digite a base da área: ")
    altura = ler_numero("Digite a altura da área: ")

    taxa_aplicacao = ler_numero("Digite a taxa de aplicação do insumo: ")
    medida_insumo = ler_numero("Digite a medida usada no cálculo do insumo: ")

    registro = {
        "cultura": cultura_nome,
        "figura": figura,
        "base": base,
        "altura": altura,
        "area": None,
        "insumo": insumo_padrao,
        "taxa_aplicacao": taxa_aplicacao,
        "medida_insumo": medida_insumo,
        "total_insumo": None
    }

    dados.append(registro)
    print("Cadastro realizado com sucesso.")

def listar_dados():
    print("\n" + "-" * 50)
    print("LISTAGEM DE DADOS")
    print("-" * 50)

    if not dados:
        print("Nenhum dado cadastrado.")
        return

    for i, item in enumerate(dados):
        print(f"\nÍndice: {i}")
        print(f"Cultura: {item['cultura']}")
        print(f"Figura: {item['figura']}")
        print(f"Base: {item['base']}")
        print(f"Altura: {item['altura']}")
        print(f"Área calculada: {item['area']}")
        print(f"Insumo: {item['insumo']}")
        print(f"Taxa de aplicação: {item['taxa_aplicacao']}")
        print(f"Medida do insumo: {item['medida_insumo']}")
        print(f"Total de insumo: {item['total_insumo']}")
        print("-" * 50)

def atualizar_dado():
    print("\n" + "-" * 50)
    print("ATUALIZAR DADO")
    print("-" * 50)

    if not dados:
        print("Não existe nenhum dado para atualizar.")
        return

    listar_dados()
    indice = ler_inteiro("Digite o índice do dado que deseja atualizar: ")

    if not verificar_indice_valido(indice):
        print("Índice inválido.")
        return

    print("\nEscolha a nova cultura:")
    cultura_escolhida = escolher_cultura()
    cultura_nome = CULTURAS[cultura_escolhida]["nome"]
    figura = CULTURAS[cultura_escolhida]["figura"]
    insumo_padrao = CULTURAS[cultura_escolhida]["insumo_padrao"]

    base = ler_numero("Digite a nova base da área: ")
    altura = ler_numero("Digite a nova altura da área: ")
    taxa_aplicacao = ler_numero("Digite a nova taxa de aplicação do insumo: ")
    medida_insumo = ler_numero("Digite a nova medida usada no cálculo do insumo: ")

    dados[indice] = {
        "cultura": cultura_nome,
        "figura": figura,
        "base": base,
        "altura": altura,
        "area": None,
        "insumo": insumo_padrao,
        "taxa_aplicacao": taxa_aplicacao,
        "medida_insumo": medida_insumo,
        "total_insumo": None
    }

    print("Dado atualizado com sucesso.")

def remover_dado():
    print("\n" + "-" * 50)
    print("REMOVER DADO")
    print("-" * 50)

    if not dados:
        print("Não existe nenhum dado para remover.")
        return

    listar_dados()
    indice = ler_inteiro("Digite o índice do dado que deseja remover: ")

    if not verificar_indice_valido(indice):
        print("Índice inválido.")
        return

    removido = dados.pop(indice)
    print(f"Dado removido com sucesso: {removido['cultura']}")

def calcular_area():
    print("\n" + "-" * 50)
    print("CALCULAR ÁREA")
    print("-" * 50)

    if not dados:
        print("Não existe nenhum dado cadastrado.")
        return

    listar_dados()
    indice = ler_inteiro("Digite o índice do dado para calcular a área: ")

    if not verificar_indice_valido(indice):
        print("Índice inválido.")
        return

    item = dados[indice]
    base = item["base"]
    altura = item["altura"]
    figura = item["figura"]

    if figura == "retangulo":
        area = calcular_area_retangulo(base, altura)
    elif figura == "triangulo":
        area = calcular_area_triangulo(base, altura)
    else:
        print("Figura geométrica inválida.")
        return

    item["area"] = area
    print(f"Área calculada com sucesso: {area}")

def calcular_insumo():
    print("\n" + "-" * 50)
    print("CALCULAR INSUMOS")
    print("-" * 50)

    if not dados:
        print("Não existe nenhum dado cadastrado.")
        return

    listar_dados()
    indice = ler_inteiro("Digite o índice do dado para calcular o insumo: ")

    if not verificar_indice_valido(indice):
        print("Índice inválido.")
        return

    item = dados[indice]
    taxa = item["taxa_aplicacao"]
    medida = item["medida_insumo"]

    total = taxa * medida
    item["total_insumo"] = total

    print(f"Insumo calculado com sucesso: {total}")

def executar_programa():
    rodando = True

    while rodando:
        mostrar_menu()
        opcao = ler_inteiro("Escolha uma opção: ")

        if opcao == 1:
            cadastrar_dados()
        elif opcao == 2:
            listar_dados()
        elif opcao == 3:
            atualizar_dado()
        elif opcao == 4:
            remover_dado()
        elif opcao == 5:
            calcular_area()
        elif opcao == 6:
            calcular_insumo()
        elif opcao == 7:
            print("Encerrando o programa...")
            rodando = False
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar_programa()