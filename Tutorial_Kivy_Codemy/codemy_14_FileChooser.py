# https://www.youtube.com/watch?v=YlRd4rw_vBw&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=23

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Builder.load_file('codemy_14_FileChooser.kv')


class MyLayout(Widget):
    def selected(self, nome_arquivo):
        try:
            self.ids.my_image.source = nome_arquivo[0]
            self.ids.my_label.text = nome_arquivo[0]
            # print(nome_arquivo[0])
        except Exception:
            pass


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('37474F')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
