from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import Lista_botoes
import os
from random import *
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from pynput.mouse import Controller

Window.fullscreen = 'fake'#ocultar barra de menu
Window.size = (1024, 768)#tamanho da janela
Window.set_system_cursor("hand")
mouse = Controller()

lista1 = []
#retorna quntidade de arquivos no diretorio
path, dirs, files = next(os.walk("/media/mauricio/BackUp/UFMT/Trabalho_de_Curso/projeto_museu2/animais"))
file_count = len(files)

def NumAleatorio():
    i = 1
    global lista1
    if len(lista1) == file_count:
        lista1 = []
    while i == 1:
        num = randint(1, file_count)
        if num not in lista1:
            lista1.append(num)
            i = 0
        else:
            i = 1
    return num

# Carrega arquivo de configurações da janela do kivy
Config.read("config.ini")

# Cria o Gerenciador de Telas
class Manager(ScreenManager):
    pass

class Menu(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def load_imagens(self):
        lista1 = []
        self.x = NumAleatorio()
        print(self.x)
        self.manager.ids.game.ids.imagem.source = 'animais/' + str(self.x) + '.png'
        self.manager.transition.direction = 'left'
        self.manager.current = 'game'

class Game(Screen):
    def apagar_botao(self):
        self.background_color = 0, 0, 0, 0

    def voltar_menu(self):
        Lista_botoes.lista_botoes(self)
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'

class Curiosidades(Screen):
    def voltar_menu(self):
        Lista_botoes.ListaBotoes(self)
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu2'

    def loadAnimaisCur(self,animal):
        self.manager.ids.curiosidades.ids.imagem1.source = 'animais_curiosidades/' + str(animal) + '.png'
        self.manager.transition.direction = 'left'
        self.manager.current = 'curiosidades'

class Menu2(Screen):
    pass

class MuseuApp(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    MuseuApp().run()