# Testes para aprender sobre classes e herança.

class Carro():
    '''Definindo de maneira simples um carro.'''

    def __init__(self, fabricante, modelo, ano):
        '''Atributos comuns de um carro.'''
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.km_andados = 0

    def quilometragem(self):
        '''Mensagem com quilometragem do carro.'''
        mensagem = ("O carro possui " + str(self.km_andados) + " km andados.")
        print(mensagem)

    def atualizar_quilometragem(self, km_rodados):
        '''
        Modofique a quilometragem de acordo com o valor marcado.
        Faça uma mensagem de aviso caso alguém queira diminuir o valor.'''
        if km_rodados >= self.km_andados:
            self.km_andados = km_rodados
        else:
            print("Você não pode voltar o contador.")

    def incremento_contador(self, incremento):
        '''Adicione à quilometragem cada incremento de km rodado.'''
        self.km_andados += incremento

    def info_carro(self):
        '''Mensagem formatada sobre o carro.'''
        return ("Eu tenho um " +
            self.fabricante.title() +
            " modelo " + self.modelo.title() +
            " ano " + str(self.ano))

class Carro_eletrico(Carro):
    '''Definindo um carro elétrico.'''

    def __init__(self, fabricante, modelo, ano):
        '''Defina o carro elétrico.
        Especifique a potência da bateria.'''
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria()

class Bateria():
    '''Armazenar dados sobre a bateria do carro elétrico.'''

    def __init__(self, tamanho_bateria = 70):
        self.tamanho_bateria = tamanho_bateria

    def potencia_bateria(self):
        '''Escreva a potência da bateria do carro.'''
        mensagem = "A bateria deste carro possui " 
        mensagem += str(self.tamanho_bateria) + " kwh de potência."
        print(mensagem)
    
    def rodagem_carga_cheia(self):
        '''Escreva quantos km rodados por carga cheia da bateria.'''

        if self.tamanho_bateria == 70:
            carga_cheia = 240
        elif self.tamanho_bateria == 80:
            carga_cheia = 270

        mensagem = "Em carga cheia, este carro anda cerca de "
        mensagem += str(carga_cheia) + " km."
        print(mensagem)


meu_carro = Carro("honda", "civic", 2018)
print(meu_carro.info_carro())
meu_carro.atualizar_quilometragem(30)
meu_carro.quilometragem()
meu_carro.incremento_contador(50)
meu_carro.quilometragem()
meu_carro_eletrico = Carro_eletrico("tesla", "modelo s", 2016)
print(meu_carro_eletrico.info_carro())
meu_carro_eletrico.bateria.potencia_bateria()
meu_carro_eletrico.bateria.rodagem_carga_cheia()