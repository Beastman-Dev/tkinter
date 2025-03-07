from tkinter import *
import tkinter as tk


class ToDoItem:

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description


class ToDoListApp:

    def __init__(self, root):

        root.title("To Do List")

        frame = Frame(root, borderwidth=3, relief="sunken")
        frame.grid(column=1, row=1, sticky=(N, E, S, W))
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        list_label = Label(frame, text="To Do Items")
        list_label.grid(column=1, row=1, sticky=(S, W))

        self.to_do_items = [
            ToDoItem("Item 1", "Description 1"),
            ToDoItem("Item 2", "Description 2"),
            ToDoItem("Item 3", "Description 3"),
            ToDoItem("Item 4", "Description 4")
        ]
        self.to_do_names = StringVar(value=list(map(lambda x: x.name, self.to_do_items)))
        items_list = Listbox(frame, listvariable=self.to_do_names)
        items_list.bind("<<ListboxSelect>>", lambda s: self.select_item(items_list.curselection()))
        items_list.grid(column=1, row=2, sticky=(E, W))

        self.selected_description = StringVar()
        selected_description_label = Label(frame, textvariable=self.selected_description)
        selected_description_label.grid(column=1, row=3, sticky=(E, W))

        self.label_text = StringVar()
        label = Label(frame, text="Some label text", textvariable=self.label_text)
        # label.grid(column=1, row=1)
        # Then we draw the widgets to the window

        # Modifying existing widgets can be done one attribute at a time with the dictionary method        
        # label["text"] = "New text"
        label["font"] = ("Arial", 28)

        self.entry_text = StringVar()
        entry = Entry(frame, textvariable=self.entry_text)

        button = Button(frame, text="Button text", command=self.press_button)
        # button.grid(column=1, row=2, sticky=(N, S, E, W))
        # button.configure(width=10, height=2, font=("Arial", 18))


    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)

    def select_item(self, index):
        selected_item = self.to_do_items[index[0]]
        self.selected_description.set(selected_item.description)

root = Tk()
ToDoListApp(root)
root.mainloop()

