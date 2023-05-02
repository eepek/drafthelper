from tkinter import Tk
from interface.ui import UI
#Starts the program with graphical user interface
window = Tk()
window.title('Draft Helper - Fantasy draft simulator')

ui = UI(window)
ui.show_settings_view()
window.mainloop()
