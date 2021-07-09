from kivy.app import App
from kivy.config import Config
from kivy.core.audio import SoundLoader
from widgets import Pong
from telas import TelaJogo, TelaMenu, TelaVencedor1, TelaVencedor2
from kivy.uix.screenmanager import ScreenManager

# Carrega nosso arquivo de configurações
Config.read("Tutoriais_Kivy_KivyMD/Jogo_pong/config.ini")

# Cria nosso Gerenciador de Telas
screen_manager = ScreenManager()


class PongApp(App):

    def build(self):

        # Carrega o áudio
        sound = SoundLoader.load(
            'Tutoriais_Kivy_KivyMD/Jogo_pong/audio/bg-music.mp3')

        # Verifica se houve o carregamento do nosso áudio e coloca para tocar
        if sound:
            sound.play()

        # Objeto do nosso jogo
        pong = Pong(screen_manager=screen_manager)

        # Cria a Tela de Jogo
        tela_jogo = TelaJogo(name="jogo")

        # Adiciona o Widget Pong
        tela_jogo.add_widget(pong)

        # Adiciona as telas ao nosso gerenciador
        screen_manager.add_widget(TelaMenu(name='menu'))
        screen_manager.add_widget(tela_jogo)
        screen_manager.add_widget(TelaVencedor1(name='vencedor_1'))
        screen_manager.add_widget(TelaVencedor2(name='vencedor_2'))

        return screen_manager


if __name__ == '__main__':
    PongApp().run()
