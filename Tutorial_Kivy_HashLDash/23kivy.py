# 20 - Python Kivy - Confirmação de saída
# https://www.youtube.com/watch?v=sjlw91OStHE&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=20

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

Builder.load_file('23kivy.kv')


class Gerenciador_de_telas(ScreenManager):
    pass


class Menu(Screen):
    # Criamos esta função para integrar outras formas de sair do app ao nosso
    #  pop-up, exe: apertar esc. ou o x de sair. O evento on_pre_enter através
    #  do on_request_close é um evento de Window, ou seja ao sair da tela
    #  chama este evento e ao chamar este evento chamaremos nossa função
    #  confirmar_saida.
    #  Obs: para este método não usamos o unbind como na
    #  class Widget_geral(Screen), pois aqui queremos que este evento propague
    #  em todas as telas, ou seja, seja qual for a tela queremos que chame a
    #  popup de confirmação de saida.
    def on_pre_enter(self, *args):
        Window.bind(on_request_close=self.confirmar_saida)

    def confirmar_saida(self, *args, **kwargs):
        box_popup_sair = BoxLayout(
            orientation='vertical', padding=10, spacing=10)
        box_botoes_popup_sair = BoxLayout(padding=10, spacing=10)

        popup_sair = Popup(title='Deseja mesmo sair?',
                           content=box_popup_sair,
                           size_hint=(None, None),
                           size=(300, 180))

        botao_sim_popup_sair = Botao_dinamico(
            text='Sim', on_release=App.get_running_app().stop)
        botao_nao_popup_sair = Botao_dinamico(
            text='Não', on_release=popup_sair.dismiss)

        box_botoes_popup_sair.add_widget(botao_sim_popup_sair)
        box_botoes_popup_sair.add_widget(botao_nao_popup_sair)

        atenção_icon = Image(source='Tutoriais_Kivy_KivyMD/Icones/atencao.png')

        box_popup_sair.add_widget(atenção_icon)
        box_popup_sair.add_widget(box_botoes_popup_sair)

        popup_sair.open()
        # colocamos este return Trua para finalizar o evento e não deixar o
        #  mesmo propagar, assim podemos usar o popup para fechar.
        return True


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
