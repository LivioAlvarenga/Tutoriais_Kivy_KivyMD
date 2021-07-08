# https://www.youtube.com/watch?v=NjUV_QxWNEQ&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=24

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.spelling import Spelling

Builder.load_file('codemy_15_Corretor_Ortografico.kv')


class MyLayout(Widget):
    def press(self):
        s = Spelling()
        s.select_language('en_US')

        # verificar quais idiomas existem
        # print(s.list_languages()) NÃO TEM PORTUGUES PRA VARIAR!!!
        word = self.ids.word_input.text
        options = s.suggest(word)
        x = ''
        for item in options:
            x = f'{x} - {item}'

        self.ids.word_label.text = f'{x}'


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('37474F')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
