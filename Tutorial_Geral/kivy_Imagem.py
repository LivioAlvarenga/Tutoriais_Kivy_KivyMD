from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)  # 1,1,1,1 white


class Aplicativo(App):
    def build(self):  # built é uma função herdada de APP
        # imagem = Image(source='icones/batman.png')
        imagem = AsyncImage(
            source='https://i.pinimg.com/originals/f2/a6/dd/\
f2a6dd67b6d6bfe92900293cfc7d64cb.png')
        return imagem


if __name__ == '__main__':
    Aplicativo().run()

# AsyncImage(source='https://i.pinimg.com/originals/f2/a6/dd/f2a6dd67b6d6bfe92900293cfc7d64cb.png')
#  para imagem da internet.
# Image(source='icones/batman.png') para imagem salva.
