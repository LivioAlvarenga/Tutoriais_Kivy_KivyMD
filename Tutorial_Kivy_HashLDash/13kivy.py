# 8 - Python Kivy - Adicionando Widgets Dinamicamente e TextInput
# https://www.youtube.com/watch?v=foydYTuk0uQ&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('13kivy.kv')

# Mudamos a tarefa Scroll_para_colocar_as_tarefas de ScrollView para
#  BoxLayout, pois vamos precisar colocar mais widgets nesta tarefa e tambem
#  modificamos o nome para Widget_geral.


class Widget_geral(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.scroll_para_colocar_as_tarefas.add_widget(
                Tarefa_mais_botao_remover(text=tarefa))

    # função para pegar o texto digitado da nova tarefa e colocar mo widget
    #  principal
    def adicionar_nova_tarefa(self):
        # Esta variavel captura (.text) o texto digitado no id texto_da_tarefa
        nova_tarefa = self.ids.texto_da_tarefa.text
        # Aqui repetimos o codigo acima da função __init__, pois este codigo
        #  inclui uma tarefa nova, porem incluímos a variavel nova_tarefa
        #  (text=nova_tarefa)
        self.ids.scroll_para_colocar_as_tarefas.add_widget(
            Tarefa_mais_botao_remover(text=nova_tarefa))
        # Colocamos esta instrução para limpar o local onde digitamos a tarefa
        #  apos a inclusão da mesma assim deixando limpara proxima digitação
        self.ids.texto_da_tarefa.text = ''


class Tarefa_mais_botao_remover(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.descricao_tarefa.text = text


class HashLDash_Tutorial_App(App):
    def build(self):
        return Widget_geral(['Fazer compras', 'Buscar filho na escola',
                            'Fazer imposto de renda', 'Enviar email',
                             'Fazer sacolão', 'levar carro na oficina',
                             'trocar lâmpada'])


if __name__ == '__main__':
    HashLDash_Tutorial_App().run()
