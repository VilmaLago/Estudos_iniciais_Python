# Testes iniciais para a utilização de JSON.

import json 

# Leia o nome do usuário.
# Dê uma mensagem de boas-vindas caso ele já esteja no sistema.
# Se não, peça para ele cadastrar seu nome.

filename = 'username.json'
try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("Digite seu nome: ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print("Bem-vindo(a) " + username.title() + "!")
else:
    print("Bem-vindo(a) novamente " + username.title() + "!")