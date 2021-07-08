# https://www.youtube.com/watch?v=NzUTZj31AfM&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=30

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Builder.load_file('codemy_25_Botoes_Imagens.kv')


class MyLayout(Widget):
    def botão_on(self):
        self.ids.my_label.text = 'Você pressionou o botão!'
        self.ids.my_image.source = 'Tutorial_Kivy_Codemy/icones/user_on.png'

    def botão_off(self):
        self.ids.my_label.text = 'Pressione o botão!'
        self.ids.my_image.source = 'Tutorial_Kivy_Codemy/icones/user_off.png'


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#FFB74D')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
