class Filmes:
    def __init__(
        self, 
        nome, 
        ano, 
        duracao, 
        elenco, 
        genero, 
        shortDescription,
        ):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.elenco = elenco
        self.genero = genero
        self.shortDescription = shortDescription
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    def plus_like(self):
        self.likes += 1


class Series:
    def __init__(
        self, 
        nome, 
        ano, 
        elenco, 
        genero, 
        shortDescription,
        temporadas,
        ):
        self.__nome = nome.title()
        self.ano = ano
        self.elenco = elenco
        self.genero = genero
        self.shortDescription = shortDescription
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    def plus_like(self):
        self.likes += 1
