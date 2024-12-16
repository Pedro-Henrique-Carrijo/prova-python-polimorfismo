''' Parte 2: Polimorfismo com Métodos
6. Crie uma classe chamada Leão com um método falar() que imprime "Rugido!".
7. Crie outra classe chamada Lobo com o método falar() que imprime "Uivo!".
8. Crie objetos para ambas as classes e chame o método falar() de cada um.
9. O que acontece quando dois objetos diferentes possuem métodos com o mesmo nome?
10. Implemente uma classe Arara com o método falar() que imprime "Bom dia!" e repita o
processo.'''
# 9 cada método vai ser executado de acordo com a implementação de sua classe.
class Leão:
 def falar(self):
 print("Rugido!")


class Lobo:
 def falar(self):
 print("Uivo!")

leão = Leão()
lobo = Lobo()

leão.falar()
lobo.falar()


class Arara:
 def falar(self):
 print("Bom dia!")

arara = Arara()
arara.falar()
