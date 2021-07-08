from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)  # 1,1,1,1 white
Window.size = (360, 600)


class Aplicativo(App):
    def build(self):  # built é uma função herdada de APP
        layout = BoxLayout(orientation='vertical',
                           spacing=100,
                           padding=80)

        imagem = Image(source='Tutoriais_Kivy_KivyMD/icones/batman.png')

        button1 = Button(text='Login',
                         size_hint=(None, None),
                         width=100,
                         height=50,
                         font_size='20sp',
                         pos_hint={'center_x': 0.5})

        layout.add_widget(imagem)
        layout.add_widget(button1)

        return layout


if __name__ == '__main__':
    Aplicativo().run()

# Colocando size_hint=(None, None) o botão para de aumentar com o tamanho da
#  tela, assim terá o mesmo tamanho idependente do celular, Ipad etc. Usamos
#  width e height para determinar o tamanho fixo.
