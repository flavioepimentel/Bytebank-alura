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
        self._likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def likes(self):
        return self._likes

    def newLike(self):
        self._likes += 1

    def __str__(self):
        return f'{self.__nome} {self.ano} {self.elenco} {self.genero} {self.shortDescription} {self.likes}'


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

    def __str__(self):
        f'{self.__nome} - {self.ano} | {self.duracao} h, {self.genero} {self.likes} '


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
    
    def __str__(self):
        return f'{self.__nome} T{self.temporadas} - {self.ano} | {self.genero}  {self.likes}'

