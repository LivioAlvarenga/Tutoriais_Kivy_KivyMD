from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)  # 1,1,1,1 white


class Aplicativo(App):
    def build(self):  # built é uma função herdada de APP
        button = Button(text='Testando o Botão',
                        size_hint=(0.2, 0.2),
                        font_size='20sp',
                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
                        on_press=self.botao_pressionado,
                        on_release=self.botao_solto)
        return button

    def botao_pressionado(self, obj):
        print('Botão foi pressionado.')

    def botao_solto(self, obj):
        print('Botão foi solto.')


if __name__ == '__main__':
    Aplicativo().run()


# size_hint=(0.5, 0.5) O primeiro é x e o segundo é y. 0.5 é 50%, ou seja:
#  x com 50% da tela
