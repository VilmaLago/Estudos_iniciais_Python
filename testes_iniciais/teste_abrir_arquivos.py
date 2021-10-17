# Testes iniciais para aprender sobre abertura e leitura de arquivos.

filename = "C:/Users/joaom/Downloads/PYTHON CRASH COURSE/ehmatthes-pcc-f555082/chapter_10/pi_million_digits.txt"
with open(filename) as file_object:
    lista = file_object.readlines()

pi_digits = ''
for line in lista:
    pi_digits += line.strip()

birthdate = input("Escreva a data do seu aniversário ")
birthdate += "com esta formatação [ddmmaa]: "

if birthdate in pi_digits:
    print("Sua data de aniversário se encontra dentro de PI.")
else:
    print("Sua data de aniversário não se encontra em PI.")