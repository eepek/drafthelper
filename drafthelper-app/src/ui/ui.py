from tkinter import Tk
from ui.views.settings_view import SettingsView
from ui.views.draft_view import DraftView
from ui.views.end_view import EndView
from services.interface import App
# from interface.initialize import App

class UI:
    """General graphical user interface draft that is used for handling different views
    during the use of program

    Attributes:
        root (Tk): Main Tk window
        interface (App): App class that works as interface between UI and other classes
    """
    def __init__(self, root: Tk):
        """Constructs a new UI class

        Args:
            root (Tk): Main Tk window
        """
        self._root = root
        self._interface = App()
        #Initial sizing
        self._root.minsize(1024,768)

    def show_settings_view(self):
        """Creates a SettingsView class that displays the settings view to the user
        """
        SettingsView(self._root, self._interface, self.draft_view)

    def draft_view(self):
        """Creates a DraftView class that displays the draft view to the user
        """
        DraftView(self._root, self._interface, self.end_of_draft_view)

    def end_of_draft_view(self):
        """Creates a EndView class that displays the end of draft view to the user
        """
        EndView(self._root, self._interface)
