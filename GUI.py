import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.animation import Animation
from kivy.graphics import Rotate
from kivy.uix.widget import Widget
from baralho import Baralho
from flashcard import Flashcard

class MenuPrincipal(Screen):
    pass

class SessaoFlashcards(Screen):
    def __init__(self, **kwargs):
        super(SessaoFlashcards, self).__init__(**kwargs)
        self.baralho = Baralho()

class Configuracoes(Screen):
    baralho = ObjectProperty()

class InserirFlashcard(Screen):
    baralho = ObjectProperty()
    pergunta = ObjectProperty(None)
    resposta = ObjectProperty(None)
    def inserir_pressed(self):
        pergunta = self.ids.pergunta.text
        resposta = self.ids.resposta.text
        self.baralho.inserirFlashcard(pergunta, resposta, 1)

class RemoverFlashcard(Screen):
    baralho = ObjectProperty()
    remover = ObjectProperty(None)
    def on_enter(self):
        flashcards = self.baralho.getFlashcards()
        lista: str = ""
        for i in range(len(flashcards)):
            lista = lista + (str(i)+" Pergunta:"+flashcards[i].getPergunta() + "\n")
        self.ids.display.text = lista
    def remover_pressed(self):
        flashcards = self.baralho.getFlashcards()
        if int(self.ids.remover.text) <= len(flashcards):
            index = int(self.ids.remover.text)
            self.baralho.removerFlashcard(index)

class FinalizarSessao(Screen):
    acertos = StringProperty('')
    baralho = ObjectProperty()
    def __init__(self, **kwargs):
        super(FinalizarSessao, self).__init__(**kwargs)

class Sessao(Screen):
    baralho = ObjectProperty()
    flashcard = None
    def __init__(self, **kwargs):
        super(Sessao, self).__init__(**kwargs)
        self.acertos = 0
        self.flashcard = None

    def on_enter(self):
        self.baralho.resetarMarcadorUtilizado()
        self.flashcard = self.baralho.sortearFlashcard()
        self.ids.flashcard_label.text = "Pergunta: " + self.flashcard.getPergunta()
        self.acertos = 0
            
    def passar_flashcard_pressed(self):
        self.flashcard.setUtilizadoTrue()
        self.flashcard = self.baralho.sortearFlashcard()
        self.atualizar_pergunta(self.flashcard)

    def acertei_pressed(self):
        self.acertos = self.acertos + 1
        self.flashcard.acertou()
        self.flashcard.setUtilizadoTrue()
        self.flashcard.aumentarCaixa()
        self.flashcard = self.baralho.sortearFlashcard()
        self.atualizar_pergunta(self.flashcard)
        self.ids.acertei_button.disabled = True
        self.ids.errei_button.disabled = True
        self.ids.mostrar_resposta_button.disabled = False
        
    def errei_pressed(self):
        self.flashcard.setUtilizadoTrue()
        self.flashcard.diminuirCaixa()
        self.flashcard = self.baralho.sortearFlashcard()
        self.atualizar_pergunta(self.flashcard)
        self.ids.acertei_button.disabled = True
        self.ids.errei_button.disabled = True
        self.ids.mostrar_resposta_button.disabled = False

    def atualizar_pergunta(self, flashcard: Flashcard):
        if flashcard != None:
            self.ids.flashcard_label.text = "Pergunta: " + self.flashcard.getPergunta()
            return

    def check_flashcard(self):
        return self.flashcard

    def animacaoFlashcard(self, widget, *args):
        anim = Animation(angle=180, duration=1.5)
        anim += Animation(angle=360, duration=1.5)
        anim.start(widget)

    def mostrar_resposta_pressed(self):
        self.ids.flashcard_label.text = self.flashcard.getResposta()
        self.ids.mostrar_resposta_button.disabled = True
        self.ids.acertei_button.disabled = False
        self.ids.errei_button.disabled = False

class Aplicacao(App):
    gmanager = None
    finalizarSessao = None
    configuracao = None
    sessao = None
    inserir = None
    remover = None
    def build(self):
        return Builder.load_file('interface.kv')

    def on_start(self):
       self.gmanager = self.root.ids.gmanager
       self.finalizarSessao = self.root.ids.gmanager.get_screen('finalizarSessao')
       self.configuracao = self.root.ids.gmanager.get_screen('configuracoes')
       self.sessao = self.root.ids.gmanager.get_screen('sessao')
       self.inserir = self.root.ids.gmanager.get_screen('inserirFlashcard')
       self.remover = self.root.ids.gmanager.get_screen('removerFlashcard')

    def on_acertos(self, valor):
        self.finalizarSessao.acertos = valor

    def on_baralho_sessao(self, valor):
        self.sessao.baralho = valor

    def on_baralho_configuracao(self, valor):
        self.configuracao.baralho = valor

    def on_baralho_inserir(self, valor):
        self.inserir.baralho = valor

    def on_baralho_remover(self, valor):
        self.remover.baralho = valor

    def atualizarBaralho(self, valor):
        self.sessao.baralho = valor
        self.configuracao.baralho = valor
        self.inserir.baralho = valor
        self.remover.baralho = valor




