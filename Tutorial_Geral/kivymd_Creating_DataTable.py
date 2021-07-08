from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):

    cabeçalho = [("No.", dp(18)),
                 ("Food", dp(20)),
                 ("Calories", dp(20))
                 ]

    tabela_dados = [("1", "Burger", "300"),
                    ("2", "Oats", "200"),
                    ("3", "Oats", "200"),
                    ("4", "Oats", "200"),
                    ("5", "Oats", "200"),
                    ("6", "Oats", "200"),
                    ("7", "Oats", "200"),
                    ("8", "Oats", "200")
                    ]

    def build(self):
        screen = Screen()
        data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(0.9, 0.6),
                                 check=True,
                                 column_data=self.cabeçalho,
                                 row_data=self.tabela_dados
                                 )

        data_table.bind(on_check_press=self.on_check_press)
        data_table.bind(on_row_press=self.on_row_press)
        screen.add_widget(data_table)
        return screen

    def on_check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def on_row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)


if __name__ == '__main__':
    DemoApp().run()

'''
MDTableData - How to create a basic Table
- Add columns
- Add row data
- size_hint
- pos_hint
- check
- on_check_press & on_row_press
'''
