# Testes iniciais para aprender sobre funções.

# Defina a função para formatar nomes.
def nome_formatado(primeiro_nome, sobrenome):
    '''Formate o nome da pessoa'''
    nome_completo = primeiro_nome + ' ' + sobrenome
    return nome_completo.title()
# Receba os inputs de nome e sobrenome.
print("Digite seu nome completo: ")
print("Digite 'sair' a qualquer momento para sair.")

while True:
    p_nome = input("Primeiro nome: ")
    if p_nome.lower() == "sair":
        break
    s_nome = input("Sobrenome: ")
    if s_nome.lower() == "sair":
        break
    nome_completo = nome_formatado(p_nome, s_nome)
    print(nome_completo)
