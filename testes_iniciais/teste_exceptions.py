# Testes iniciais para aprender sobre exceções.

print("Dê-me dois números e eu irei dividí-los: ")
print("Digite 'sair' sempre que quiser fechar o programa.")

while True:
    primeiro_numero = input("Digite o primeiro número: ")
    if primeiro_numero.lower() == 'sair':
        break
    segundo_numero = input("Digite o segundo número: ")
    if segundo_numero.lower() == 'sair':
        break
    try:
        resposta = int(primeiro_numero)/int(segundo_numero)
    except ZeroDivisionError:
        print("You can't divide by 0.")
    else:
        print(resposta)