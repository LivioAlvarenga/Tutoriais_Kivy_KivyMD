# 25 - Python Kivy - Efeitos sonoros
# https://www.youtube.com/watch?v=9Vv3a42JE40&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=25

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
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
import json
from kivy.lang import Builder

Builder.load_file('27kivy.kv')


class Gerenciador_de_telas(ScreenManager):
    pass


class Menu(Screen):
    def on_pre_enter(self, *args):
        Window.bind(on_request_close=self.confirmar_saida)

    def confirmar_saida(self, *args, **kwargs):
        # Da o play na poppap_sound como variavel global
        global pop_sound
        pop_sound.play()

        box_popup_sair = BoxLayout(
            orientation='vertical', padding=10, spacing=10)
        box_botoes_popup_sair = BoxLayout(padding=10, spacing=10)

        popup_sair = Popup(title='Deseja mesmo sair?',
                           content=box_popup_sair,
                           size_hint=(None, None),
                           size=(150, 150))

        botao_sim_popup_sair = Botao_dinamico(
            text='Sim', on_release=App.get_running_app().stop)
        botao_nao_popup_sair = Botao_dinamico(
            text='Não', on_release=popup_sair.dismiss)

        box_botoes_popup_sair.add_widget(botao_sim_popup_sair)
        box_botoes_popup_sair.add_widget(botao_nao_popup_sair)

        atenção_icon = Image(source='Tutoriais_Kivy_KivyMD/Icones/atencao.png')

        box_popup_sair.add_widget(atenção_icon)
        box_popup_sair.add_widget(box_botoes_popup_sair)

        animacao = Animation(size=(300, 180), duration=0.2, t='out_back')
        animacao.start(popup_sair)
        animacao_texto = Animation(color=get_color_from_hex(
            '#FF1493')) + Animation(color=get_color_from_hex('#0000FF'))
        animacao_texto.start(botao_sim_popup_sair)
        animacao_texto.repeat = True

        popup_sair.open()
        return True


class Botao_dinamico(ButtonBehavior, Label):
    cor_dinamica_release = ListProperty(get_color_from_hex('#23a3bc'))
    cor_dinamica_press = ListProperty(get_color_from_hex('#7FFF00'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
            Ellipse(size=(self.height, self.height),
                    pos=(self.x + self.width - self.height, self.y))
            Rectangle(size=(self.width - self.height, self.height),
                      pos=(self.x + self.height / 2.0, self.y))


class Widget_geral(Screen):
    tarefas: list = []
    path = ''

    def on_pre_enter(self):
        # Notamos um erro que ao estar em tarefa e apertar o botão volta da
        #  actionbar e retornar a tarefas as mesmas estão duplicando usamos
        #  self.ids.scroll_para_colocar_as_tarefas.clear_widgets() assim
        #  resolvemos o problema.
        self.ids.scroll_para_colocar_as_tarefas.clear_widgets()
        self.path = App.get_running_app().user_data_dir + '/'
        print(f'*********{self.path}')
        self.load_data()
        Window.bind(on_keyboard=self.voltar)
        for tarefa in self.tarefas:
            self.ids.scroll_para_colocar_as_tarefas.add_widget(
                Tarefa_mais_botao_remover(text=tarefa))

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def load_data(self, *args):
        try:
            with open(self.path + 'data.json', 'r') as data:
                self.tarefas = json.load(data)
        except FileNotFoundError:
            pass

    def save_data(self, *args):
        with open(self.path + 'data.json', 'w') as data:
            json.dump(self.tarefas, data)

    def remover_tarefa(self, tarefa):
        # Da o play na poppap_sound como variavel global
        global poppap_sound
        poppap_sound.play()
        tarefa_a_remover = tarefa.ids.descricao_tarefa.text
        self.ids.scroll_para_colocar_as_tarefas.remove_widget(tarefa)
        self.tarefas.remove(tarefa_a_remover)
        self.save_data()

    def adicionar_nova_tarefa(self):
        # Da o play na poppap_sound como variavel global
        global pop_sound
        pop_sound.play()
        nova_tarefa = self.ids.texto_da_tarefa.text
        self.ids.scroll_para_colocar_as_tarefas.add_widget(
            Tarefa_mais_botao_remover(text=nova_tarefa))
        self.ids.texto_da_tarefa.text = ''
        self.tarefas.append(nova_tarefa)
        self.save_data()


class Tarefa_mais_botao_remover(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.descricao_tarefa.text = text


class HashLDash_Tutorial_App(App):
    def build(self):
        return Gerenciador_de_telas()


if __name__ == '__main__':
    # Cria as variaveis de som como global e carregamos nossas variaveis.
    pop_sound = SoundLoader.load('Tutoriais_Kivy_KivyMD/Icones/pop.wav')
    poppap_sound = SoundLoader.load('Tutoriais_Kivy_KivyMD/Icones/poppap.wav')

    HashLDash_Tutorial_App().run()
