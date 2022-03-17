class Programa:
    def __init__(
        self, 
        nome, 
        ano, 
        elenco, 
        genero, 
        shortDescription,
        ):
        self.__nome = nome
        self.ano = ano
        self.elenco = elenco
        self.genero = genero
        self.shortDescription = shortDescription
        self.__likes = 0

        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self, nome):
            self.__nome = nome.title()

        def __str__(self):
            return f'{self.__nome} {self.ano} {self.elenco} {self.genero} {self.shortDescription} {self.__like}'

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

    def __str__(self):
        f'{self.__nome} - {self.ano} | {self.duracao} h, {self.genero} {self.__likes} '


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
    
    def __str__(self):
        return f'{self.__nome} T{self.temporadas} - {self.ano} | {self.genero}  {self.__likes}'
