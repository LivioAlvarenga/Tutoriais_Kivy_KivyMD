# https://www.youtube.com/watch?v=tToJBfDgCsc&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=48

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton


class Codemy_Tutorial_App(MDApp):

    dialog = None

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('codemy_kivyMd_35_Dialog_box.kv')

    def show_alert_dialog(self):

        if not self.dialog:
            self.dialog = MDDialog(
                title='Titulo do popup!',
                text='Texto do popup!!!',
                buttons=[
                    MDFlatButton(
                        text='CANCEL',
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                    MDRectangleFlatButton(
                        text='SUBMIT',
                        text_color=self.theme_cls.primary_color,
                        on_release=self.submit
                    )
                ]
            )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def submit(self, obj):
        self.dialog.dismiss()
        self.root.ids.my_label.text = 'Botão SUBMIT press!!!'


if __name__ == '__main__':
    Codemy_Tutorial_App().run()
