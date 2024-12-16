'''Parte 5: Polimorfismo com Interfaces
21. Crie uma classe abstrata chamada Figura com um método abstrato perimetro().
22. Implemente as classes Quadrado e TrianguloEquilatero que herdam de Figura e implementam o
método perimetro().
23. Crie um objeto de cada classe e chame o método perimetro() para calcular o perímetro.
24. Explique o que acontece se você tentar instanciar a classe Figura.
25. Adicione outra classe chamada Circulo e implemente o método perimetro().'''
#24 Vai causar um erro: TypeError: Can't instantiate abstract class Figura with abstract method perimetro
from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def perimetro(self):
        pass

class Quadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def perimetro(self):
        return 4 * self.lado

class TrianguloEquilatero(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def perimetro(self):
        return 3 * self.lado

class Circulo(Figura):
    def __init__(self, raio):
        self.raio = raio
    
    def perimetro(self):
        return 2 * math.pi * self.raio

quadrado = Quadrado(5)
triangulo = TrianguloEquilatero(6)
circulo = Circulo(7)

print(f"Perímetro do quadrado: {quadrado.perimetro()}")
print(f"Perímetro do triângulo equilátero: {triangulo.perimetro()}")
print(f"Perímetro do círculo: {circulo.perimetro()}")
