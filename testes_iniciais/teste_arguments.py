# Testes iniciais para aprender sobre argumentos.

def pets(animal_nome, animal_tipo = "cachorro"):
    '''Mensagem com tipo de animal e seu nome'''
    print("Eu tenho um " + animal_tipo +
        " chamado " + animal_nome.title() +
        ".")
pets(animal_tipo = "gato", animal_nome = "gigi")

def nome_completo_formatado(primeiro_nome, sobrenome, nome_do_meio = ""):
    '''Escreva nome e sobrenome e formate o nome completo.'''
    if nome_do_meio:
        nome_completo = primeiro_nome + " " + nome_do_meio + " " + sobrenome
    else:
        nome_completo = primeiro_nome + ' ' + sobrenome
    print(nome_completo.title())

pessoa = nome_completo_formatado("vilma", "lago", "terezinha")

def pessoas(primeiro_nome, sobrenome, nome_do_meio = "", idade = ''):
    '''Crie um dicionário com informações das pessoas.'''
    dicionário_pessoas = {
        "primeiro": primeiro_nome,
        "último": sobrenome,

    }
    if nome_do_meio:
        dicionário_pessoas['nome do meio'] = nome_do_meio
    if idade:
        dicionário_pessoas["idade"] = str(idade)
    print (dicionário_pessoas)

pessoa = pessoas("vilma", "lago", "terezinha", 20)