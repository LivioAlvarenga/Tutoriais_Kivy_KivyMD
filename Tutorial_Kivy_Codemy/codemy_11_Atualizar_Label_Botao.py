# https://www.youtube.com/watch?v=7Sks1Ld1DWY&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=14

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Builder.load_file('codemy_11_Atualizar_Label_Botao.kv')


class MyLayout(Widget):
    def press(self):
        # variaveis para nosso widget
        name = self.ids.name_input.text
        print(name)

        # atualizando label
        self.ids.name_label.text = name

        # limpando o input box
        self.ids.name_input.text = ''


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#916eff')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
