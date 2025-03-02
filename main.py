from tkinter import *


class MyApp:

    def __init__(self, root):

        # Configuring parameters of the window
        root.title("My First Tkinter App")
        root.geometry("640x480")
        root.maxsize(1000, 800)

        # Creating widgets - in this case text widgets
        # First we define the widgets
        label = Label(root, text="Some label text")
        # Then we draw the widgets to the window
        label.pack()

        # Modifying existing widgets can be done one attribute at a time with the dictionary method        
        # label["text"] = "New text"
        label["font"] = ("Arial", 32)

        # Multiple widget attributes may be modified with the configure method
        #label.configure(text="Yet more text", font=(("Courier", 28)))

        # Creating a text entry field
        # Binding the entry by type (e.g. StringVar) to a variable (entry_text)
        entry_text = StringVar()
        # Create the widget instance from the "Entry" class, bound to a different variable (entry)
        entry = Entry(root, textvariable=entry_text)
        # Draw the widget to the window
        entry.pack()

        # Use the dictionary method of updating widget properties to bind the entry value to the widget
        label["textvariable"] = entry_text

        #entry_text.set("Set text manually")



root = Tk()
MyApp(root)
root.mainloop()

