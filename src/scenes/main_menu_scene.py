"""
Main Menu Scene.

Primeira tela interativa do Snake Master.
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

from src.scenes.base_scene import BaseScene
from src.config.settings import Settings
from src.ui.labels.footer_label import FooterLabel
from src.ui.labels.title_label import TitleLabel


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

        layout = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=40,
        )
    
        layout.add_widget(
            TitleLabel(
                text=Settings.APP_TITLE,
                size_hint=(1, 0.25),
            )
        )
    
        menu_items = (
            "Novo Jogo",
            "Configurações",
            "Créditos",
            "Sair",
        )
    
        for item in menu_items:
        
            option = Label(
                text=item,
                font_size=24,
                halign="center",
                valign="middle",
            )
    
            option.bind(
                size=lambda instance, size: setattr(
                    instance,
                    "text_size",
                    size,
                )
            )
    
            layout.add_widget(option)
    
        layout.add_widget(
            FooterLabel(
                text=f"Engine v{Settings.ENGINE_VERSION}",
                size_hint=(1, 0.15),
            )
        )
    
        self.root_layout.add_widget(layout)

    @staticmethod
    def _update_text_size(label: Label, size: tuple[float, float]) -> None:
        """
        Atualiza a área do texto para permitir alinhamento correto.
        """
        label.text_size = size
