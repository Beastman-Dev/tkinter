from tkinter import *


class MyApp:

    def __init__(self, root):

        # Configuring parameters of the window
        root.title("My First Tkinter App")
        root.maxsize(800, 600)
        root.geometry("640x480")

        # Creating widgets - in this case text widgets
        # First we define the widgets
        self.label_text = StringVar()
        label = Label(root, text="Some label text", textvariable=self.label_text)
        # Then we draw the widgets to the window
        label.pack()

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
        entry.pack()

        # Use the dictionary method of updating widget properties to bind the entry value to the widget
        # label["textvariable"] = entry_text

        #entry_text.set("Set text manually")

        button = Button(root, text="Button text", command=self.press_button)
        button.pack()

        self.list_item_strings = ["Hey", "Hi", "Hello", "Howdy", "Greetings"]
        list_items = StringVar(value=self.list_item_strings)
        listbox = Listbox(root, listvariable=list_items)
        listbox.pack()
        listbox["height"] = 5
        listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection()))
        # This is some arbitrary stuff, so just have to remember or use reference materials
        # The listbox.bind method binds the item selected in a listbox and allows it to be called - in this case from the 'select_item' function

    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)

    def select_item(self, index):
        selected_item = self.list_item_strings[index[0]]
        print(selected_item)

root = Tk()
MyApp(root)
root.mainloop()

