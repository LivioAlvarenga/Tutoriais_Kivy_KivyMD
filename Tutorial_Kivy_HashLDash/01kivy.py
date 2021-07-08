# Tutorial de Kivy 001: Diga Olá
# http://inclem.net/2019/12/18/kivy/kivy_tutorial_001_say_hello/

from kivy.uix.label import Label
from kivy import require, __version__
from kivy.app import App

# usamos o require para determinar qual versão vamos usar do kivy
require('2.0.0')  # colocar a versão da instalação do Kivy

# O módulo uix é a seção que contém os elementos da interface do usuário, como
#  layouts e widgets.

# É necessário que a classe base do seu aplicativo (MeuAplicativo) herde da
#  classe do aplicativo (App)


class MeuAplicativo(App):
    # Esta é a função onde você deve inicializar e retornar seu Root Widget
    #  (Widget Raiz)
    def build(self):
        # Aqui, inicializamos um Label com a versão do kivy e retornamos sua
        #  instância.
        # Este rótulo será o widget raiz deste aplicativo.
        versao = __version__
        return Label(text=f'A versão da instalação do kivy é {versao}')


if __name__ == '__main__':
    # Aqui, a classe MeuAplicativo é inicializada e seu método run () chamado.
    #  Isso inicializa e inicia nosso aplicativo Kivy.
    MeuAplicativo().run()
