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
    baralho = ObjectProperty(None)
    pass

class FinalizarSessao(Screen):
    acertos = StringProperty('')
    def __init__(self, **kwargs):
        super(FinalizarSessao, self).__init__(**kwargs)

class Sessao(Screen):
    def __init__(self, **kwargs):
        super(Sessao, self).__init__(**kwargs)
        self.acertos = 1
        self.baralho = Baralho()
        self.flashcard = self.baralho.sortearFlashcard()

    def on_enter(self):
        self.ids.flashcard_label.text = "Pergunta: " + self.flashcard.getPergunta()
            
    def passar_flashcard_pressed(self):
        self.flashcard.setUtilizadoTrue()
        self.atualizar_pergunta(self.baralho.sortearFlashcard())

    def acertei_pressed(self):
        self.flashcard.acertou()
        self.acertos = self.acertos + 1
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
    def build(self):
        return Builder.load_file('interface.kv')

    def on_start(self):
       self.gmanager = self.root.ids.gmanager
       self.finalizarSessao = self.root.ids.gmanager.get_screen('finalizarSessao')
       self.configuracao = self.root.ids.gmanager.get_screen('configuracoes')
       self.sessao = self.root.ids.gmanager.get_screen('sessao')

    def on_acertos(self, valor):
        self.finalizarSessao.acertos = valor

    def on_baralho(self, valor):
        self.configuracao.baralho = valor

