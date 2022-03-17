class Programa:
    def __init__(
        self, 
        nome, 
        ano, 
        elenco, 
        genero, 
        shortDescription,
        ):
        self.__nome = nome.title()
        self.ano = ano
        self.elenco = elenco
        self.genero = genero
        self.shortDescription = shortDescription
        self.__likes = 0

class Filmes(Programa):
    def __init__(
        self,
        nome, 
        ano, 
        elenco, 
        genero, 
        shortDescription,
        duracao, 
        ):
        super().__init__(nome, ano, elenco, genero, shortDescription)
        self.duracao = duracao

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    def plus_like(self):
        self.likes += 1


class Series(Programa):
    def __init__(
        self,
        nome, 
        ano, 
        elenco, 
        genero, 
        shortDescription,
        temporadas,
        ):
        super().__init__(nome, ano, elenco, genero, shortDescription)
        self.temporadas = temporadas

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    def plus_like(self):
        self.likes += 1
