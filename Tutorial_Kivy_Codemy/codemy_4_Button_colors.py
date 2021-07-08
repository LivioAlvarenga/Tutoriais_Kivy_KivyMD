# https://www.youtube.com/watch?v=2IuAQ1HUpU4&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=7

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('codemy_4_Button_colors.kv')


class MyGridLayout(Widget):

    # None para quando iniciar esta variavel não ter nada.
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        nome = self.name.text
        pizza = self.pizza.text
        cor = self.color.text

        print(
            f'Olá {nome}, sua pizza favorita é {pizza} e sua cor favorita \
é {cor}')

        # limpar input boxes
        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
