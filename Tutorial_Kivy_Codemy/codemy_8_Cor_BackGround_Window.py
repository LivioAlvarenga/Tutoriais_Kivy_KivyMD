# https://www.youtube.com/watch?v=KTpYXX1-6yY&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=11

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('codemy_8_Cor_BackGround_Window.kv')


class MyLayout(Widget):
    pass


class Codemy_Tutorial_App(App):
    def build(self):
        # Ou use o Window.clearcolor = get_color_from_hex('#d602ee') aqui
        # Window.clearcolor = get_color_from_hex('#d602ee')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
