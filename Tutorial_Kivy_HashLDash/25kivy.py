# 22 - Python Kivy - Salvando informações e persistência de dados
# https://www.youtube.com/watch?v=6A8igVPUNLc&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=22

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
import json
from kivy.lang import Builder

Builder.load_file('25kivy.kv')


class Gerenciador_de_telas(ScreenManager):
    pass


class Menu(Screen):
    def on_pre_enter(self, *args):
        Window.bind(on_request_close=self.confirmar_saida)

    def confirmar_saida(self, *args, **kwargs):
        box_popup_sair = BoxLayout(
            orientation='vertical', padding=10, spacing=10)
        box_botoes_popup_sair = BoxLayout(padding=10, spacing=10)

        popup_sair = Popup(title='Deseja mesmo sair?',
                           content=box_popup_sair, size_hint=(None, None),
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
    # Vamos remover todo o __init__ e mover o for para o método on_pre_enter.
    # def __init__(self, tarefas=[], **kwargs):
    # super().__init__(**kwargs)

    # Criamos esta variavel pois antes a mesma estava no __init__
    tarefas: list = []
    # Esta variavel foi criada para salvarmos o arquivo com os dados do app,
    #  pois se apagar ou reinstalar o app não perderemos os dados. O arquivo
    #  fica salvo em C:\Users\Avell\AppData\Roaming\kivy25
    path = ''

    def on_pre_enter(self):
        # Esta instrução serve para salvar o arquivo no AppData conforme
        #  explicação na variavel path
        self.path = App.get_running_app().user_data_dir + '/'
        # Antes de entrar temos que chamar a função para ler o arquivo json
        self.load_data()
        Window.bind(on_keyboard=self.voltar)
        # Este for veio do __init__ que desabilitamos e sera chamado antes do
        #  Widget_geral, poi é o metodo on_pre_enter. Modificamos tarefas para
        #  self.tarefas, pois agora tarefas é uma variavel da class
        #  Widget_geral
        for tarefa in self.tarefas:
            self.ids.scroll_para_colocar_as_tarefas.add_widget(
                Tarefa_mais_botao_remover(text=tarefa))

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    # O problema agora é que quando ele entra no app ele não esta lendo o
    #  arquivo json com as tarefas, ou seja, temos que criar um método ao ele
    #  iniciar ler o arquivo.
    def load_data(self, *args):
        try:
            # Vai tentar abrir o arquivo json como leitura e carregar a lista
            #  tarefas. Indicamos o caminho path para buscar o arquivo no
            #  AppData conforme explicação na variavel path.
            with open(self.path + 'data.json', 'r') as data:
                self.tarefas = json.load(data)
        # Se não conseguir abrir é porque não existe nenhuma tarefa, ou seja,
        #  a lista tarefas esta vazia.
        except FileNotFoundError:
            pass

    # Este é o método que ira salvar o arquivo com as tarefas.
    def save_data(self, *args):
        # Abrimos o arquivo data.json para escrita. Salvamos o mesmo no path
        #  para salvar no AppData conforme explicação na variavel path.
        with open(self.path + 'data.json', 'w') as data:
            # Salvamos as tarefas no arquivo data. Obs. temos que import o json
            json.dump(self.tarefas, data)

    # Criamos esta função de remover as tarefas que antes estava no arquivo
    #  kv, pois agora temos que remover as tarefas do arquivo json
    def remover_tarefa(self, tarefa):
        # Criamos a variavel remover_tarefa que vem do ids.descricao_tarefa do
        #  arquivo .kv
        tarefa_a_remover = tarefa.ids.descricao_tarefa.text
        # Aqui eleminamos a tarefa no widget Tarefa_mais_botao_remover
        self.ids.scroll_para_colocar_as_tarefas.remove_widget(tarefa)
        # Aqui removemos a tarefa da lista tarefas
        self.tarefas.remove(tarefa_a_remover)
        # Apos fazer os ajustes salvamos o arquivo json
        self.save_data()

    def adicionar_nova_tarefa(self):
        nova_tarefa = self.ids.texto_da_tarefa.text
        self.ids.scroll_para_colocar_as_tarefas.add_widget(
            Tarefa_mais_botao_remover(text=nova_tarefa))
        self.ids.texto_da_tarefa.text = ''
        # Aqui colocamos a lista tarefas para receber a nova_tarefa
        self.tarefas.append(nova_tarefa)
        # Chamamos um metodo novo para salvar o arquivo save_data()
        self.save_data()


class Tarefa_mais_botao_remover(BoxLayout):
    def __init__(self, text='', **kwargs):
        super(Tarefa_mais_botao_remover, self).__init__(**kwargs)
        self.ids.descricao_tarefa.text = text


class HashLDash_Tutorial_App(App):
    def build(self):
        return Gerenciador_de_telas()


if __name__ == '__main__':
    HashLDash_Tutorial_App().run()
