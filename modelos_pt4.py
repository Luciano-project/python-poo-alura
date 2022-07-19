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

# Temos necessidade de criar um objeto para representar as playlists
#uma estrura de dados, substituindo nossa lista,
#aqui playlist herdará atributos de listas do 
#python, logo poderá ser manipulado como uma lista
#class Playlist(list):
#    def __init__(self, nome, programas):
#        self.nome = nome
#        super().__init__(programas)
#Vamos reescrever esta função pois herdar a classe
#lista não é uma boa prática.

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self,item):
        return self._programas[item]
    
    
    @property
    def listagem(self):
        return self._programas
        
    @property
    def tamanho(self):
        return len(self._programas)




vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmp = Filme('todo mundo em pânico',1999, 100)
demolidor = Serie('Demolidor',2016,2)

vingadores.dar_likes()
tmp.dar_likes()
tmp.dar_likes()
tmp.dar_likes()
tmp.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

# Vamos implementar uma playlist para os filmes, para isso
#vamos utilizar uma lista como estrutura de dados
filmes_e_series = [vingadores, atlanta, demolidor, tmp]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)


print(f'Tamanho do playlist: {len(playlist_fim_de_semana.listagem)}')



#Aqui podemos checar a iterabilidade de nossa classe)
#print(playlist_fim_de_semana[0]) 
# Aqui estamos aplicando polimorfismo, pois estamos a 
#utilizar um comportamento uniforme para diferentes classes, com diferentes representações
# print(demolidor in playlist_fim_de_semana)
for programas in playlist_fim_de_semana.listagem:
    print(programas)
