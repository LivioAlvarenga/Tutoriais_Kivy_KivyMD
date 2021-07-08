# 18 - Python Kivy - Propriedades e atribuição simultânea
# https://www.youtube.com/watch?v=kDu1HJPruIE&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=18

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.utils import get_color_from_hex
# se formos mudar uma propriedade de lista como cores importamos ListProperty,
#  ser texto --> StringProperty, se numero --> NumericProperty
from kivy.properties import ListProperty
from kivy.lang import Builder

Builder.load_file('21kivy.kv')


class Gerenciador_de_telas(ScreenManager):
    pass


class Menu(Screen):
    pass


class Botao_dinamico(ButtonBehavior, Label):
    # Criamos uma variavel e definimos uma cor padrão para a mesma, lembre que
    #  tambem poderiamos colocar com lista e não usar o formato hex. Ex:
    #  cor_dinamica = ListProperty([0.1,0.5,0.7,1])
    cor_dinamica = ListProperty(get_color_from_hex('#23a3bc'))
    # Esta cor é para quando o botão for pressionado.
    cor_dinamica_pressed = ListProperty(get_color_from_hex('#7FFF00'))

    def __init__(self, **kwargs):
        super(Botao_dinamico, self).__init__(**kwargs)
        self.atualizar_canvas()

    def on_pos(self, *args):
        self.atualizar_canvas()

    def on_size(self, *args):
        self.atualizar_canvas()

    # Esta função serve para ao pressionar o botão use a cor
    #  cor_dinamica_pressed.
    def on_press(self, *args):
        # Aqui podemos trocar as cores a cor que esta em self.cor_dinamica ira
        #  para self.cor_dinamica_pressed e vice-versa.
        self.cor_dinamica = self.cor_dinamica_pressed
        self.cor_dinamica_pressed = self.cor_dinamica
        # Apos trocar a cor atualizamos para modificar
        self.atualizar_canvas()

    # Esta função serve para ao soltar o botão use a cor cor_dinamica.
    def on_release(self, *args):
        self.cor_dinamica = self.cor_dinamica_pressed
        self.cor_dinamica_pressed = self.cor_dinamica
        self.atualizar_canvas()

    def atualizar_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # Aqui colocamos rgba=self.cor_dinamica para definir a variavel e
            #  agora no .kv, chamamos esta variavel e colocamos a cor que
            #  queremos.
            Color(rgba=self.cor_dinamica)
            Ellipse(size=(self.height, self.height), pos=(self.pos))
            Ellipse(size=(self.height, self.height), pos=(
                self.x + self.width - self.height, self.y))
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
