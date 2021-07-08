# 21 - Python Kivy - Criando animações
# https://www.youtube.com/watch?v=P5-Nn4i7hZY&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=21

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
from kivy.lang import Builder

Builder.load_file('24kivy.kv')


class Gerenciador_de_telas(ScreenManager):
    pass


class Menu(Screen):
    def on_pre_enter(self, *args):
        Window.bind(on_request_close=self.confirmar_saida)

    def confirmar_saida(self, *args, **kwargs):
        box_popup_sair = BoxLayout(
            orientation='vertical', padding=10, spacing=10)
        box_botoes_popup_sair = BoxLayout(padding=10, spacing=10)

        # Vamos diminuir o tamanho do pop up de size=(300, 180) para
        #  size=(150, 150) para assim ele poder ter a animação de crescer.
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

        # Criamos uma variavel para armazenar nossa animação. com
        #  Animation(size=(300, 180)) nosso popup ira crescer.
        # Obs para o widget crescer ele deve ter um tamanho menor, então
        #  vamos diminuir o tamanho do popup na variavel popup_sair.
        #  duration=0.2 é a duração da animação e t='out_back' e a transição.
        #  Na documentação do kivy tem vários modelos de transição.
        animacao = Animation(size=(300, 180), duration=0.2, t='out_back')
        # Com comando animacao.start(popup_sair) damos start na animação
        animacao.start(popup_sair)

        # Podemos combinar animações com + ou fazer elas acontecerem ao mesmo
        #  tempo com &, neste exemplo o texto do botão sim inicia rosa e
        #  finaliza azul
        animacao_texto = Animation(color=get_color_from_hex('#FF1493'))
        + Animation(color=get_color_from_hex('#0000FF'))
        animacao_texto.start(botao_sim_popup_sair)
        # Para a animação ficar repetindo constantemente colocamos
        #  animacao_texto.repeat = True
        animacao_texto.repeat = True

        popup_sair.open()
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
