import tkinter as tk
from tkinter import messagebox, ttk
from ui.note import Note
from handler import get_db

class Notes:

    def __init__(self, tab) -> None:
        self.db = get_db()
        self.frame = ttk.Frame(tab)

        self.notes = tk.Canvas(self.frame, height=500)
        self.notes.pack(expand=1, fill="both")
        self.scroll_bar = ttk.Scrollbar(self.notes, orient="vertical")
        self.scroll_bar.pack(side="right", fill="y")
        self.notes.config(yscrollcommand=self.scroll_bar.set)

        self.add_note_button = tk.Button(self.frame, text="Add Note", command=self.add_note)
        self.add_note_button.pack()

        self.frame.pack(expand=1, fill="both")

        self.load_notes()

    def load_notes(self):
        notes = self.db.get_notes()
        for note in notes:
            Note(self.notes, note)

    def add_note(self):
        Note(self.notes)
