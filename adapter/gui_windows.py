from dataclasses import dataclass
from interfaces.gui import GUI


@dataclass
class GUIWindows(GUI):

    name = "Windows"

    def get_display(self):
        return "Display Windows"
