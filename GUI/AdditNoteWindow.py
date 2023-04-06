import tkinter as tk
import DataIO
from DataIO import get_note


class Window:
    def __init__(self, parrent_window, editable_note_id=None):

        header = ""
        text = ""

        if editable_note_id is not None:
            self.title = "Изменение заметки"
            self.text = "Изменить"
            editable_note_data = get_note(editable_note_id)
            header = editable_note_data[0]
            text = editable_note_data[1]
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
        self.entry.insert(0, header)
        self.entry.pack(side=tk.RIGHT, expand=True, fill="x")

        self.text_box = tk.Text(self.root)
        self.text_box.insert('1.0', text)
        self.text_box.pack(expand=True, fill="both")

        button = tk.Button(self.root, text=self.text,
                           command=lambda: self.button_action((editable_note_id,
                                                               self.entry.get(),
                                                               self.text_box.get('1.0', 'end'))))
        button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.root.mainloop()

    def button_action(self, note):
        DataIO.write_to_file(note)
        self.root.destroy()
        self.parrent_window.update_table()
        self.parrent_window.main_window.deiconify()


