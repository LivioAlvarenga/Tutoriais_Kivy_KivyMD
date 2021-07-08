# https://www.youtube.com/watch?v=Prt_SKkZji8&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=31

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('codemy_21_ScreenManager.kv')


class Primeira_Janela(Screen):
    pass


class Segunda_Janela(Screen):
    pass


class Gerenciador_Janelas(ScreenManager):
    pass


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#FFB74D')
        return Gerenciador_Janelas()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
