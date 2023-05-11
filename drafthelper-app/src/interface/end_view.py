from tkinter import Tk, ttk
import webbrowser
from services.interface import App
from interface.styles import Style

class EndView:
    def __init__(self, root: Tk, interface: App) -> None:
        self._root = root
        self.style = Style()
        self._interface = interface
        self.end_view()
        self.get_teams()

    def end_view(self):

        #Frame
        self._main_frame = ttk.Frame(master=self._root, style='self.style.main.TFrame')
        self._header_frame = ttk.Frame(master=self._main_frame, style='self.style.header.TFrame')
        self._roster_frame = ttk.Frame(master=self._main_frame, style='self.style.roster.TFrame')

        #Labels
        self._header_label = ttk.Label(master=self._header_frame, text='The draft has ended!', style='self.style.header.TLabel')
        self._save_label = ttk.Label(master=self._roster_frame, text='Save your draft to a .txt file')
        self._save_button = ttk.Button(master=self._roster_frame, text='Save draft', command=self.save_draft)


        #Grid
        self._main_frame.grid(row=0, column=0, sticky='NSEW')
        self._header_frame.grid(row=0, column=0, sticky='WE')
        self._roster_frame.grid(row=1, column=0, sticky='NSWE')
        self._header_label.grid(row=0, column=0, padx=20, pady=20)
        self._save_label.grid()
        self._save_button.grid()

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
        number_of_teams = len(teams)
        column_number = 0
        roster_size=0
        for team, roster in teams.items():
            self.grid_team(roster, team, column_number)
            column_number += 1
            roster_size = len(roster)
        self._save_label.grid(row=2+roster_size, column=0, columnspan=number_of_teams)
        self._save_button.grid(row=3+roster_size, column=0, columnspan=number_of_teams)


    def grid_team(self, team:dict, team_name: str, team_number: int):
        team_column = team_number
        team_name_label = ttk.Label(master=self._roster_frame, text=f'{team_name}')
        team_name_label.grid(row=1, column=team_column)
        i=1
        for position, player in team.items():
            player_label = ttk.Label(master=self._roster_frame, text=f'{position}: {player}')
            player_label.grid(row=1+i, column=team_column)
            i += 1

    def save_draft(self):
        filename = self._interface.save_draft()
        self.generate_open_button(filename)


    def generate_open_button(self, filename: str):
        self._save_label.configure(text='Open the txt file in editor')
        self._save_button.configure(text='Open', command=lambda: self.open_txt_file(filename))


    def open_txt_file(self, filename: str):
        webbrowser.open(filename)