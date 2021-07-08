from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)  # 1,1,1,1 white
Window.size = (360, 600)


class Aplicativo(App):
    def build(self):
        layout = GridLayout(cols=2,
                            row_force_default=True,
                            row_default_height=50,
                            spacing=10,
                            padding=20)

        self.peso = TextInput(text='Escreva seu peso aqui')
        self.altura = TextInput(text='Escreva sua altura aqui')

        button1 = Button(text='Enviar',
                         on_press=self.enviar)

        layout.add_widget(self.peso)
        layout.add_widget(self.altura)
        layout.add_widget(button1)

        return layout

    def enviar(self, obj):
        print(f'peso: {self.peso.text}')
        print(f'altura: {self.altura.text}')


if __name__ == '__main__':
    Aplicativo().run()
