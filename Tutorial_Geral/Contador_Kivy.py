from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


# fizemos tudo isso com Python
class Test(App):
    def build(self):
        # Box 1, box principal
        box = BoxLayout(orientation='vertical')  # por default horizontal
        box1 = BoxLayout()  # por default horizontal
        button = Button(text='Add', font_size=30, on_release=self.incrementar)
        button2 = Button(text='Sub', font_size=30, on_release=self.retirar)
        # self.label criamos uma instancia da variavel label dentro da
        #  class Test
        self.label = Label(text='1', font_size=30)
        box1.add_widget(button)
        box1.add_widget(button2)

        box2 = BoxLayout(orientation='vertical')  # por default horizontal
        box2.add_widget(self.label)

        box.add_widget(box1)
        box.add_widget(box2)

        return box

    def incrementar(self, button):
        button.text = 'Soltei'
        # sempre que soltar o botão conta 1
        self.label.text = str(int(self.label.text) + 1)

    def retirar(self, button2):
        button2.text = 'Soltei'
        # sempre que soltar o botão conta 1
        self.label.text = str(int(self.label.text) - 1)


Test().run()
