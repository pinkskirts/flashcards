from flashcard import Flashcard
from random import randrange
from random import choice

class Baralho(Flashcard):
    def __init__(self) -> None:
        self.__flashcard: list(Flashcard) = list()
        self.criarBaralhoInicial()

    def inserirFlashcard(self, pergunta, resposta, nivel) -> None:
        self.__flashcard.append(Flashcard(pergunta, resposta, nivel))

    def sortearFlashcard(self) -> Flashcard | None:
        valid_indices: list(Flashcard) = [index for index, flashcard in enumerate(self.__flashcard) if not flashcard.getUtilizado()]
        print(valid_indices)
        if valid_indices:
            i = choice(valid_indices)
            return self.__flashcard[i]
        else:
            return None

    def resetarMarcadorUtilizado(self):
        for i in range(len(self.__flashcard)):
            self.__flashcard[i].setUtilizadoFalse()

    def removerFlashcard(self, indice):
        self.__flashcard.pop(indice)

    def getFlashcards(self):
        return self.__flashcard

    def criarBaralhoInicial(self) -> None: 
       self.__flashcard.append(Flashcard("O que é arquitetura de software?",
                                         "A arquitetura de software é a estrutura fundamental e organização de um sistema de software.",
                                         1))
       self.__flashcard.append(Flashcard("Quais são os principais objetivos da arquitetura de software?",
                                         "Os principais objetivos da arquitetura de software são a escalabilidade, a modularidade e a manutenibilidade do sistema.",
                                         1))
       self.__flashcard.append(Flashcard("Quais são os principais padrões de arquitetura de software?",
                                         "Alguns exemplos de padrões de arquitetura de software são MVC, SOA e arquitetura em camadas.",
                                         1))       
       self.__flashcard.append(Flashcard("O que é uma arquitetura em camadas?",
                                         "A arquitetura em camadas divide o sistema em camadas distintas, cada uma com responsabilidades específicas.",
                                         2))
       self.__flashcard.append(Flashcard("Quais são os benefícios da arquitetura orientada a serviços (SOA)?",
                                         "A arquitetura SOA permite a reutilização de serviços, facilita a integração entre sistemas e promove a flexibilidade e a escalabilidade.",
                                         2))
       self.__flashcard.append(Flashcard("O que são microsserviços?",
                                         "Microsserviços são pequenos componentes independentes que se comunicam entre si para compor um sistema maior.",
                                         2))
       self.__flashcard.append(Flashcard("Qual é a diferença entre arquitetura monolítica e arquitetura em microsserviços?",
                                         "A arquitetura monolítica é um sistema único e coeso, enquanto a arquitetura em microsserviços divide o sistema em componentes independentes.",
                                         2))
       self.__flashcard.append(Flashcard("O que é arquitetura em nuvem?",
                                         "A arquitetura em nuvem é projetada para aproveitar os recursos e serviços disponíveis na computação em nuvem.",
                                         2))
       self.__flashcard.append(Flashcard("Quais são os componentes principais da arquitetura MVC?",
                                         "Os componentes principais da arquitetura MVC são o modelo (model), a visão (view) e o controlador (controller).",
                                         3))
       self.__flashcard.append(Flashcard("Explique a arquitetura de microfrontends.",
                                         "A arquitetura de microfrontends divide a interface do usuário em componentes independentes, permitindo o desenvolvimento e a implantação separados.",
                                         3))
       print(self.__flashcard)
       
