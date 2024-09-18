from dataclasses import dataclass
from interfaces.gui import GUI


@dataclass
class GUIMac(GUI):

    name = "Mac"

    def get_display(self):
        return "Display Mac"
