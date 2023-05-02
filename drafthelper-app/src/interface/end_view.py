from tkinter import Tk, ttk
from services.interface import App

class EndView:
    def __init__(self, root: Tk, interface: App) -> None:
        self._root = root
        self._interface = interface
        self.end_view()
        self.get_teams()

    def end_view(self):
        #--------Styles------
        s = ttk.Style()
        s.configure('main.TFrame', 
                    background="#a8dadc"
                    )
        s.configure('header.TFrame',
                    background='#a8dadc')
        s.configure('header.TLabel',
                    background="#a8dadc",
                    font = ('Helvetica', 24, 'bold')
                    )
        
        #Frame
        self._main_frame = ttk.Frame(master=self._root, style='main.TFrame')
        self._header_frame = ttk.Frame(master=self._main_frame, style='header.TFrame')
        self._roster_frame = ttk.Frame(master=self._main_frame, style='roster.TFrame')

        #Labels
        self._header_label = ttk.Label(master=self._header_frame, text='The draft has ended!', style='header.TLabel')

        #Grid
        self._main_frame.grid(row=0, column=0, sticky='NSEW')
        self._header_frame.grid(row=0, column=0, sticky='WE')
        self._roster_frame.grid(row=1, column=0, sticky='NSWE')
        self._header_label.grid(row=0, column=0, padx=20, pady=20)
        
        #Grid config
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._main_frame.columnconfigure(0, weight=1)
        self._main_frame.rowconfigure(0, weight=1)
        self._main_frame.rowconfigure(1, weight=5)
        self._header_frame.grid_rowconfigure(0, weight=1)
        self._header_frame.grid_columnconfigure(0, weight=2)

    def get_teams(self):
        teams = self._interface.get_all_teams()
        column_number = 0
        for team, roster in teams.items():
            self.grid_team(roster, team, column_number)
            column_number += 1

    def grid_team(self, team:dict, team_name: str, team_number: int):
        team_column = team_number
        team_name_label = ttk.Label(master=self._roster_frame, text=f'{team_name}')
        team_name_label.grid(row=1, column=team_column)
        i=1
        for position, player in team.items():
            player_label = ttk.Label(master=self._roster_frame, text=f'{position}: {player}')
            player_label.grid(row=1+i, column=team_column)
            i += 1