# Testes iniciais para aprender sobre classes.

class Cachorro():
    '''Defina atributos comuns para um cachorro.'''

    def __init__(self, nome, idade):
        '''Mostre atributos de nome e idade.'''
        self.nome = nome
        self.idade = idade
        
    def sentar(self):
        '''Mostre que o cachorro sentou.'''
        print(self.nome.title() +
            " sentou!")

    def rolar(self):
        '''Mostre que o cachorro rolou.'''
        print(self.nome.title() +
            " rolou!")

meu_cachorro = Cachorro('ventura', 8)
print("Tenho um cachorro chamado " +
    meu_cachorro.nome.title() +
    " que possui " + str(meu_cachorro.idade) +
    " anos de idade.")

meu_cachorro.sentar()
meu_cachorro.rolar()

seu_cachorro = Cachorro('Aladin', 3)
print("O cachorro da Laura se chama " +
    seu_cachorro.nome.title() +
    " e possui " + str(seu_cachorro.idade) +
    " anos de idade.")
seu_cachorro.rolar()