# Testes iniciais para a criação de dicionários, uso de flags e loops.

# Crie um dicionário para os sabores preferidos dos respondentes.
sabores_preferidos = {}

# Crie uma flag para ativar o while loop.
# Armazene as respontas dos respondentes.
# Rode o programa enquanto o usuário quiser.
dicionário_ativo = True
while dicionário_ativo:
    nome = input("Nome: ")
    resposta_sabor = input("Sabor preferido de sorvete: ")
    sabores_preferidos[nome] = resposta_sabor

# Verifique se o usuário quer cadastrar mais respostas.
    continuar = input("\nCadastrar sabor preferido de outro usuário? [Sim/Não]: ")
    if continuar.lower() == 'não':
        dicionário_ativo = False

# Após a finalização das respostas...
# Imprima as respostas cadastradas.
for nome, resposta_sabor in sabores_preferidos.items():
    print("\nNome: " + nome.title() + "." +
        "\nSabor preferido: " +
        resposta_sabor.title() + ".")