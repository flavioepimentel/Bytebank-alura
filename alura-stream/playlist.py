from videos import Programa


class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

    def addPrograma(self):
        pass