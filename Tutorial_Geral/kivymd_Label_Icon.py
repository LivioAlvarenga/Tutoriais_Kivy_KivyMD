from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.boxlayout import MDBoxLayout


class DemoApp(MDApp):
    def build(self):
        # halign = horizontal align
        layout = MDBoxLayout(orientation='vertical')

        label1 = MDLabel(text="Hello world",
                         halign="right",
                         theme_text_color="Primary",
                         font_style="Caption")

        label2 = MDLabel(text="Hello world",
                         halign="center",
                         theme_text_color="Secondary",
                         font_style="Subtitle2")

        label3 = MDLabel(text="Hello world",
                         halign="left",
                         theme_text_color="Hint",
                         font_style="H2")

        label4 = MDLabel(text="Hello world",
                         halign="center",
                         theme_text_color="Error",
                         font_style="Subtitle1")

        label5 = MDLabel(text="Hello world",
                         halign="center",
                         theme_text_color="Custom",
                         text_color=(0/255.0, 255/255.0, 127/255.0, 1),
                         font_style="H1")

        label6 = MDIcon(icon="language-python", halign="center")
        label7 = MDIcon(icon="apache-kafka", halign="center")

        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(label4)
        layout.add_widget(label5)
        layout.add_widget(label6)
        layout.add_widget(label7)

        return layout


if __name__ == '__main__':
    DemoApp().run()

# Existe 4 temas de cor para fonte theme_text_color
#  https://raw.githubusercontent.com/HeaTTheatR/KivyMD-data/master/gallery/kivymddoc/md-label-theme-text-color.png

# Para colocar cor rgb dividimos a mesma por 255.0
#  text_color=(0/255.0, 255/255.0, 127/255.0, 1)

# Existe estilos de fontes:
#  https://raw.githubusercontent.com/HeaTTheatR/KivyMD-data/master/gallery/kivymddoc/md-label-font-style.gif
