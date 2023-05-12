from tkinter import Tk, ttk, messagebox
from services.interface import App
from ui.styling.styles import Style

class DraftView:
    """Class that contains all the necessary widgets to display and handle the draft event.

    Attributes:
        root (Tk): Main Tk window
        end_of_draft (function): Function used to change the view to end of draft view
        interface (App): Main interface working between UI and other classes
        startstop (Bool): Timer used to refresh the view
        current_draft_position (Int): Position that has the draf turn at that moment
        bot_labels (list): Contains Labels for computer made player choices
        choose_buttons (list): Contains tkk buttons displayed to user
        user_labels (list): Contains labels that display players to user
        current_row (int): Current round of draft, used to put player labels on right row
        roster_label (list): Contains labels for displaying user roster
        roster_colors (list): Contains colors for label backgrounds for different positions

    """

    def __init__(self, root: Tk, interface: App, end_of_draft):
        """Constructs a new DraftView class and calls initialize method. If not users turn
        refreshes view every 1 second.

        Args:
            root (Tk): Main Tk window
            interface (App): App class main interface working between UI and other classes
            end_of_draft (_type_): Function used to change the view to end of draft view
        """
        self.style = Style()
        self._root = root
        self._end_of_draft = end_of_draft
        self._interface = interface
        self.__startstop = True
        self._current_draft_position = self._interface.get_draft_position()
        self.bot_labels = []
        self.choose_buttons = []
        self.user_labels = []
        self._current_row = int
        self._roster_labels = []
        self._roster_colors = {'QB': '#A8E6CF', 'RB': '#DCEDC1', 'WR': '#FFD3B6', 'TE': '#FFAAA5', 'K': '#BFCCB5', 'DS': '#DBDFEA'}
        self.initialize()
        if self.__startstop:
            self._root.after(1000, self.check_draft_position)

    def initialize(self):
        """Method used for creating and gridding widgets and configuring them.
        Creates main frame, static labels and calls method for creating buttons.
        Grids widgets either directly or calls methods to do it.
        """
        #Frames
        self._main_frame = ttk.Frame(master=self._root, style='self.style.main.TFrame')
        self._main_frame.grid(row=0, column=0, sticky='NSWE')
        self._title_frame = ttk.Frame(master=self._main_frame,  style='self.style.title.TFrame')
        self._title_frame.grid(row=0, column=0, columnspan=2, sticky='NSEW')
        self._user_frame = ttk.Frame(master=self._main_frame, style="self.style.user_frame.TFrame")
        self._user_frame.grid(row=1, column=0, sticky='NSEW')
        self._draft_frame = ttk.Frame(master=self._main_frame, style='self.style.draft_frame.TFrame')
        self._draft_frame.grid(row=1, column=1, columnspan=2, sticky='NSWE')
        #First row of empty labels
        self._empty_label = ttk.Label(master=self._draft_frame, style='self.style.empty.TLabel')

        #Labels
        self._header_label = ttk.Label(master=self._title_frame,
                                    text="The draft is on!",
                                    style='self.style.header.TLabel')
        self._round_labels = [ttk.Label(master=self._draft_frame,
                                        text=f'{i}:',
                                        style='self.style.round.TLabel')
                                        for i in range(1,self._interface.rounds+1)]

        self._roster_labels = [ttk.Label(master=self._user_frame,
                                    text=f'{position}: {player}',
                                    style=''
                                    )
                                    for position, player in self._interface.roster.get_user_roster().items()]
        self._choose_another_label = ttk.Label(master=self._user_frame, text="Choose other player:")
        #Buttons and entry
        self.generate_choose_buttons()
        self._player_name_entry = ttk.Entry(master=self._user_frame, style='self.style.entry.TEntry')
        self._find_button = ttk.Button(master=self._user_frame, text="Find", command=self.find_player)

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
        """Method that contains main functionality needed for the draft
        event to flow forward. Checks which turn is it and calls method
        based on the current position.
        """
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
            self.update_user_roster()
            self.__startstop = True
        else:
            self._header_label.config(text="Waiting for your next turn!")
            self.get_bot_choice()
            self._root.after(1000, self.check_draft_position)

    def grid_labels(self):
        """Creates team name labels and grids them
        """
        team_names = [ttk.Label(master=self._draft_frame,
                                text=f'{team_name}', style='self.style.draftFplayer.TLabel')
                                for team_name in self._interface.get_team_names()]
        for i, team in enumerate(team_names):
            team.grid(row=1, column=1+i)

    def grid_chosen_player(self, name: str, position: str):
        """After player is chosen, creates label for player and grids it
        in correct position. Deletes labels for users recommended players
        and generates new choose buttons.

        Args:
            name (str): Player name
            position (str): Players playing position
        """
        player_label = ttk.Label(master=self._draft_frame,
                                 text=f'{name}\n{position}',
                                 style='self.style.draftFplayer.TLabel')
        if position.startswith('K'):
            position = 'K'
        color = self._roster_colors[position]
        player_label.configure(background=color)
        player_label.grid(row=self._current_row+4,
                            column=self._current_draft_position,
                            padx=5,
                            pady=10,
                            sticky='EW'
                            )
        self._player_name_entry.delete(0, 'end')
        self.delete_user_labels()
        self.generate_choose_buttons()
        self.__startstop = True
        self._root.after(1000, self.check_draft_position)


    def player_chosen(self, id_number: int):
        """If player is chosen by button click, receives buttons id and
        passes player name to App interface, receiving players name and position
        after pick is checked to be eligible and added to roster. Calls for
        player to be labeled and gridded.

        Args:
            id_number (int): Number of button that was clicked
        """
        player_name = self._player_names[id_number]
        chosen = self._interface.find_player_by_name(player_name)
        self.grid_chosen_player(chosen[0],chosen[1])

    def find_player(self):
        """Method used for user to enter players name directly into entry box.
        Needs at least 7 letters to avoid confusion of names. Displays error
        messages accordingly. Calls for player to be labeled and gridded
        """
        player = self._player_name_entry.get()
        if len(player) < 7:
            messagebox.showinfo('Name too short', 'Enter first and last name')
            return
        chosen = self._interface.find_player_by_name(player)
        if chosen is None:
            messagebox.showinfo('Player not found', 'Player not found, please try again!')
            return
        self.grid_chosen_player(chosen[0],chosen[1])

    def update_user_roster(self):
        """Gets updated user roster via App interface and creates labels.
        Calls method to grid the roster labels.
        """
        user_roster = self._interface.roster.get_user_roster()
        self._roster_labels = [ttk.Label(master=self._user_frame,
                                    text=f'{position}: {player}',
                                    style=''
                                    )
                                    for position, player in user_roster.items()]
        self.grid_user_roster()

    def grid_user_roster(self):
        """Method that grids created roster labels
        """
        for i, label in enumerate(self._roster_labels):
            label.grid(row=10+i, column=0)

    def delete_user_labels(self):
        """Deletes the recommended players from view after pick has been
        made and initializes list for next user pick
        """
        for i in range(3):
            self.user_labels[i].destroy()
            self.choose_buttons[i].destroy()
        self.user_labels = []
        self.choose_buttons = []

    def generate_choose_buttons(self):
        """Generates ttk buttons used for selecting recommended player
        """
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
        """Calls for App interface to make player selection for bot and
        labels and grids the selected player.
        """
        player = self._interface.bot_turn()

        bot_choice_label = ttk.Label(master=self._draft_frame,
                                           text = f'{player[0]}\n{player[1]}',
                                           style='self.style.draftFplayer.TLabel')
        if player[1].startswith('K'):
            color =self._roster_colors['K']
        else:
            color = self._roster_colors[player[1]]
        bot_choice_label.configure(background=color)
        bot_choice_label.grid(row=self._current_row+4,
                                column=self._current_draft_position,
                                padx=5,
                                pady=10,
                                sticky='EW')


    def grid_players_for_user(self, player_data: list):
        """Gets recommended players for user and creates labels
        and grids them along with player search entry box and
        appropriate buttons.

        Args:
            player_data (list): List containing 3 lists for recommended players,
            player names, their teams and playing positions.
        """
        self._player_names = player_data[0]
        self._teams = player_data[1]
        self._positions = player_data[2]
        for i in range(3):
            self.user_labels.append(ttk.Label(master=self._user_frame,
                                    text=f'{self._player_names[i]}, {self._teams[i]}, {self._positions[i]}',
                                    style= 'self.style.player.TLabel'))

        for i in range(3):
            self.user_labels[i].grid(row=1+i, column=0)
            self.choose_buttons[i].grid(row=1+i, column=1)

        self._player_name_entry.grid(row=4+i, column=0)
        self._choose_another_label.grid(row=3+i, column=0)
        self._find_button.grid(row=5+i, column=0)
