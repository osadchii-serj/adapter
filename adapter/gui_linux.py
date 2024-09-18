from dataclasses import dataclass
from interfaces.gui import GUI


@dataclass
class GUILinux(GUI):

    name = "Linux"

    def get_display(self):
        return "Display Linux"
