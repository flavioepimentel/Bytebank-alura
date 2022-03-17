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
        return f'Nome: {self.nome} Likes: {self.likes}'


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
        return f'{self.nome} - {self.ano} | {self.duracao} h, {self.genero} {self.likes} '


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
        return f'{self.nome} - {self.temporadas}T - {self.ano} | {self.genero} Likes: {self.likes}'

