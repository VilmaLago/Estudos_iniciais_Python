# Estudos iniciais para aprender sobre testes.

import unittest

def nome_formatado(primeiro_nome, sobrenome, segundo_nome = ""):
    '''Retorne o nome do usuário formatado.'''
    if segundo_nome:
        nome_completo = primeiro_nome + ' ' + segundo_nome + ' ' + sobrenome
    else:
        nome_completo = primeiro_nome + ' ' + sobrenome
    return nome_completo.title()

# Teste a função
class TesteNomeFormatado(unittest.TestCase):
    '''Teste da função nome_formatado'''

    def test_nome_formatado(self):
        '''Nomes com apenas dois elementos funcionam?'''
        nome = nome_formatado("vilma", "lago")
        self.assertEqual(nome, "Vilma Lago")

unittest.main()