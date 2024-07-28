import sys
import tkinter as tk
from tkinter import ttk
from ui.notes import Notes
from handler import join_threads

class MainGUI:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Study Buddy")
        self.root.geometry("1000x500+999+999")

        # Defaults
        self.font = ('Arial', 18)

        # Menu
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        # Menu - File
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Close", command=self.on_close)
        self.menu_bar.add_cascade(menu=self.file_menu, label="File")

        # Tabs
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(expand=1, fill="both")
        # Tabs - Note
        self.notes_tab = ttk.Frame(self.tab_control)
        Notes(self.notes_tab)
        self.tab_control.add(self.notes_tab, text="Notes")
        # Tabs - Study
        self.study_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.study_tab, text="Study")
        # Tabs - Hyper
        self.hyper_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.hyper_tab, text="Hyper")

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def on_close(self):
        join_threads()
        self.root.destroy()
        sys.exit()
