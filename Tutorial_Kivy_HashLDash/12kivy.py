# 7 - Python Kivy - Referências e Remoção de Widgets dinamicamente
# https://www.youtube.com/watch?v=WmiKgFBIqkE&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=7

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder

Builder.load_file('12kivy.kv')


class Scroll_para_colocar_as_tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            # apos self referenciamos o id box do arquivo kv (self.ids.box)
            # dentro do box vamos colocar a class Tarefa abaixo e vamos
            #  referencia-lá com (text=tarefa) será necessário criar um
            #  __init__ na class tarefa para referenciar o (text=tarefa)
            # basicamente estamos mandando o tarefa para a classe Tarefa abaixo
            self.ids.scroll_para_colocar_as_tarefas.add_widget(
                Tarefa_mais_botao_remover(text=tarefa))


class Tarefa_mais_botao_remover(BoxLayout):
    # Aqui estamos colocando esta classe dentro da classe
    #  Colocar_tarefas_no_scroll
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        # apos self referenciamos o id label do arquivo kv (self.ids.label)
        #  para o id label passamos um text = text que é a tarefa do for da
        #  class Colocar_tarefas_no_scroll
        self.ids.descricao_tarefa.text = text


class HashLDash_Tutorial_App(App):
    def build(self):
        return Scroll_para_colocar_as_tarefas(['Fazer compras',
                                               'Buscar filho na escola',
                                               'Fazer imposto de renda',
                                               'Enviar email',
                                               'Fazer sacolão',
                                               'levar carro na oficina',
                                               'trocar lâmpada'])


if __name__ == '__main__':
    HashLDash_Tutorial_App().run()
