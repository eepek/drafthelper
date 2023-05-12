from tkinter import ttk, StringVar, IntVar, Toplevel



class Options:
    def __init__(self, update):
        """Creates new Options class which is used in TopLevel menu window
        to get leagues scoring and position amounts from the user.

        Args:
            update (function): Function that returns the inputted
            information to settings_view class
        """
        settings_window = Toplevel()
        settings_window.title('League settings')
        settings_window.minsize(300,200)
        self._root = settings_window
        self._update = update
        self.choose()

    def choose(self):
        """Creates elements in the options menu window and grids them.
        Optionomenus for different positions are gridded by calling
        external function.
        """
        self._main = ttk.Frame(master=self._root)
        self._main.grid()

        self._scoring_format = ttk.Label(master=self._main, text='Choose your scoring format:')
        self._scoring_format.grid(row=0,columnspan=6, pady=10)
        self._scoring_variable = StringVar(self._main, 'PPR')
        ppr = ttk.Radiobutton(master=self._main, text='PPR', value='PPR', variable=self._scoring_variable)
        half_ppr = ttk.Radiobutton(master=self._main, text='Half-PPR', value='Half_PPR', variable=self._scoring_variable)
        standard = ttk.Radiobutton(master=self._main, text='Standard', value='Standard', variable=self._scoring_variable)
        ppr.grid(columnspan=6)
        half_ppr.grid(columnspan=6)
        standard.grid(columnspan=6)
        self._positions_label = ttk.Label(master=self._main, text='Choose amounts for positions')
        self._positions_label.grid(columnspan=6, pady=10)
        self.grid_position_amounts()
        self._save_button = ttk.Button(self._main, text='Save', command=self.save_settings)
        self._save_button.grid(columnspan=6, pady=10)

    def grid_position_amounts(self):
        """Creates variables, labels and option menus for different
        playing positions and grids them side by side.
        """
        self._qb_amount = IntVar(self._main, 2)
        self._rb_amount = IntVar(self._main, 2)
        self._wr_amount = IntVar(self._main, 3)
        self._te_amount = IntVar(self._main, 1)
        self._k_amount = IntVar(self._main, 1)
        self._ds_amount = IntVar(self._main, 1)
        self._amount_variables = [self._qb_amount, self._rb_amount, self._wr_amount, self._te_amount, self._k_amount, self._ds_amount]
        self.position_labels = ['QB', 'RB', 'WR', 'TE', 'K', 'DS']
        self.qb = ttk.OptionMenu(self._main, self._qb_amount, 1, *[1,2])
        self.rb = ttk.OptionMenu(self._main, self._rb_amount, 2, *[2,3])
        self.wr = ttk.OptionMenu(self._main, self._wr_amount, 2, *[2,3])
        self.te = ttk.OptionMenu(self._main, self._te_amount, 1, *[0,1])
        self.k = ttk.OptionMenu(self._main, self._k_amount, 1, *[0,1])
        self.ds = ttk.OptionMenu(self._main, self._ds_amount, 1, *[0,1])
        self.position_menus = [self.qb, self.rb, self.wr, self.te, self.k, self.ds]
        for i, label in enumerate(self.position_labels):
            ttk.Label(master=self._main, text=label).grid(row =6, column=i)
            self.position_menus[i].grid(row=7, column=i)

    def save_settings(self):
        """Gets the chosen options from radiobuttons and optionmenus
        and returns them to settings_view via update function, when save button
        is clicked. Closes the TopLevel window after."""
        self._position_amounts = {}
        for i, amount in enumerate(self._amount_variables):
            self._position_amounts[self.position_labels[i]] = amount.get()
        self._update(self._scoring_variable.get(), self._position_amounts)
        self._root.destroy()
