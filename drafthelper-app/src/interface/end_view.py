from tkinter import Tk, ttk
from services.interface import App

class EndView:
    def __init__(self, root: Tk, interface: App) -> None:
        self._root = root
        self._interface = interface
        self.end_view()

    def end_view(self):
        #--------Styles------
        s = ttk.Style()
        s.configure('main.TFrame', 
                    background="#B1CECF"
                    )
        s.configure('header.TLabel',
                    background="#B1CECF",
                    font = ('Helvetica', 24, 'bold')
                    )
        
        #Frame
        self._main_frame = ttk.Frame(master=self._root, style='main.TFrame')

        #Header
        self._header_label = ttk.Label(master=self._main_frame, text='The draft has ended!', style='header.TLabel')

        #Grid
        self._main_frame.grid(row=0, column=0, sticky='NSEW')
        self._header_label.grid(row=0, column=0, padx=20, pady=20)