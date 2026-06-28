"""
Primeira tela exibida pelo jogo.
"""

from kivy.uix.floatlayout import FloatLayout

from kivy.uix.label import Label

from src.scenes.base_scene import BaseScene


class SplashScene(BaseScene):

    def __init__(self, **kwargs):
        super().__init__(name="splash", **kwargs)

        self.build_ui()

    def build_ui(self):
        root = FloatLayout()

        title = Label(
            text="Snake Master\n\nEngine v0.1.0",
            font_size=28,
            size_hint=(1, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        root.add_widget(title)

        self.add_widget(root)
        