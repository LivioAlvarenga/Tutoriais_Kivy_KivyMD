# 17 - Python Kivy - Customização de widgets pelo Python
# https://www.youtube.com/watch?v=ZVQtCZTBTmc&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=17

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

Builder.load_file('20kivy.kv')


class Gerenciador_de_telas(ScreenManager):
    pass


class Menu(Screen):
    pass


# Criamos aqui uma class Botao_dinamico herdando do ButtonBehavior e Label.
class Botao_dinamico(ButtonBehavior, Label):
    # Definimos o __init__
    def __init__(self, **kwargs):
        # No super aqui colocamos entre parentese o nome da class e o self.
        #  Este é o padrão do python 2
        #  super(Botao_dinamico, self).__init__(**kwargs) =
        #  python2 e super().__init__(**kwargs) é o padrão python 3, como para
        #  compilar usamos o padrão python dois e o mesmo funciona em python
        #  vamos manter desta forma.
        super(Botao_dinamico, self).__init__(**kwargs)
        # agora na inicialização queremos que rodar a função atualizar_canvas()
        self.atualizar_canvas()

    # Para nossa surpresa os desenhos ficam na pos 0,0. O que acontece é que
    #  no kivy ela ja inicia na posição padrão do item pai, aqui teremos que
    #  resolver isco com as funções:

    # Queremos que quando mudar a posição (on_pos) rode nossa função
    #  atualizar_canvas()
    def on_pos(self, *args):
        self.atualizar_canvas()

    # Queremos que quando mudar o tamanho (on_size) rode nossa função
    #  atualizar_canvas()
    def on_size(self, *args):
        self.atualizar_canvas()

    def atualizar_canvas(self, *args):
        # usamos isso que a cada atualização ele deixa rastros de desenho,
        #  coso queira ver é so comentar o cod self.canvas.before.clear()
        self.canvas.before.clear()
        # self.canvas.before para o mesmo ficar antes das propriedades, ou
        #  seja, primeira camada.
        with self.canvas.before:
            # Aqui usamos as mesmas instruções que usamos no .kv a diferença é
            #  que size: no .kv e aqui sinze=
            Color(rgba=get_color_from_hex('#23a3bc'))
            Ellipse(size=(self.height, self.height), pos=(self.pos))
            Ellipse(size=(self.height, self.height), pos=(
                self.x + self.width - self.height, self.y))
            # Usamos 2.0, pois o python para ter um float deve ser dividir por
            #  float e o python três funciona os dois.
            Rectangle(size=(self.width - self.height, self.height),
                      pos=(self.x + self.height / 2.0, self.y))


class Widget_geral(Screen):
    def __init__(self, tarefas=[], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.scroll_para_colocar_as_tarefas.add_widget(
                Tarefa_mais_botao_remover(text=tarefa))

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

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
