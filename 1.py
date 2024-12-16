''' Parte 1: Entendendo o Polimorfismo
1. Explique com suas palavras o que é polimorfismo.
2. Crie duas classes vazias chamadas Pessoa e Objeto.
3. Adicione um método chamado executar() em ambas as classes, mas sem implementar nada dentro
deles.
4. Crie dois objetos, um de cada classe, e chame o método executar() de ambos.
5. Explique o que acontece ao tentar chamar o método executar() sem implementá-lo.'''

# polimorfismo é um conceito fundamental da programação e se refere à capacidade de objetos de diferentes classes responderem de maneiras diferentes à mesma mensagem

class Pessoa:
 pass

class Objeto:
 pass


class Pessoa:
 def executar(self):
 pass

class Objeto:
 def executar(self):
 pass

pessoa = Pessoa()
objeto = Objeto()

pessoa.executar()  
objeto.executar()  

# 5. Explicação
# se você chamar o executar sem implementação é como se ele não existisse na classe

