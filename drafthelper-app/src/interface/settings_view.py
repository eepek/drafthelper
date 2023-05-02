from tkinter import Tk, ttk, IntVar, messagebox
from services.interface import App

class SettingsView:
        def __init__(self, root: Tk, interface: App, start_draft):
            self._root = root
            self._settings = interface
            self._start_draft = start_draft
            self.set_up()
            self.settings_view()
            
        def set_up(self):

            self.__league_sizes = [i for i in range(6,15)]
            self.__league_size = IntVar(None, 6)

            self.__draft_positions = [i for i in range(1,15)]
            self.__draft_position = IntVar(None,1)

        def settings_view(self):
            #--------Styles------
            s = ttk.Style()
            s.configure('main.TFrame', 
                        background="#B1CECF"
                        )
            s.configure('header.TLabel',
                        background="#B1CECF",
                        font = ('Helvetica', 24, 'bold')
                        )
            s.configure('setting.TLabel',
                        padding=(60,10,60,10),
                        background="#B1CECF",
                        font = ('Helvetica', 16)
                        )
            s.configure('entry.TEntry',
                        font=('Helvetica', 16)
                        )
            #------Frames-----
            self.__main_frame = ttk.Frame(master=self._root, style='main.TFrame')
            #-----Labels-----
            header_label = ttk.Label(master=self.__main_frame, 
                                    text="Welcome to Draft Helper", 
                                    style='header.TLabel'
                                    )
            choose_name_label = ttk.Label(master=self.__main_frame,
                                        text="Please choose your team name:",
                                        style='setting.TLabel'
                                        )
            choose_league_size_label = ttk.Label(master=self.__main_frame,
                                                text="Please choose the number of teams: ",
                                                style='setting.TLabel'
                                                )
            choose_draft_position_label = ttk.Label(master=self.__main_frame,
                                                    text="Please choose your draft position: ",
                                                    style='setting.TLabel'
                                                    )
            #-----Entrys, buttons and dropdowns-----
            self.__name_entry = ttk.Entry(master=self.__main_frame, 
                                style='entry.TEntry'
                                )
            league_size_drop = ttk.OptionMenu(self.__main_frame,
                                            self.__league_size, 6, 
                                            *self.__league_sizes,
                                            direction='right'
                                            )
            draft_position_drop = ttk.OptionMenu(self.__main_frame,
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
            draft_position_drop.grid(row=6)
            start_draft_button.grid(row=8, pady=20)
            
            #------Grid config-----
            self._root.columnconfigure(0, weight=1)
            self._root.rowconfigure(0, weight=1)
            self.__main_frame.columnconfigure(0, weight=1)

        def incorrect_value(self, id):
            if id == 1:
                  messagebox.showerror('Incorrect name', 'Please choose a name')
            elif id == 3:
                  messagebox.showerror('Incorrect draft position', 'Please choose correct draft position')

        def send_settings_values(self):
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
   

        