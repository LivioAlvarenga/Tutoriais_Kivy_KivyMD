# 19 - Python Kivy - Criando um Popup
# https://www.youtube.com/watch?v=w0BwoGl18Fk&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=19

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.utils import get_color_from_hex
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.lang import Builder

Builder.load_file('22kivy.kv')


class Gerenciador_de_telas(ScreenManager):
    pass


class Menu(Screen):
    # Esta função será o pop-up perguntando se queremos sair do aplicativo
    def confirmar_saida(self, *args):
        # Boxlayout do popup
        box_popup_sair = BoxLayout(
            orientation='vertical', padding=10, spacing=10)

        # Boxlayout dos botões, obs. não declaramos orientation, pois o padrão
        #  é horizontal
        box_botoes_popup_sair = BoxLayout(padding=10, spacing=10)

        # Declarando o Popup e o content é o Boxlayout que ele faz parte
        popup_sair = Popup(title='Deseja mesmo sair?',
                           content=box_popup_sair,
                           size_hint=(None, None),
                           size=(300, 180))

        # Botão de sim, obs que estamos usando o botão dinamico
        #  App.get_running_app().stop para sair do app
        botao_sim_popup_sair = Botao_dinamico(
            text='Sim', on_release=App.get_running_app().stop)

        # botão de não, obs que estamos usando o botão dinamico
        #  popup_sair.dismiss para sair do popup
        botao_nao_popup_sair = Botao_dinamico(
            text='Não', on_release=popup_sair.dismiss)

        # Adicionando os botões em seu Boxlayout
        box_botoes_popup_sair.add_widget(botao_sim_popup_sair)
        box_botoes_popup_sair.add_widget(botao_nao_popup_sair)

        # Criando o ícone com Image
        atenção_icon = Image(source='Tutoriais_Kivy_KivyMD/Icones/atencao.png')

        # Adicionando o ícone no layout geral
        box_popup_sair.add_widget(atenção_icon)

        # Adicionando o layout dos botões no layout geral
        box_popup_sair.add_widget(box_botoes_popup_sair)

        # Executando o popup
        popup_sair.open()


class Botao_dinamico(ButtonBehavior, Label):
    cor_dinamica_release = ListProperty(get_color_from_hex('#23a3bc'))
    cor_dinamica_press = ListProperty(get_color_from_hex('#7FFF00'))

    def __init__(self, **kwargs):
        super(Botao_dinamico, self).__init__(**kwargs)
        self.atualizar_canvas()

    def on_pos(self, *args):
        self.atualizar_canvas()

    def on_size(self, *args):
        self.atualizar_canvas()

    def on_press(self, *args):
        self.cor_dinamica_release = self.cor_dinamica_press
        self.cor_dinamica_press = self.cor_dinamica_release
        self.atualizar_canvas()

    def on_release(self, *args):
        self.cor_dinamica_release = self.cor_dinamica_press
        self.cor_dinamica_press = self.cor_dinamica_release
        self.atualizar_canvas()

    def atualizar_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor_dinamica_release)
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
