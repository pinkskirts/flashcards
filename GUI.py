import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class MenuPrincipal(Screen):
    pass

class SessaoFlashcards(Screen):
    pass

class Configuracoes(Screen):
    pass

class GerenciadorJanelas(ScreenManager):
    pass

kv = Builder.load_file('interface.kv')

class Aplicacao(App):
    def build(self):
        return kv
