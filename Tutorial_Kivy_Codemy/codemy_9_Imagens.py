# https://www.youtube.com/watch?v=LMgLt70kAro&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=12

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Builder.load_file('codemy_9_Imagens.kv')


class MyLayout(Widget):
    pass


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#916eff')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
