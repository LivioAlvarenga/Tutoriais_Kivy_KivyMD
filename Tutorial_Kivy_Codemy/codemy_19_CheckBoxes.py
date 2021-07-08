# https://www.youtube.com/watch?v=RpAzki0UJPI&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=28
# https://www.youtube.com/watch?v=X-9l-Sll_gE&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=29

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Builder.load_file('codemy_19_CheckBoxes.kv')


class MyLayout(Widget):
    checks: list = []

    # instance do check box memory address, value true or false.
    def checkbox_click(self, instance, value, sabor):
        print(f'instancia = {instance}\nvalue = {value}\nsabor = {sabor}')
        if value:
            MyLayout.checks.append(sabor)
            sabores = ''
            for sb in MyLayout.checks:
                sabores = f'{sabores} {sb}'

            self.ids.output_label.text = f'Você selecionou o sabor: {sabores}.'
        else:
            MyLayout.checks.remove(sabor)
            sabores = ''
            for sb in MyLayout.checks:
                sabores = f'{sabores} {sb}'

            self.ids.output_label.text = f'Você selecionou o sabor: {sabores}.'


class Codemy_Tutorial_App(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#FFEA00')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
