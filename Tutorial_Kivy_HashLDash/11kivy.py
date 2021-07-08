# 6 - Python Kivy - ScrollView e Size Hints!
# https://www.youtube.com/watch?v=-jM0BKWUKKk&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=6

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder

Builder.load_file('11kivy.kv')


class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            # apos self referenciamos o id box do arquivo kv (self.ids.box)
            # Da mesma maneira vamos desligar o (size_hint_y=None) aqui igual
            #  ao .kv, porem aqui estamos fazendo no Label. Tambem precisamos
            #  especificar uma altura deste label (height=200)
            self.ids.box.add_widget(
                Label(text=tarefa, font_size=30, size_hint_y=None, height=200))


class HashLDash_Tutorial_App(App):
    def build(self):
        return Tarefas(['Fazer compras', 'Buscar filho na escola',
                        'Fazer imposto de renda', 'Enviar email',
                        'Fazer sacolão', 'levar carro na oficina',
                        'trocar lâmpada'])


if __name__ == '__main__':
    HashLDash_Tutorial_App().run()
