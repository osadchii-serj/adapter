from gui_client_windows import GUIClientWindows
from gui_client_linux import GUIClientLinux
from gui_client_mac import GUIClientMac

from gui_windows import GUIWindows
from gui_linux import GUILinux
from gui_mac import GUIMac

from gui_adapter import GUIAdapter

from random import choice


if __name__ == "__main__":

    gui_client_list = [
        GUIClientWindows(),
        GUIClientLinux(),
        GUIClientMac(),
    ]

    client = choice(gui_client_list)

    gui_list = [
        GUIWindows(),
        GUILinux(),
        GUIMac(),
    ]

    adapter = GUIAdapter(gui_list, client)
    adapter.adapter()
