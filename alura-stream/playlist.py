from videos import Filmes, Series, Programa


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    def __len__(self):
        return len(self.__programas)

    def __getitem__(self, item):
        return self.__programas[item]        

    def addPrograma(self):
        pass



vingador = Filmes("vingadores - guerra infinita", 2019, "Homem de ferro, Homem aranha", "Aventura", "Um filme de sucesso", 2)
robot = Series("Mr Robot", 2019, "Sr Robot", "Ação", "Sériado de hacker", 5)

robot.newLike()
robot.newLike()
robot.newLike()
robot.newLike()
robot.newLike()
robot.newLike()
robot.newLike()
robot.newLike()
robot.newLike()

vingador.newLike()
vingador.newLike()
vingador.newLike()
vingador.newLike()
vingador.newLike()
vingador.newLike()
vingador.newLike()
vingador.newLike()
vingador.newLike()
vingador.newLike()
vingador.newLike()
vingador.newLike()
vingador.newLike()



lista = [vingador, robot]
playlist = Playlist("nome qualquer", lista)


for programa in playlist:
    print(programa)
print(f'Tamanho {len(playlist)}')