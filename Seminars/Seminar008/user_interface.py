from tkinter import ttk
from tkinter import *
import tkinter as tk
import bd

class Dictionary:
    def __init__(self, window):

        self.wind = window
        self.wind.title('База данных')

        frame_add_form = tk.Frame(window)
        frame_input = tk.Frame(window)
        frame_list = tk.Frame(window, bg='blue')
        frame_add_form.grid(column=1, row=0,sticky='n')
        frame_input.grid(column=0, row=0)
        frame_list.grid(column=0, row=1, columnspan=2, sticky='we')

        ttk.Label(frame_input, text='ID').grid(row = 1, column = 1)
        input_id = ttk.Entry(frame_input)
        input_id.grid(row = 1, column = 2)
        ttk.Label(frame_input, text='Фирма').grid(row = 2, column = 1)
        input_firm = ttk.Entry(frame_input)
        input_firm.grid(row = 2, column = 2)
        ttk.Label(frame_input, text='Модель').grid(row = 3, column = 1)
        input_model = ttk.Entry(frame_input)
        input_model.grid(row = 3, column = 2)
        ttk.Label(frame_input, text='Разрешение').grid(row = 4, column=1)
        input_resol = ttk.Entry(frame_input)
        input_resol.grid(row = 4, column = 2)
        ttk.Label(frame_input, text='Размер').grid(row = 5, column=1)
        input_size = ttk.Entry(frame_input)
        input_size.grid(row = 5, column = 2)
        ttk.Label(frame_input, text='Стоимость').grid(row = 6, column=1)
        input_price = ttk.Entry(frame_input)
        input_price.grid(row = 6, column = 2)


        heads = ['ID','Фирма','Модель','Разрешение','Размер','Стоимость']
        table = ttk.Treeview(frame_list, show='headings')
        table['columns'] = heads

        for header in heads:
            table.heading(header, text = header, anchor=CENTER)
            table.column(header, anchor=CENTER)

        scroll_pane = ttk.Scrollbar(frame_list, command=table.yview)
        table.configure(yscrollcommand=scroll_pane.set)
        scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)

        table.pack(expand=tk.YES, fill=tk.BOTH)

        ttk.Button(frame_add_form, text = 'Загрузить', command= lambda: [data_in := self.load_table(), reload_table(data_in)]).grid(row = 1, columnspan = 2, sticky = W)
        ttk.Label(frame_add_form, text='Нажмите, чтобы загрузить БД').grid(row = 1, column = 2,sticky=W)
        def reload_table(data):
            table.delete(*table.get_children())
            for row in data:
                table.insert('',tk.END, values=row)

        ttk.Button(frame_add_form, text = 'Добавить', command= lambda: [data_all := input_data(),self.added_table(data_all),data_in := self.load_table(), reload_table(data_in)]).grid(row = 2, columnspan = 2, sticky = W)
        ttk.Label(frame_add_form, text='Введите элементы слева и нажмите, чтобы добавить').grid(row = 2, column = 2, sticky=W)
        def input_data():
            data = (input_firm.get(),input_model.get(),input_resol.get(),input_size.get(),input_price.get())
            return data

        ttk.Button(frame_add_form, text = 'Удалить', command= lambda: [id_del := input_id.get(),self.delete_elem(id_del),data_in := self.load_table(), reload_table(data_in)]).grid(row = 3, columnspan = 2, sticky = W)
        ttk.Label(frame_add_form, text='Введите ID элемента слева и нажмите, чтобы удалить').grid(row = 3, column = 2, sticky=W)
        ttk.Button(frame_add_form, text = 'Поиск', command= lambda: [data_in := bd.find_table(input_firm.get(),input_model.get(),input_resol.get(),input_size.get()), reload_table(data_in)]).grid(row = 4, columnspan = 2, sticky = W)
        ttk.Label(frame_add_form, text='Введите интересующие элементы слева и нажмите, чтобы найти').grid(row = 4, column = 2, sticky=W)
        

        ttk.Button(text = 'Выход', command=exit).grid(row = 5, column = 0, sticky = W + E, columnspan=2)

    def load_table(self):
        table = bd.read_table()
        return table

    def added_table(self, data):
        bd.added_element(data)

    def delete_elem(self, id_del):
        bd.delete_element(id_del)


if __name__ == '__main__':
    window = tk.Tk()
    application = Dictionary(window)
    window.mainloop()