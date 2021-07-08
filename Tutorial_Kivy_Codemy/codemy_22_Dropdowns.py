# https://www.youtube.com/watch?v=Wu7kTFZtM6I&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=32

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Builder.load_file('codemy_22_Dropdowns.kv')


class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f'Você escolheu: {value}'


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#FFB74D')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
