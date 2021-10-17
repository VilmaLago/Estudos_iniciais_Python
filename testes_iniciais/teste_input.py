# Testes iniciais para aprender sobre inputs.

unconfirmed_user = ['alice', 'john', 'vilma']
confirmed_user = []

# Verificando usuários.
while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    confirmed_user.append(current_user)
    print("Verificando usuários: " +
        current_user + '.')

# Imprima uma lista com os usuários verificados.
for verified_user in confirmed_user:
    print("Usuário verificado: " +
        verified_user + '.')
