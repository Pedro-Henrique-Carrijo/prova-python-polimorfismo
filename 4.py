''' Parte 4: Polimorfismo com Herança
16. Crie uma classe base chamada Veiculo com um método mover() vazio (usando pass).
17. Faça as classes Carro, Moto e Caminhão herdarem de Veiculo e sobrescrevam o método
mover().
18. Crie uma lista contendo objetos de cada classe e itere sobre ela chamando o método mover().
19. Explique como a herança facilita a implementação do polimorfismo nesse exemplo.
20. Adicione outra classe chamada Patinete que também herda de Veiculo, mas com um método
mover() que imprime "Patinetes deslizam".'''
# 19 facilita implementação de polimorfismo, permitindo comportamentos específicos.
class Veiculo:
 def mover(self):
    pass


class Carro(Veiculo):
 def mover(self):
    print("Carro em movimento.")

class Moto(Veiculo):
 def mover(self):
    print("Moto em movimento.")

class Caminhão(Veiculo):
 def mover(self):
    print("Caminhão em movimento.")


veículos = [Carro(), Moto(), Caminhão()]
for veiculo in veículos:
 veiculo.mover()

class Patinete(Veiculo):
 def mover(self):
    print("Patinete deslizando.")

patinete = Patinete()
patinete.mover() 
