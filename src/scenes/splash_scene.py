"""
SplashScene.

Primeira tela exibida pelo Snake Master.
"""
from kivy.clock import Clock
from src.config.settings import Settings

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

from src.scenes.base_scene import BaseScene


class SplashScene(BaseScene):
    """
    Cena inicial da aplicação.

    Nesta primeira versão exibe apenas o nome do jogo
    e a versão da Engine.

    Futuramente esta tela será responsável por:

    - Exibir o logotipo.
    - Mostrar animações.
    - Exibir barra de carregamento.
    - Inicializar recursos do jogo.
    """

    def __init__(self, **kwargs) -> None:
        """
        Inicializa a Splash Screen.
        """
        super().__init__(name="splash", **kwargs)

        self.root_layout = FloatLayout()

        self.build_ui()

        self.add_widget(self.root_layout)

    def build_ui(self) -> None:
        """
        Constrói todos os componentes da interface.
        """
        title = Label(
            text="Snake Master\n\nEngine v0.1.0",
            font_size=28,
            size_hint=(1, 1),
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.5,
            },
            halign="center",
            valign="middle",
        )

        # Garante que a área do texto acompanhe o tamanho do widget,
        # permitindo alinhamento horizontal e vertical corretos.
        title.bind(size=self._update_text_size)

        self.root_layout.add_widget(title)

    @staticmethod
    def _update_text_size(label: Label, size: tuple[float, float]) -> None:
        """
        Atualiza a área utilizada pelo texto.

        Isso permite que o alinhamento do Label funcione corretamente.
        """
        label.text_size = size
        
    def on_enter(self, *args) -> None:
        """
        Inicia o temporizador da Splash Screen.
        """
        Clock.schedule_once(
            self.change_to_menu,
            Settings.SPLASH_DURATION,
        )


    def change_to_menu(self, dt: float) -> None:
            """
            Navega para o Menu Principal.
            """
            if self.manager is not None:
                self.manager.current = "menu"
        