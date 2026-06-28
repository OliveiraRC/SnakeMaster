"""
Main Menu Scene.

Primeira tela interativa do Snake Master.
"""

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

from src.scenes.base_scene import BaseScene


class MainMenuScene(BaseScene):
    """
    Tela principal do jogo.

    Nesta primeira versão exibe apenas um texto.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(name="menu", **kwargs)

        self.root_layout = FloatLayout()

        self.build_ui()

        self.add_widget(self.root_layout)

    def build_ui(self) -> None:
        """
        Constrói a interface da cena.
        """

        title = Label(
            text="Main Menu\n\n(Em desenvolvimento)",
            font_size=30,
            size_hint=(1, 1),
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.5,
            },
            halign="center",
            valign="middle",
        )

        title.bind(size=self._update_text_size)

        self.root_layout.add_widget(title)

    @staticmethod
    def _update_text_size(label: Label, size: tuple[float, float]) -> None:
        """
        Atualiza a área do texto para permitir alinhamento correto.
        """
        label.text_size = size
