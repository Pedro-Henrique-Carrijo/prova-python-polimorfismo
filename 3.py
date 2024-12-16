''' Parte 3: Uso de Polimorfismo com Funções
11. Escreva uma função chamada executar_acao(objeto) que chama o método falar() do objeto
recebido.
12. Use a função executar_acao() com um objeto de cada uma das classes Leão, Lobo e Arara.
13. O que acontece se você passar um objeto sem o método falar() para a função?
14. Modifique a função executar_acao() para verificar se o método existe antes de chamá-lo.
15. Adicione uma classe Bicicleta sem o método falar() e teste a função executar_acao() com ela.'''
# 13 acontece AttributeError. 
def executar_acao(objeto):
    if hasattr(objeto, 'falar'):
        objeto.falar()
    else:
        print("Objeto falando")


class Leão:
    def falar(self):
        print("Rugido!")

class Lobo:
    def falar(self):
        print("Uivo!")

class Arara:
    def falar(self):
        print("Bom dia!")

leão = Leão()
lobo = Lobo()
arara = Arara()

executar_acao(leão)
executar_acao(lobo) 
executar_acao(arara)


class Bicicleta:
    pass

bicicleta = Bicicleta()
executar_acao(bicicleta)
