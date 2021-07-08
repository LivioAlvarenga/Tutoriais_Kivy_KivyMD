from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)  # 1,1,1,1 white
Window.size = (360, 600)


class Aplicativo(App):
    def build(self):  # built é uma função herdada de APP
        layout = GridLayout(cols=2,
                            row_force_default=True,
                            row_default_height=40)

        button1 = Button(text='Hello 1',
                         size_hint=(None, None),
                         width=100,
                         height=40)

        button2 = Button(text='World 1')

        button3 = Button(text='Hello 2',
                         size_hint=(None, None),
                         width=100,
                         height=40)

        button4 = Button(text='World 2')

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)

        return layout


if __name__ == '__main__':
    Aplicativo().run()
