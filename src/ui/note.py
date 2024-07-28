import tkinter as tk

class Note:

        def __init__(self, frame, note=None) -> None:
            self.frame = tk.Frame(frame)

            self.entry = tk.Entry(self.frame)
            self.entry.grid(row=0, column=0, sticky='new')

            self.text = tk.Text(self.frame, height=10)
            self.text.grid(row=0, column=1, sticky='nsew')

            if note:
                self.entry.insert(0, note[1])
                self.text.insert("1.0", note[2])

            self.frame.grid_columnconfigure(0, weight=1)
            self.frame.grid_columnconfigure(1, weight=2)
            self.frame.grid_rowconfigure(0, weight=1)

            self.frame.pack(expand=1, fill="both")
