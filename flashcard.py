class Flashcard():
    def __init__(self, pergunta, resposta, nivel):
        self.__pergunta = pergunta
        self.__resposta = resposta
        self.__nivel = nivel
        self.__acertos = 0
        self.__caixa = 1
        self.__utilizado = False

    def getPergunta(self):
        return self.__pergunta

    def getResposta(self):
        return self.__resposta

    def getCaixa(self):
        return self.__caixa

    def getAcertos(self):
        return self.__acertos

    def getUtilizado(self):
        return self.__utilizado

    def getNivel(self):
        return self.__nivel

    def setUtilizadoFalse(self):
        self.__utilizado = False
        
    def setUtilizadoTrue(self):
        self.__utilizado = True

    def aumentarCaixa(self):
        self.__caixa = self.__caixa + 1

    def diminuirCaixa(self):
        self.__caixa = self.__caixa - 1

    def acertou(self):
        self.__acertos = self.__acertos + 1

    def getFlashcard(self):
        return print("Pergunta: ", self.__pergunta, "\n",
                     "Resposta: ", self.__resposta, "\n",
                     "Nivel: ", self.__nivel)
