import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from baralho import Baralho
from flashcard import Flashcard
from kivy.clock import Clock

class MenuPrincipal(Screen):
    pass

class SessaoFlashcards(Screen):
    pass

class Configuracoes(Screen):
    pass

class GerenciadorJanelas(ScreenManager):
    pass

class FinalizarSessao(Screen):
    pass

class Sessao(Screen, Baralho):
    def __init__(self, **kwargs):
        super(Sessao, self).__init__(**kwargs)
        self.question_text = "Novo texto"
    def on_enter(self):
        self.atualizar_pergunta(self.sortearFlashcard())

    def passar_flashcard_pressed(self):
        self.atualizar_pergunta(self.sortearFlashcard())

    def ressoterar_flashcard_pressed(self):
        self.atualizar_pergunta(self.sortearFlashcard())

    def atualizar_pergunta(self, flashcard: Flashcard ):
        if flashcard != None:
            self.ids.question_label.text = flashcard.getPergunta()
            return
        self.finalizar_sessao()

    def finalizar_sessao(self):
        pass

class RespostaFlashcard(Screen):
    pass

class Aplicacao(App, Sessao):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_file('interface.kv')
        return self.root
