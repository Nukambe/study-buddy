import tkinter as tk
from tkinter import messagebox, ttk
from ui.note import Note
from handler import get_db

class Notes:

    def __init__(self, tab) -> None:
        self.db = get_db()
        self.frame = ttk.Frame(tab)

        # Create a canvas with a scrollbar
        self.canvas = tk.Canvas(self.frame, height=500)
        self.scroll_bar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scroll_bar.set)

        # Create a frame inside the canvas to hold the notes
        self.notes_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.notes_frame, anchor="nw")

        # Pack the canvas and scrollbar
        self.canvas.pack(side="left", expand=1, fill="both")
        self.scroll_bar.pack(side="right", fill="y")

        # Add note button
        self.add_note_button = tk.Button(self.frame, text="Add Note", command=self.add_note)
        self.add_note_button.pack()

        self.frame.pack(expand=1, fill="both")

        # Bind the configuration event to update the scroll region
        self.notes_frame.bind("<Configure>", self.on_frame_configure)

        self.load_notes()

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def load_notes(self):
        notes = self.db.get_notes()
        for note in notes:
            Note(self.notes_frame, note)

    def add_note(self):
        Note(self.notes_frame)
