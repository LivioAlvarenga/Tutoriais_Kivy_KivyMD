# 10 - Python Kivy - Criando um menu com imagem
# https://www.youtube.com/watch?v=As24tYzXmEU&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=10

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('15kivy.kv')


class Gerenciador_de_telas(ScreenManager):
    pass


# Criamos esta nova classe para atribuir imagens ao menu
class Menu(Screen):
    pass


class Widget_geral(Screen):
    def __init__(self, tarefas=[], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.scroll_para_colocar_as_tarefas.add_widget(
                Tarefa_mais_botao_remover(text=tarefa))

    def adicionar_nova_tarefa(self):
        nova_tarefa = self.ids.texto_da_tarefa.text
        self.ids.scroll_para_colocar_as_tarefas.add_widget(
            Tarefa_mais_botao_remover(text=nova_tarefa))
        self.ids.texto_da_tarefa.text = ''


class Tarefa_mais_botao_remover(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.descricao_tarefa.text = text


class HashLDash_Tutorial_App(App):
    def build(self):
        return Gerenciador_de_telas()


if __name__ == '__main__':
    HashLDash_Tutorial_App().run()
