import tkinter as tk

class Note:

        def __init__(self, frame, note=None) -> None:
            self.frame = tk.Frame(frame)

            self.entry = tk.Entry(self.frame)
            self.entry.pack()

            self.text = tk.Text(self.frame, height=10)
            self.text.pack()

            if note:
                self.entry.insert(0, note[1])
                self.text.insert("1.0", note[2])

            self.frame.pack(expand=1, fill="both")
