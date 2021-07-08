# https://www.youtube.com/watch?v=e73K1DoTNio&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=9

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('codemy_6_Padronizando_propriedades.kv')


class MyLayout(Widget):
    pass


class Codemy_Tutorial_App(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
