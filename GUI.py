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
    pass

class Configuracoes(Screen):
    pass

class GerenciadorJanelas(ScreenManager):
    pass

class FinalizarSessao(Screen):
    acertos = StringProperty('')
    def __init__(self, **kwargs):
        super(FinalizarSessao, self).__init__(**kwargs)

    def on_enter(self):
            print(self.acertos)

class Sessao(Screen, Baralho):
    def __init__(self, **kwargs):
        super(Sessao, self).__init__(**kwargs)
        self.flashcard = self.sortearFlashcard()
        self.acertos = 0

    def on_enter(self):
        self.ids.flashcard_label.text = "Pergunta: " + self.flashcard.getPergunta()
            
    def passar_flashcard_pressed(self):
        self.flashcard.setUtilizadoTrue()
        self.atualizar_pergunta(self.sortearFlashcard())

    def acertei_pressed(self):
        self.flashcard.acertou()
        self.acertos = self.acertos + 1
        self.flashcard.setUtilizadoTrue()
        self.flashcard.aumentarCaixa()
        self.flashcard = self.sortearFlashcard()
        self.atualizar_pergunta(self.flashcard)
        self.ids.acertei_button.disabled = True
        self.ids.errei_button.disabled = True
        self.ids.mostrar_resposta_button.disabled = False
        
    def errei_pressed(self):
        self.flashcard.setUtilizadoTrue()
        self.flashcard.diminuirCaixa()
        self.flashcard = self.sortearFlashcard()
        self.atualizar_pergunta(self.flashcard)
        self.ids.acertei_button.disabled = True
        self.ids.errei_button.disabled = True
        self.ids.mostrar_resposta_button.disabled = False

    def atualizar_pergunta(self, flashcard: Flashcard):
        if flashcard != None:
            self.ids.flashcard_label.text = "Pergunta: " + self.flashcard.getPergunta()
            return
        Aplicacao().on_acertos(str(self.acertos))
        print(self.acertos)

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
    gmanager = GerenciadorJanelas()
    kv = Builder.load_file('interface.kv')
    def build(self):
        return self.kv

    def on_acertos(self, valor):
        finalizarSessao = self.kv.ids.gmanager.get_screen('finalizarSessao')
        finalizarSessao.acertos = valor
