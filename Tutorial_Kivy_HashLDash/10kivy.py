# 5 - Python Kivy - Layouts dinâmicos e KWARG!
# https://www.youtube.com/watch?v=CXZWmVU4VIc&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=5

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_file('10kivy.kv')


class Tarefas(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa, font_size=30))


class HashLDash_Tutorial_App(App):
    def build(self):
        return Tarefas(['Fazer compras', 'Buscar filho na escola',
                        'Fazer imposto de renda', 'Enviar email',
                        'Fazer sacolão', 'levar carro na oficina'],
                       orientation='horizontal')


if __name__ == '__main__':
    HashLDash_Tutorial_App().run()
