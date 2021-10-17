# Testes iniciais para aprender a criar e abrir pastas em modos diferentes.

filename = 'teste_write_mode.txt'
with open(filename, 'w') as file_object:
    file_object.write("Hello world!\n")
    file_object.write("My name's Vilma!\n")

with open(filename, "a") as file_object:
    file_object.write("I am learning how to programm with Python.\n")
    file_object.write("And I am loving it.\n")