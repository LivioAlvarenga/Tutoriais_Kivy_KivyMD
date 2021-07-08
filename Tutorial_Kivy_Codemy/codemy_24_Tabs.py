# https://www.youtube.com/watch?v=hoEbMTE_k-M&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=34

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file('codemy_24_Tabs.kv')


class MyLayout(TabbedPanel):
    pass


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#FFB74D')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
