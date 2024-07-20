import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.font = ('Arial', 18)

        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Close", command=self.on_close)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Close without question", command=exit)

        self.action_menu = tk.Menu(self.menu_bar)
        self.action_menu.add_command(label="Show message", command=self.show_message)

        self.menu_bar.add_cascade(menu=self.file_menu, label="File")
        self.menu_bar.add_cascade(menu=self.action_menu, label="action")
        self.root.config(menu=self.menu_bar)

        self.label = tk.Label(self.root, text="Message", font=self.font)
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, font=self.font, height=5)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Message Box", font=self.font, variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show message", font=self.font, command=self.show_message)
        self.button.pack()

        self.entry = tk.Entry(self.root, font=self.font)
        self.entry.bind("<KeyPress>", self.shortcut)
        self.entry.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        if event.state == 16 and event.keysym == "Return":
            self.show_message()

    def on_close(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
