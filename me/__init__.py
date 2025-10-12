from typing import Literal
from rendercv.themes.options import ThemeOptions, theme_options_theme_field_info
import pydantic

theme_options_theme_field_info.default = "classic"


class MeThemeOptions(ThemeOptions):
    theme: Literal["me"] = theme_options_theme_field_info
    show_citizenship: bool = True
