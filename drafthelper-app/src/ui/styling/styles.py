from tkinter import ttk

class Style:

    def __init__(self) -> None:

        self.style = ttk.Style()
        background_color = "#F6F1F1"
        self.style.configure('header.TLabel',
            background=background_color,
            font = ('Helvetica', 24, 'bold')
            )
        self.style.configure('user_frame.TFrame',
            background=background_color,
            font = ('Helvetica', 24, 'bold')
            )
        self.style.configure('draft_frame.TFrame',
            background=background_color,
            font = ('Helvetica', 24, 'bold')
            )
        self.style.configure('title.TFrame',
            background=background_color,
            font = ('Helvetica', 24, 'bold')
        )
        self.style.configure('player.TLabel',
            font = ('Helvetica', 16),
            background=background_color,
            width=25)
        self.style.configure('roster.TLabel',
            font = ('Helvetica', 13),
            width = 25,
            background = background_color
        )
        self.style.configure('draftFplayer.TLabel',
                    font= ('Helvetica', 18),
                    padding=(10,10,10,10),
                    width=12)
        self.style.configure('team.TLabel',
                    font= ('Helvetica', 14),
                    padding=(13,13,13,13),
                    background=background_color,
                    width = 15)
        self.style.configure('round.TLabel',
                    font=('Helvetica', 18, 'bold'),
                    background=background_color)
        self.style.configure('empty.TLabel',
            background='#a8dadc'
            )
        self.style.configure('main.TFrame',
            background=background_color
            )
        self.style.configure('header.TFrame',
                    background=background_color)
        self.style.configure('setting.TLabel',
                    padding=(60,10,60,10),
                    background=background_color,
                    font = ('Helvetica', 16)
                    )
        self.style.configure('entry.TEntry',
                    font=('Helvetica', 16)
                    )