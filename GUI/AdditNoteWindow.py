import tkinter as tk
import DataIO


class Window:
    def __init__(self, parrent_window, edit=None):

        if edit:
            self.title = "Изменение заметки"
            self.text = "Изменить"
        else:
            self.title = "Добавление заметки"
            self.text = "Добавить"
        self.parrent_window = parrent_window

        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry("500x500")

        self.label_frame = tk.Frame(self.root)
        self.label_frame.pack(fill="x", padx=10, pady=10)

        self.label = tk.Label(self.label_frame, text="Название заметки:")
        self.label.pack(side=tk.LEFT)

        self.entry = tk.Entry(self.label_frame)
        self.entry.pack(side=tk.RIGHT, expand=True, fill="x")

        self.text_box = tk.Text(self.root)
        self.text_box.pack(expand=True, fill="both")

        button = tk.Button(self.root, text=self.text, command=lambda: self.button_action())
        button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.root.mainloop()

    def button_action(self):
        DataIO.write_to_file(self.entry.get(), self.text_box.get('1.0', 'end'))
        self.root.destroy()
        self.parrent_window.deiconify()
