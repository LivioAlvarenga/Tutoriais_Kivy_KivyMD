# https://www.youtube.com/watch?v=jOaIL8HiO6U&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=33

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Builder.load_file('codemy_23_Splitters.kv')


class MyLayout(Widget):
    pass


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#FFB74D')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
