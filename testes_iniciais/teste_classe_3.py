# Teste para aprender sobre criação de funções em classes.

class PesquisaAnonima():
    '''Mostre perguntas e recolha as respostas'''

    def __init__(self, questão):
        '''Guarde uma questão, e prepare para guardar respostas.'''
        self.questão = questão
        self.resposta = []

    def mostre_questão(self):
        '''Mostre a questão dada.'''
        print(questão)

    def respostas(self, nova_resposta):
        '''Recolha a resposta e armazene na lista.'''
        self.resposta.append(nova_resposta)

    def mostrar_resultados(self):
        '''Mostre os resultados.'''
        print("Resultados da pesquisa: ")
        for resposta in self.resposta:
            print("- " + resposta.title() + ".")

# Teste classe
# Crie a primeira questão.
questão = "Qual é sua sobremesa preferida? "
minha_pesquisa = PesquisaAnonima(questão)

# Mostre a questão
minha_pesquisa.mostre_questão()
# Recolha as respostas.
# Permita que a pessoa saia da pesquisa se quiser.
print("Digite 'sair' se quiser finalizar.")
while True:
    nova_resposta = input("Resposta: ")
    if nova_resposta.lower() == 'sair':
        break
    else:
        minha_pesquisa.respostas(nova_resposta)

# Mostre os resultados da pesquisa e agradeça:
minha_pesquisa.mostrar_resultados()
print("Obrigado por participar!")