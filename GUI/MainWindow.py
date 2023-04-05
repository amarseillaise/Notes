from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import GUI
from GUI import AdditNoteWindow


class MainWindow:
    def __init__(self, search_func, download_func):
        self.company_list_in_window = None
        self.search = search_func
        self.download = download_func

        PURPLE = "#c2aed1"
        GREEN = "#84faac"
        BLUE = "#87CEEB"
        RED = "#FF3636"

        columns = ("name", "date")

        self.main_window = Tk()
        self.main_window.title("Notes")
        self.main_window.geometry('600x405')
        self.main_window.resizable(False, False)
        self.main_window["bg"] = PURPLE

        self.canvas = Canvas(self.main_window)
        self.canvas["bg"] = PURPLE
        self.canvas.grid(row=0, column=0, sticky='news')

        self.frame = Frame(self.canvas)
        self.frame["bg"] = PURPLE
        self.frame.grid(row=0, column=0, sticky='news')

        self.lbl = Label(self.frame, text="Поиск заметки:")
        self.lbl["bg"] = PURPLE
        self.lbl.grid(row=0, column=0, padx=(21, 1), pady=15, sticky='w')

        self.text = Entry(self.frame, width=60)
        self.text.grid(row=0, column=0, padx=(120, 1), pady=15, sticky='w', columnspan=2)

        self.button_search = Button(self.frame, text="Поиск", width=8, command=lambda: self.get_company())
        self.button_search.grid(row=0, column=1, padx=(1, 1), pady=15, sticky='e')

        self.table = ttk.Treeview(self.frame, height=14, columns=columns, show="headings")
        self.table.grid(row=1, column=0, columnspan=2, padx=(25, 1), pady=1)
        self.table.heading("name", text="Заголовок")
        self.table.column("name", width=400)
        self.table.heading("date", text="Дата создания")
        self.table.column("date", width=150)

        self.button_ok = Button(self.frame, text="Добавить", width=8, command=lambda: self.get_addit_window())
        self.button_ok["bg"] = GREEN
        self.button_ok.grid(row=2, column=1, padx=(1, 151), pady=5, sticky='e')

        self.button_edit = Button(self.frame, text="Изменить", width=8, command=lambda: self.download_company())
        self.button_edit["bg"] = BLUE
        self.button_edit.grid(row=2, column=1, padx=(1, 76), pady=5, sticky='e')

        self.button_del = Button(self.frame, text="Удалить", width=8, command=lambda: self.download_company())
        self.button_del["bg"] = RED
        self.button_del.grid(row=2, column=1, padx=(1, 2), pady=5, sticky='e')

        self.main_window.bind('<Return>', self.hit_return)  # hit Enter event

        self.main_window.mainloop()

    def get_company(self):
        for i in self.table.get_children():  # first clean the table if it almost has info
            self.table.delete(i)

        self.company_list_in_window = self.search(self.text.get())
        try:
            for company in self.company_list_in_window:
                self.table.insert(parent='', index='end', text='',
                                  values=(company.name, company.inn, company.adress))
        except TypeError:
            messagebox.showwarning("Внимание!", "Компаний с таким название не найдено")

    def download_company(self):
        focused = self.table.focus()
        inn_of_selected_company = self.table.item(focused, 'values')[1]
        for c in self.company_list_in_window:
            try:
                if c.inn == int(inn_of_selected_company):
                    self.download(c)
                    messagebox.showinfo("Успешно!", "Загрузка успешно завершена. Ты - молодец")
            except ValueError:
                raise ValueError("Похоже изменился порядок данных в столбцах в MainWinow")

    def get_addit_window(self):
        self.main_window.withdraw()
        AdditNoteWindow.Window(self.main_window)

    def hit_return(self, event=None):
        self.get_company()