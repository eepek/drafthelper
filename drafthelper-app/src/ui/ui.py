from tkinter import Tk
from ui.settings_view import SettingsView
from ui.draft_view import DraftView
from ui.end_view import EndView
from services.interface import App
# from interface.initialize import App

class UI:
    def __init__(self, root: Tk):
        self._root = root
        self._interface = App()
        #Initial sizing
        self._root.minsize(1024,768)

    def show_settings_view(self):
        SettingsView(self._root, self._interface, self.draft_view)

    def draft_view(self):
        DraftView(self._root, self._interface, self.end_of_draft_view)

    def end_of_draft_view(self):
        EndView(self._root, self._interface)







if __name__ == "__main__":
    window = Tk()
    window.title('Draft Helper - Fantasy draft simulator')

    ui = UI(window)
    ui.show_settings_view()
    window.mainloop()
