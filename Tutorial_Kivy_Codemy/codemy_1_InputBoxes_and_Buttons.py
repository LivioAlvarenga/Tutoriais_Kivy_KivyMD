# https://www.youtube.com/watch?v=TVnUxyEUVw0&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=3

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        # chamar construtor grid layout
        super().__init__(**kwargs)
        # criar duas colunas
        self.cols = 1

        # criando o segundo gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # adicionar widgets
        self.top_grid.add_widget(Label(text='Name: '))
        # adicionar input box
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text='Favorite Pizza: '))
        # adicionar input box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text='Favorite Color: '))
        # adicionar input box
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        # Adicionando o novo top_grid no nosso app
        self.add_widget(self.top_grid)

        # criar botão submit
        self.submit = Button(text='Submit', font_size=25)
        # bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f'Hello {name}, sua pizza favorita é {pizza} e sua cor
        #  favorita é {color}')
        # imprimir na tela
        self.add_widget(Label(
            text=f'Olá {name}, sua pizza favorita é {pizza} e sua cor favorita \
é {color}'))

        # limpar input boxes
        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
