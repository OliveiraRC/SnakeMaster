"""
Componente de rodapé.
"""

from src.ui.labels.base_label import BaseLabel


class FooterLabel(BaseLabel):
    """
    Label utilizado para informações de rodapé.
    """

    def __init__(self, text: str = "", **kwargs) -> None:
        super().__init__(
            text=text,
            font_size=14,
            **kwargs,
        )
        