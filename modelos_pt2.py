#class Filme:
#    def __init__(self, nome, ano, duracao):
#        self.__nome = nome.title()
#        self.ano = ano
#        self.duracao = duracao
#        self.__likes = 0

#    @property
#    def likes(self):
#        return self.__likes

#    def dar_likes(self):
#        self.__likes += 1

#    @property
#    def nome(self):
#        return self.__nome

#    @nome.setter
#    def nome(self, nome):
#        self.__nome = nome

#class Serie:
#    def __init__(self, nome, ano, temporadas):
#        self.__nome = nome.title()
#        self.ano = ano
#        self.temporadas = temporadas
#        self.__likes = 0

#    @property
#    def likes(self):
#        return self.__likes

#    def dar_likes(self):
#        self.__likes += 1

#    @property
#    def nome(self):
#        return self.__nome

#    @nome.setter
#    def nome(self, nome):
#        self.__nome = nome


 #Aqui fazemos a alteração do código, vamos utilizar a herança
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes=0
        
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)

atlanta = Serie('atlanta', 2018, 2)

# Vamos implementar uma playlist para os filmes, para isso
#vamos utilizar uma lista como estrutura de dados
filmes_e_series = [vingadores, atlanta]

# Aqui estamos aplicando polimorfismo, pois estamos a 
#utilizar um comportamento uniforme para diferentes classes, com diferentes representações

for programas in filmes_e_series:
    print(programas)
