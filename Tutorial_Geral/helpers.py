username_helper = """
MDTextField:
    hint_text: "Digite seu usuário:"
    helper_text: "ou clique aqui se esqueceu seu usuário."
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width:300

"""

list_helper = """
ScrollView:
    MDList:
        OneLineListItem:
            text: 'Item1'
        OneLineListItem:
            text: 'Item2'

"""

list_helper2 = """
ScrollView:
    MDList:
        id: container

"""

list_helper3 = """
Screen:
    ScrollView:
        MDList:
            id: container

"""

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Livio'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["clock", lambda x: app.navigation_draw()]]
            elevation: 8

        MDLabel:
            text: 'hello world'
            halign: 'center'

        MDBottomAppBar:
            MDToolbar:
                icon: 'language-python'
                type: 'bottom'
                left_action_items:
                    [["coffee", lambda x: app.navigation_draw()]]
                mode: 'center'
                on_action_button: app.navigation_draw()

"""
