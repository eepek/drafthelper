from tkinter import Tk, ttk, IntVar
from services.interface import App

class DraftView:

    def __init__(self, root: Tk, interface: App, end_of_draft):
        self._root = root
        self._end_of_draft = end_of_draft
        self._interface = interface
        self.__startstop = True
        self._current_draft_position = self._interface.get_draft_position()
        self.bot_labels = []
        self.choose_buttons = []
        self.user_labels = []
        self.initialize()
        if self.__startstop:
            self._root.after(10, self.check_draft_position)

    def initialize(self):
        #Styles
        s = ttk.Style()
        background_color = "#1d3557"
        s.configure('header.TLabel',
            background='#457b9d',
            font = ('Helvetica', 24, 'bold')
            )
        s.configure('user_frame.TFrame',
            background='#a8dadc',
            font = ('Helvetica', 24, 'bold')
            )
        s.configure('draft_frame.TFrame',
            background='#a8dadc',
            font = ('Helvetica', 24, 'bold')
            )
        s.configure('title.TFrame',
            background='#457b9d',
            font = ('Helvetica', 24, 'bold')
            )
        s.configure('player.TLabel',
            font = ('Helvetica', 16),
            width=20)
        s.configure('draftFplayer.TLabel',
                    font= ('Helvetica', 12),
                    width=15)
        s.configure('main.TFrame', 
            background=background_color
            )
        s.configure('round.TLabel',
                    font=('Helvetica', 18, 'bold'),
                    background='#a8dadc')
        s.configure('empty.TLabel',
            background='#a8dadc'
            )
        #Frames
        self._main_frame = ttk.Frame(master=self._root, style='main.TFrame')
        self._main_frame.grid(row=0, column=0, sticky='NSWE')
        self._title_frame = ttk.Frame(master=self._main_frame,  style='title.TFrame')
        self._title_frame.grid(row=0, column=0, columnspan=2, sticky='NSEW')
        self._user_frame = ttk.Frame(master=self._main_frame, style="user_frame.TFrame")
        self._user_frame.grid(row=1, column=0, sticky='NSEW')
        self._draft_frame = ttk.Frame(master=self._main_frame, style='draft_frame.TFrame')
        self._draft_frame.grid(row=1, column=1, columnspan=2, sticky='NSWE')
        #First row of empty labels
        self._empty_label = ttk.Label(master=self._draft_frame, style='empty.TLabel')

        #Labels
        self._header_label = ttk.Label(master=self._title_frame,
                                    text="The draft is on!", 
                                    style='header.TLabel')
        self._round_labels = [ttk.Label(master=self._draft_frame,
                                        text=f'{i}:',
                                        style='round.TLabel')
                                        for i in range(1,self._interface.rounds+1)]
        
        self._roster_labels = [ttk.Label(master=self._user_frame,
                                    text=f'{position}: {player}',
                                    style=''
                                    )
                                    for position, player in self._interface.roster.get_user_roster().items()]  
        
        #Buttons
        self.generate_choose_buttons()
        
        #Grid
        
        self._header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        self.grid_labels()
        self.grid_user_roster()
        
        
        #Grid-config
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._main_frame.columnconfigure(0, weight=1)
        self._main_frame.columnconfigure(1, weight=30)
        self._main_frame.rowconfigure(0, weight=1)
        self._main_frame.rowconfigure(1, weight=30)

        self._title_frame.grid_rowconfigure(0, weight=1)
        self._title_frame.grid_columnconfigure(0, weight=2)



    def check_draft_position(self):
        if self._interface.is_draft_done:
            self._main_frame.destroy()
            self._end_of_draft()
        self._current_row = self._interface.get_current_round()
        self._current_draft_position = self._interface.get_draft_position()
        if self._interface.is_it_users_turn():
            self.__startstop = False
            self._header_label.config(text="It is your turn to choose!")
            self.grid_players_for_user(self._interface.users_turn())
            self.update_user_roster()
            self.__startstop = True
        else:
            self._header_label.config(text="Waiting for your next turn!")
            self.get_bot_choice()
            self._root.after(10, self.check_draft_position)

    def grid_labels(self):
        team_names = [ttk.Label(master=self._draft_frame,
                                text=f'{team_name}', style='draftFplayer.TLabel')
                                for team_name in self._interface.get_team_names()]
        for i in range(len(team_names)):
            team_names[i].grid(row=1, column=1+i)

    def grid_chosen_player(self, id: int):
        player_label = ttk.Label(master=self._draft_frame,
                                 text=f'{self._player_names[id]}\n{self._positions[id]}',
                                 style='draftFplayer.TLabel')
        player_label.grid(row=self._current_row+4, 
                            column=self._current_draft_position,
                            padx=5,
                            pady=10,
                            sticky='EW'
                            )


    def player_chosen(self, id: int):
        self.grid_chosen_player(id)
        self._interface.player_chosen_by_user(id)
        self.delete_user_labels()
        self.generate_choose_buttons()
        self.__startstop = True
        self._root.after(10, self.check_draft_position)

    def update_user_roster(self):
        user_roster = self._interface.roster.get_user_roster()
        print(user_roster)
        self._roster_labels = [ttk.Label(master=self._user_frame,
                                    text=f'{position}: {player}',
                                    style=''
                                    )
                                    for position, player in user_roster.items()]
        self.grid_user_roster()
        
    def grid_user_roster(self):
        for i in range(len(self._roster_labels)):
            self._roster_labels[i].grid(row=5+i, column=0)

    def delete_user_labels(self):
        for i in range(3):
            self.user_labels[i].destroy()
            self.choose_buttons[i].destroy()
        self.user_labels = []
        self.choose_buttons = []

    def generate_choose_buttons(self):
        self.choose_buttons = [ttk.Button(master=self._user_frame,
                                text="Choose",
                                command=lambda: self.player_chosen(0)),
                                ttk.Button(master=self._user_frame,
                                text="Choose",
                                command=lambda: self.player_chosen(1)),
                                ttk.Button(master=self._user_frame,
                                text="Choose",
                                command=lambda: self.player_chosen(2))]

    def get_bot_choice(self):
        player = self._interface.bot_turn()
        
        bot_choice_label = ttk.Label(master=self._draft_frame, 
                                           text = f'{player[0]}\n{player[1]}',
                                           style='draftFplayer.TLabel')
        bot_choice_label.grid(row=self._current_row+4, 
                                column=self._current_draft_position,
                                padx=5,
                                pady=10,
                                sticky='EW'
                                )

        
    
    def grid_players_for_user(self, player_data: list):
        self._player_names = player_data[0]
        self._teams = player_data[1]
        self._positions = player_data[2]
        for i in range(3):
            self.user_labels.append(ttk.Label(master=self._user_frame, 
                                    text=f'{self._player_names[i]} {self._teams[i]} {self._positions[i]}',
                                    style= 'player.TLabel'))
            
        for i in range(3):
            self.user_labels[i].grid(row=1+i, column=0)
            self.choose_buttons[i].grid(row=1+i, column=1)

    
            

       

        



    