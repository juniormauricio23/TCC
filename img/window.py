
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.app import App

class ExampleClass(Widget):
    pass



class ExampleApp(App):
    def build(self):
       return ExampleClass()


Window.fullscreen = 'auto'
ExampleApp().run()