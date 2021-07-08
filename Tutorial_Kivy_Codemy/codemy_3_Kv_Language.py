# https://www.youtube.com/watch?v=k4QCoS-hj-s&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=5
# https://www.youtube.com/watch?v=dVVPOPuPPc0&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=6

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('codemy_3_Kv_Language.kv')


class MyGridLayout(Widget):

    # None para quando iniciar esta variavel não ter nada.
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f'Hello {name}, sua pizza favorita é {pizza} e sua cor
        #  favorita é {color}')
        # imprimir na tela
        # self.add_widget(Label(text=f'Olá {name}, sua pizza favorita é {pizza}
        #  e sua cor favorita é {color}'))
        print(
            f'Olá {name}, sua pizza favorita é {pizza} e sua cor favorita \
é {color}')

        # limpar input boxes
        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()

'''
Existem três forma de fazer um kv language:
1. crie um arquivo com nome da class App em minusculo sem o app. Ex:
    class MyApp(App): ----> my.kv
    Desta forma ira localizar e usar o arquivo my.kv automatico.

2. crie um arquivo com qualquer nome .kv e chame o mesmo com Builder
    Builder.load_file('codemy_3_Kv_Language_C.kv'). Obs. se estiver
    em outro diretorio é so colocar o caminho

3. a terceira forma é com Builder.load_string
    Builder.load_string(""" coloque o codigo kv aqui!!! """)
'''
