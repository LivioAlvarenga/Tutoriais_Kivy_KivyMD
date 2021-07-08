# 12 - Python Kivy - Usando o botão de voltar do android
# https://www.youtube.com/watch?v=V6GqRYrgthw&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=12

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file('17kivy.kv')


class Gerenciador_de_telas(ScreenManager):
    pass


class Menu(Screen):
    pass

# Para adicionar eventos de teclado importamos from kivy.core.window import
#  Window. Quando herdamos da classe Screen também herdamos eventos associados
#  a ela, ou seja quando entramos em Widget_geral(Screen) acontece alguns
#  eventos antes de entrar (on_pre_enter), quando entrar (on_enter) na tela e
#  antes de sair da tela (on_pre_leave) e por fim quando sair da tela
#  (on_leave). Usaremos estes eventos para vincular os eventos de teclado na
#  tela Widget_geral(Screen).


class Widget_geral(Screen):
    def __init__(self, tarefas=[], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.scroll_para_colocar_as_tarefas.add_widget(
                Tarefa_mais_botao_remover(text=tarefa))

    # Quando o evento antes de entrar na tela (on_pre_enter) rodar vamos
    #  vincular os eventos de teclado
    def on_pre_enter(self):
        # Vincularemos os eventos de teclado (on_keyboard) no Window.bind(),
        #  self.voltar representa que que toda vez que ter um evento de
        #  teclado ira chamar a função voltar.
        Window.bind(on_keyboard=self.voltar)

    # A função voltar é chamada toda vez que tiver um evento de teclado que
    #  vem do def on_pre_enter(self): atravez do
    #  Window.bind(on_keyboard=self.voltar). Toda vez que ele for chamado ele
    #  vira com window e a key(tecla que apertamos).
    def voltar(self, window, key, *args):
        # A tecla esc tem cod 27, ou seja quando ela for acionada voltaremos
        #  da tela tarefas para menu.
        if key == 27:
            # Ao ser ativado vamos ir para tela de menu atravez do
            #  App.get_running_app().root.current = 'menu' como no arquivo .kv
            App.get_running_app().root.current = 'menu'
            # Obs. para saber o numero da tecla comentamos o codigo
            #  #App.get_running_app().root.current = 'menu' e colocamos
            #  print(key), assim ao rodar o codigo e apertar as teclas vamos
            #  ver o codigo de cada tecla. Vamos usar esc (cod 27) para
            #  retornar da tela tarefas para menu. print(key)
            # Precisamos retornar True para informar que capturamos este
            #  evento de teclado e que ele não será passado para outros
            #  eventos.
            return True

    # Quando o evento antes de sair na tela (on_pre_leave) rodar vamos
    #  desvincular os eventos de teclado. Se não fizermos isso perdemos a
    #  funcionalidade de ao clicar esc na tela menu fechar o aplicativo.
    def on_pre_leave(self):
        # Aqui utilizados o mesmo comando de vincular porem trocamos o bind
        #  por unbind, ou seja, desvincular os eventos de teclado.
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
