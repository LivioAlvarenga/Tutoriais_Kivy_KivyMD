# 9 - Python Kivy - Múltiplas telas com ScreenManager
# https://www.youtube.com/watch?v=jZ5KehdPf8c&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=9

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('14kivy.kv')

# Criamos aqui um gerenciador de telas, nosso aplicativo tinha somente uma
#  tela, para incluirmos mais telas usamos o ScreenManager


class Gerenciador_de_telas(ScreenManager):
    pass

# Como nosso app terá agora mais de uma tela o Widget geral não mais será
#  BoxLayout e sim um Screen. Como na função build abaixo não vamos mais
#  enviar as tarefas na função def __init__ a variavel tarefas irá gerar um
#  erro, para evitar este erro vamos declara e ela com valor padrão de lista
#  vazia --> tarefas=[]


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

# Ao invés de retornar a lista de tarefas vamos agora retornar a nova class
#  Gerenciador_de_telas()


class HashLDash_Tutorial_App(App):
    def build(self):
        return Gerenciador_de_telas()


if __name__ == '__main__':
    HashLDash_Tutorial_App().run()
