# https://www.youtube.com/watch?v=18bvQW2OHZE&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=25

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Builder.load_file('codemy_16_Sliders.kv')


class MyLayout(Widget):
    def slider_it(self, *args):
        # print(args[1])
        self.slide_text.text = str(int(args[1]))
        self.slide_text.font_size = str(int(args[1]) * 10)


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('37474F')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
