"""
Componente base para todos os labels do Snake Master.
"""

from kivy.uix.label import Label


class BaseLabel(Label):
    """
    Classe base para os componentes de texto do projeto.
    Centraliza o comportamento comum de alinhamento.
    """

    def __init__(self, text: str = "", **kwargs) -> None:
        super().__init__(
            text=text,
            halign="center",
            valign="middle",
            **kwargs,
        )

        self.bind(size=self._update_text_size)

    def _update_text_size(self, *_args) -> None:
        """
        Mantém a área do texto sincronizada com o tamanho do widget.
        """
        self.text_size = self.size
        