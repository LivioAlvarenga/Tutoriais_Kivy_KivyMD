# https://www.youtube.com/watch?v=4-PASskUCW0&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=39

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Builder.load_file('codemy_29_Switch.kv')


class MyLayout(Widget):
    def switch_click(self, switch_Object, switch_Value):
        # print(f'switch_Object = {switch_Object}\nswitch_Value =
        # {switch_Value}')
        if switch_Value:
            self.ids.my_label.text = 'Switch Ligado!'
        else:
            self.ids.my_label.text = 'Switch Desligado!'
            # self.ids.my_switch.disabled = True


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#FFD600')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
