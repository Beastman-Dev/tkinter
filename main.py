from tkinter import *
import tkinter as tk

class ToDoListApp:

    def __init__(self, root):

        root.title("To Do List")

        frame = Frame(root, borderwidth=3, relief="sunken")
        frame.grid(column=1, row=1, sticky=(N, E, S, W))
        root.columnconfigure(1, weight=1)

        self.label_text = StringVar()
        label = Label(root, text="Some label text", textvariable=self.label_text)
        # label.grid(column=1, row=1)
        # Then we draw the widgets to the window
        # label.pack(side=tk.LEFT)

        # Modifying existing widgets can be done one attribute at a time with the dictionary method        
        # label["text"] = "New text"
        label["font"] = ("Arial", 28)

        # Multiple widget attributes may be modified with the configure method
        #label.configure(text="Yet more text", font=(("Courier", 28)))

        # Creating a text entry field
        # Binding the entry by type (e.g. StringVar) to a variable (entry_text)
        self.entry_text = StringVar()
        # Create the widget instance from the "Entry" class, bound to a different variable (entry)
        entry = Entry(root, textvariable=self.entry_text)
        # Draw the widget to the window
        # entry.pack(side=tk.LEFT)
        # entry.place(x=100, y=50)
        # entry.grid(column=3, row=1)

        # Use the dictionary method of updating widget properties to bind the entry value to the widget
        # label["textvariable"] = entry_text

        #entry_text.set("Set text manually")

        button = Button(root, text="Button text", command=self.press_button)
        # button.pack(side=tk.LEFT)
        # button.grid(column=1, row=2, sticky=(N, S, E, W))
        # button.place(x=0, y=0)
        # button.configure(width=10, height=2, font=("Arial", 18))

        self.list_item_strings = ["Hey", "Hi", "Hello", "Howdy", "Greetings"]
        list_items = StringVar(value=self.list_item_strings)
        listbox = Listbox(root, listvariable=list_items)
        # listbox.pack(side=tk.LEFT, padx=40, pady=20)
        listbox["height"] = 5
        listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection()))
        # This is some arbitrary stuff, so just have to remember or use reference materials
        # The listbox.bind method binds the item selected in a listbox and allows it to be called - in this case from the 'select_item' function
        # listbox.grid(column=3, row=2)

    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)

    def select_item(self, index):
        selected_item = self.list_item_strings[index[0]]
        print(selected_item)

root = Tk()
ToDoListApp(root)
root.mainloop()

