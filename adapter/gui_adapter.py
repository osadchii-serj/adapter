from interfaces.gui_client import GUIClient
from dataclasses import dataclass


@dataclass
class GUIAdapter:

    __gui: list
    __gui_client: GUIClient

    def adapter(self):
        for gui in self.__gui:
            if gui.name == self.__gui_client.get_gui_name():
                print(f"Подключён {gui.get_display()}")
            else:
                pass
