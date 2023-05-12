from tkinter import Tk, ttk, IntVar, messagebox, Menu, StringVar, Toplevel
from services.interface import App
from ui.styling.styles import Style
from ui.views.options import Options

class SettingsView:
    """Class that is used to display and handle the actions in the settings view, where
    user needs to select a team name for their team, number of teams they want to take
    part in the draft and their own draft position. Creates file menu in menubar where
    user can do more specific changes according to their league settings, using the Option
    class.

    Attributes:
        root (Tk): Root window
        style (Style): Style class containing styling for labels
        settings (App): Interface that contains most methods used by the program
        start_draft (method): UI class method that changes the view to DraftView
    """
    def __init__(self, root: Tk, interface: App, start_draft):
        """Constructs a new SettingsView class and calls for methods to create widgets
        and grid them

        Args:
            root (Tk): Root Tk window
            interface (App): App class interface for using interface methods
            start_draft (_type_): UI class method for changing the view into draft_view
        """
        self._root = root
        self.style = Style()
        self._settings = interface
        self._start_draft = start_draft
        self.set_up()
        self.settings_view()

    def set_up(self):
        """Sets up variables and value lists for league size and draft positon optionmenus
        """
        self.__league_sizes = [i for i in range(6,15)]
        self.__league_size = IntVar(None, 6)

        self.__draft_positions = [i for i in range(1,15)]
        self.__draft_position = IntVar(None,1)


    def settings_view(self):
        """Creates Main frame, menubar and other widgets to be displayed in the view. Grids
        most widgets and uses gridconfigure to set up places for widgets.
        """
        #------Frames-----
        self.__main_frame = ttk.Frame(master=self._root, style='self.style.main.TFrame')

        #----Menu bar---
        self._menu = Menu(self._root)
        self._root.config(menu= self._menu)
        self._file_menu = Menu(self._menu)
        self._file_menu.add_command(label='Change league settings', command=self.change_league)
        self._file_menu.add_command(label='Exit', command=self._root.destroy)
        self._menu.add_cascade(label='Options', menu=self._file_menu)


        #-----Labels-----
        header_label = ttk.Label(master=self.__main_frame,
        text="Welcome to Draft Helper",
        style='self.style.header.TLabel'
                                )
        choose_name_label = ttk.Label(master=self.__main_frame,
                                    text="Please choose your team name:",
                                    style='self.style.setting.TLabel'
                                    )
        choose_league_size_label = ttk.Label(master=self.__main_frame,
                                            text="Please choose the number of teams: ",
                                            style='self.style.setting.TLabel'
                                            )
        choose_draft_position_label = ttk.Label(master=self.__main_frame,
                                                text="Please choose your draft position: ",
                                                style='self.style.setting.TLabel'
                                                )
        #-----Entrys, buttons and dropdowns-----
        self.__name_entry = ttk.Entry(master=self.__main_frame,
                            style='self.style.entry.TEntry'
                            )
        league_size_drop = ttk.OptionMenu(self.__main_frame,
                                        self.__league_size, 6,
                                        *self.__league_sizes,
                                        direction='right', command=self.update_positions
                                        )
        self.draft_position_drop = ttk.OptionMenu(self.__main_frame,
                                            self.__draft_position,
                                            1,
                                            *self.__draft_positions,
                                            direction='right'
                                            )
        start_draft_button = ttk.Button(master=self.__main_frame,
                                        text='Start your draft!',
                                        command=self.send_settings_values)
        #-----Grid-----
        self.__main_frame.grid(row=0, column=0, sticky='NSEW')
        header_label.grid(row=0, column=0, padx=20, pady=20)
        choose_name_label.grid(row=1, column=0)
        self.__name_entry.grid(row=2, column=0, padx=300, pady=10)
        choose_league_size_label.grid(row=3)
        league_size_drop.grid(row=4)
        choose_draft_position_label.grid(row=5)
        self.draft_position_drop.grid(row=6)
        start_draft_button.grid(row=8, pady=20)

        #------Grid config-----
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        self.__main_frame.columnconfigure(0, weight=1)

    def incorrect_value(self, error_id: int):
        """Displays correct error messagebox if given value is not acceptable

        Args:
            error_id (int): Identification number for input field giving the error
        """
        if error_id == 1:
            messagebox.showerror('Incorrect name', 'Please choose a name')
        elif error_id == 3:
            messagebox.showerror('Incorrect draft position', 'Please choose correct draft position')

    def change_league(self):
        """Generates TopLevel window which gives user chance to change more specific
        league settings
        """
        Options(self.update_values)

    def update_positions(self, size:int):
        """Updates draft position option menus values according to league size
        picked in league size option menu.

        Args:
            size (int): League size selected in the league_size_drop option menu
        """
        self.__draft_positions = [i for i in range(1,size+1)]
        self.draft_position_drop = ttk.OptionMenu(self.__main_frame,
                                            self.__draft_position,
                                            1,
                                            *self.__draft_positions,
                                            direction='right'
                                            )
        self.draft_position_drop.grid(row=6)

    def update_values(self, format: str, position_amounts: dict):
        """Gets values from TopLevel Options window for scoring format to be used
        and amount of players for each position. Passes information about change
        to App interface and saves the selections in Settings class.

        Args:
            format (str): Scoring format
            position_amounts (dict): For each position stores Position: Player amount
        """
        self.scoring_format = format
        self.amounts = position_amounts
        self._settings.set_format_change(True)
        self._settings.settings.set_changes(self.scoring_format, self.amounts)

    def send_settings_values(self):
        """Gets values from OptionMenu variables and checks if they are acceptable. If
        not calls for incorrect_values method to show error message. Acceptable values
        are sent to set functions in App interface. Calls start draft function to change
        the view to DraftView
        """
        if self.__draft_position.get() > self.__league_size.get():
            self.incorrect_value(3)
            return
        elif len(self.__name_entry.get()) == 0:
            self.incorrect_value(1)
            return
        self._settings.set_draft_position(self.__draft_position.get())
        self._settings.set_team_name(self.__name_entry.get())
        self._settings.set_league_size(self.__league_size.get())
        self._settings.start()
        self.__main_frame.destroy()
        self._start_draft()
