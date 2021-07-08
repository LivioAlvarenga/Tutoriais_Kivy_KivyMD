# https://www.youtube.com/watch?v=D1Lg3oR_qig&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=37

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Builder.load_file('codemy_27_Barra_Progresso.kv')


class MyLayout(Widget):
    def press_it(self):
        current = self.ids.my_progress_bar.value

        if current == 100:
            current = 0

        current += 5
        self.ids.my_progress_bar.value = current
        self.ids.my_label.text = f'{int(current)}% Progress'


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#FFD600')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
