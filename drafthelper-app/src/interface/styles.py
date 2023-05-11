from tkinter import ttk

class Style:

    def __init__(self) -> None:

        self.style = ttk.Style()
        background_color = "#1d3557"
        self.style.configure('header.TLabel',
            background='#457b9d',
            font = ('Helvetica', 24, 'bold')
            )
        self.style.configure('user_frame.TFrame',
            background='#a8dadc',
            font = ('Helvetica', 24, 'bold')
            )
        self.style.configure('draft_frame.TFrame',
            background='#a8dadc',
            font = ('Helvetica', 24, 'bold')
            )
        self.style.configure('title.TFrame',
            background='yellow',
            font = ('Helvetica', 24, 'bold')
            )
        self.style.configure('player.TLabel',
            font = ('Helvetica', 16),
            width=20)
        self.style.configure('draftFplayer.TLabel',
                    font= ('Helvetica', 12),
                    width=15)
        self.style.configure('round.TLabel',
                    font=('Helvetica', 18, 'bold'),
                    background='#a8dadc')
        self.style.configure('empty.TLabel',
            background='#a8dadc'
            )
        self.style.configure('main.TFrame',
            background="#a8dadc"
            )
        self.style.configure('header.TFrame',
                    background='#a8dadc')
        self.style.configure('setting.TLabel',
                    padding=(60,10,60,10),
                    background="#B1CECF",
                    font = ('Helvetica', 16)
                    )
        self.style.configure('entry.TEntry',
                    font=('Helvetica', 16)
                    )