"""
Componente de subtítulo.
"""

from src.ui.labels.base_label import BaseLabel


class SubtitleLabel(BaseLabel):
    """
    Label utilizado para subtítulos.
    """

    def __init__(self, text: str = "", **kwargs) -> None:
        super().__init__(
            text=text,
            font_size=22,
            **kwargs,
        )
        