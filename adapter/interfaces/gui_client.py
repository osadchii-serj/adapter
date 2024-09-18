from abc import ABC, abstractmethod


class GUIClient(ABC):

    @abstractmethod
    def get_gui_name(self):
        pass
