from tkinter import Tk, ttk
from services.interface import App

class DraftView:

    def __init__(self, root: Tk, interface: App, end_of_draft):
        self._root = root
        self._end_of_draft = end_of_draft
        self._interface = interface
        self.__startstop = True

        #initalize
        self.bot_labels = []
        self.choose_buttons = []
        self.user_labels = []

        #check_draft_position
        self._current_draft_position = self._interface.get_draft_position()
        self._current_row = 0

        #Grid_players_for_user
        self._player_names = []
        self._teams = []
        self._positions = []
        self.initialize()

        #For looping
        if self.__startstop:
            self._root.after(1, self.check_draft_position)

    def initialize(self):
        #Styles
        s = ttk.Style()
        background_color = "#B1CECF"
        s.configure('header.TLabel',
            background=background_color,
            font = ('Helvetica', 24, 'bold')
            )
        s.configure('player.TLabel',
            font = ('Helvetica', 16))
        s.configure('main.TFrame',
            background=background_color
            )
        s.configure('empty.TLabel',
            background=background_color
            )
        #Main frame
        self._main_frame = ttk.Frame(master=self._root, style='main.TFrame')

        #First row of empty labels
        self._empty_label = ttk.Label(master=self._main_frame, style='empty.TLabel')

        #Labels
        self._header_label = ttk.Label(master=self._main_frame,
                                    text="The draft is on!",
                                    style='header.TLabel')
        #Buttons
        self.generate_choose_buttons()


        #Grid
        self._main_frame.grid(row=0, column=0, sticky='NSWE')
        self._header_label.grid(row=0, column=0, columnspan=14, padx=20, pady=20)
        self.grid_empty_labels()


        #Grid-config
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._main_frame.columnconfigure(0, weight=1)


    def check_draft_position(self):
        if self._interface.is_draft_done:
            self._main_frame.destroy()
            self._end_of_draft()
            return

        self._current_row = self._interface.get_current_round()
        self._current_draft_position = self._interface.get_draft_position()

        if self._interface.is_it_users_turn():
            self.__startstop = False
            self._header_label.config(text="It is your turn to choose!")
            self.grid_players_for_user(self._interface.users_turn())
            self.__startstop = True
        else:
            self._header_label.config(text="Waiting for your next turn!")
            self.get_bot_choice()
            self._root.after(1, self.check_draft_position)

    def grid_empty_labels(self):
        for i in range(self._interface.get_league_size()):
            self._empty_label.grid(row=4, column=0+i, sticky='W')

    def grid_chosen_player(self, id: int):
        player_label = ttk.Label(master=self._main_frame,
                                 text=f'You chose:\n{self._player_names[id]} {self._positions[id]}')
        player_label.grid(row=self._current_row+4,
                            column=self._current_draft_position-1,
                            padx=5,
                            pady=10,
                            sticky='W'
                            )


    def player_chosen(self, id: int):
        self.grid_chosen_player(id)
        self._interface.player_chosen_by_user(id)
        self.delete_user_labels()
        self.generate_choose_buttons()
        self.__startstop = True
        self._root.after(10, self.check_draft_position)

    def delete_user_labels(self):
        for i in range(3):
            self.user_labels[i].destroy()
            self.choose_buttons[i].destroy()
        self.user_labels = []
        self.choose_buttons = []

    def generate_choose_buttons(self):
        self.choose_buttons = [ttk.Button(master=self._main_frame,
                                text="Choose",
                                command=lambda: self.player_chosen(0)),
                                ttk.Button(master=self._main_frame,
                                text="Choose",
                                command=lambda: self.player_chosen(1)),
                                ttk.Button(master=self._main_frame,
                                text="Choose",
                                command=lambda: self.player_chosen(2))]

    def get_bot_choice(self):
        player = self._interface.bot_turn()

        bot_choice_label = ttk.Label(master=self._main_frame,
                                           text = f'Team {self._current_draft_position} chose:\n{player[0]}  {player[1]}')
        bot_choice_label.grid(row=self._current_row+4,
                                column=self._current_draft_position-1,
                                padx=5,
                                pady=10,
                                sticky='W'
                                )



    def grid_players_for_user(self, player_data: list):
        self._player_names = player_data[0]
        self._teams = player_data[1]
        self._positions = player_data[2]
        for i in range(3):
            self.user_labels.append(ttk.Label(master=self._main_frame,
                                    text=f'{self._player_names[i]} {self._teams[i]} {self._positions[i]}',
                                    style= 'player.TLabel'))

        for i in range(3):
            self.user_labels[i].grid(row=1+i, column=0)
            self.choose_buttons[i].grid(row=1+i, column=1)
