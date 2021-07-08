# Tutorial Kivy 002: Melhorando a aparência, personalizando widgets usando as
#  Propriedades Kivy
# http://inclem.net/2019/12/18/kivy/kivy_tutorial_002_improving_appearance/

from kivy.app import App
from kivy.uix.label import Label


class YourApp(App):
    def build(self):
        # root_widget = Label()
        # root_widget.text = 'Hello world!'
        # or
        root_widget = Label(font_size=100, bold=True, markup=True)
        root_widget.text = '[color=#0000CD]Hello[/color] [color=#00FF7F]world!\
[/color]'
        # para colorir um texto deve usar markup=True e separar a propriedade
        #  text e seguir o padrão acima
        # https://www.homehost.com.br/blog/tutoriais/tabela-de-cores-html/
        return root_widget


if __name__ == '__main__':
    YourApp().run()
