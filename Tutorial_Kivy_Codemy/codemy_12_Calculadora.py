# https://www.youtube.com/watch?v=Lu-HP4eOYM4&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=15
# https://www.youtube.com/watch?v=pdQ_KZS_GRQ&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=16
# https://www.youtube.com/watch?v=yzcGh1R6Qes&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=17
# https://www.youtube.com/watch?v=AvbcELqNbx0&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=18
# https://www.youtube.com/watch?v=xeXCrZrJazI&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=19

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Builder.load_file('codemy_12_Calculadora.kv')


class MyLayout(Widget):
    def limpar(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        prior = self.ids.calc_input.text

        if prior in 'Error!':
            prior = ''

        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def remover(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def negativar(self):
        prior = self.ids.calc_input.text
        if '-' in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def decimal(self):
        prior = self.ids.calc_input.text
        lista = prior.split('+')
        if '+' in prior and '.' not in lista[-1]:
            self.ids.calc_input.text = f'{prior}.'

        if '.' in prior:
            pass
        else:
            self.ids.calc_input.text = f'{prior}.'

    def sinal_mat(self, sinal):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sinal}'

    def verificar_antes_de_usar_eval(self, iterável):
        situação = True
        for letra in iterável:
            if letra not in '+-*/.':
                try:
                    float(letra)
                except Exception:
                    situação = False
                    break
        if situação:
            return True

    def igual(self):
        prior = self.ids.calc_input.text
        if self.verificar_antes_de_usar_eval(iterável=prior):
            try:
                resultado = eval(prior)
            except Exception:
                resultado = 'Error'
            self.ids.calc_input.text = f'{str(resultado)}'
        else:
            self.ids.calc_input.text = 'Error!'


class Codemy_Tutorial_App(App):

    Window.size = (500, 700)

    def build(self):
        Window.clearcolor = get_color_from_hex('#BBDEFB')
        return MyLayout()


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
