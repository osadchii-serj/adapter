from abc import ABC, abstractmethod


class GUI(ABC):

    @abstractmethod
    def get_display(self):
        pass
