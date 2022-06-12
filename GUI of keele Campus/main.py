# importing all the relevant packages
import tkinter.messagebox
from tkinter import *
import tkinter as gui
from tkinter import ttk
import csv

'''

>>> This a GUI representation of Keele university campus.
>>> This design displays all the required fundamentals of the project.
>>> Search anywhere you want to visit in Keele University by typing into the search box 
    and submit by Submit button/Enter Key on keyboard.
>>> Please select row of your desired location by single click plus select button or only double-click,
    and then click on show to reach that place in the university.
>>> Use exit button to exit from the GUI anytime you want.
>>> To implement this design,I have taken some syntax reference from a YT channel 'https://www.youtube.com/c/Codemycom'.
 
'''


class KeeleMapGUI:

    def __init__(self):
        self.textIn = StringVar()
        self.reference = []  # empty list for the values from csv
        self.count = 0

    @staticmethod
    def exit_program():  # exit function helps to exit from gui by popping message box
        result = tkinter.messagebox.askquestion("Exit", "Are You Sure You Want to Exit?")
        if result == "yes":
            exit()
        else:
            return

    @staticmethod
    def select_record():  # selects all the records from the selected row
        classify.delete(0, END)
        name.delete(0, END)
        num.delete(0, END)

        selected = my_tree.focus()

        values = my_tree.item(selected, 'values')
        if values:
            classify.insert(0, values[2])
            name.insert(0, values[0])
            num.insert(0, values[1])
        return values

    @staticmethod
    def clicker(e):  # event helper for to select the record by double click
        KeeleMapGUI.select_record()

    @staticmethod
    def display_message():  # displays the message to the place user wants to enter
        record = KeeleMapGUI.select_record()
        try:
            tkinter.messagebox.showinfo("Location",
                                        f'You are in {record[1]}, {record[0]}, {record[2]} in Keele University.\n')
            result = tkinter.messagebox.askquestion("Exit", "Do you want to continue the search?")
            if result == "yes":
                return
            else:
                exit()
        except IndexError:
            tkinter.messagebox.showinfo("Error", "No value has been selected!")

    @property
    def fetch_list(self):  # converts and return the data into a list of dictionary from the csv file
        with open("Appendix-A.csv", newline="") as f:
            reader = csv.DictReader(f)
            for i in reader:
                self.reference.append(i)
        return self.reference

    def refresh_input(self):  # this function help the refresh button to reset all the values from input and display box
        classify.delete(0, END)
        name.delete(0, END)
        num.delete(0, END)
        self.textIn.set("")
        for item in my_tree.get_children():
            my_tree.delete(item)

    def enter(self, e):  # event helper to submit the input using enter/return key on keyboard
        self.clk()

    def clk(self):  # this function helps to select and display the data from the provided input
        classify.delete(0, END)
        name.delete(0, END)
        num.delete(0, END)
        for item in my_tree.get_children():
            my_tree.delete(item)
        searched_item = ent.get()
        my_list = []
        for item in self.fetch_list:
            for v in item.values():
                if searched_item.lower().strip() in v.lower():
                    my_list.append(item)
        my_list = list({v["Name"]: v for v in my_list}.values())

        self.count = 0
        if len(my_list) == 0 or searched_item in [" " * item for item in range(0, 100)]:
            my_tree.insert(parent='', index='end', iid=str(self.count), text=str(self.count),
                           values=("No data", "No data", "No data"))
        else:
            for item in my_list:
                self.count += 1
                my_tree.insert(parent='', index='end', iid=str(self.count), text=str(self.count),
                               values=(item["Name"], item["Reference"], item["Classification"]))
        return my_tree


# GUI Implementation


root = gui.Tk()
root.title("Keele University Campus")
root.geometry("800x500")
root.maxsize(800, 500)
root.minsize(800, 500)
root.resizable(False, False)

img = PhotoImage(file="Map_image.png")  # background image insertion
label = Label(
    root,
    image=img
)
label.place(x=0, y=0)

style = ttk.Style(root)
# set ttk theme to "clam" which support the field background option
style.theme_use("clam")
style.configure("Treeview", background="black", border="black",
                fieldbackground="black", foreground="white")

my_scrollbar = Scrollbar(root, orient=VERTICAL)  # scrollbar for the tree display box
my_scrollbar.pack(side=RIGHT, fill=Y)
my_tree = ttk.Treeview(root, yscrollcommand=my_scrollbar.set, selectmode="browse")
my_tree.pack()

my_scrollbar.config(command=my_tree.yview)

my_tree['columns'] = ("Name", "Reference", 'Classification')  # providing column names for the resultant values
my_tree.column("#0", width=50, anchor=CENTER)
my_tree.column("Name", anchor=W, width=130)
my_tree.column("Reference", anchor=CENTER, width=130)
my_tree.column("Classification", anchor=CENTER, width=130)

my_tree.heading("#0", text="S. No.", anchor=CENTER)  # providing headings to the resultant values
my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("Reference", text="Reference", anchor=CENTER)
my_tree.heading("Classification", text="Classification", anchor=CENTER)

my_tree.pack(pady=20)
my_tree.place(relx=0.33, rely=0.6, anchor=CENTER)

lab = Label(root, text="Where do you want to visit?", font='none 14 bold', bg='light green', fg='blue')
lab.place(relx=0.15, rely=0.2, anchor=CENTER)

ent = Entry(root, width=20, font='none 18 bold', textvariable=KeeleMapGUI().textIn, bg='white', fg='black',
            insertbackground="black", insertwidth=2)
ent.place(relx=0.45, rely=0.2, anchor=CENTER)

# implementation of all the label in the UI
lab = Label(root, text="Classification", font='none 14 bold', bg='light green', fg='blue')
lab.place(relx=0.8, rely=0.35, anchor=CENTER)
classify = Entry(root, width=10, font='none 12 bold', bg='white', fg='black')
classify.place(relx=0.8, rely=0.4, anchor=CENTER)

lab = Label(root, text="Name", font='none 14 bold', bg='light green', fg='blue')
lab.place(relx=0.8, rely=0.5, anchor=CENTER)
name = Entry(root, width=10, font='none 12 bold', bg='white', fg='black')
name.place(relx=0.8, rely=0.55, anchor=CENTER)

lab = Label(root, text="Reference Number", font='none 14 bold', bg='light green', fg='blue')
lab.place(relx=0.8, rely=0.65, anchor=CENTER)
num = Entry(root, width=10, font='none 12 bold', bg='white', fg='black', justify="center")
num.place(relx=0.8, rely=0.7, anchor=CENTER)

# implementation of all the clickable button in UI
but = Button(root, width=4, padx=2, pady=2, text='Submit', command=KeeleMapGUI().clk, bg='blue', font='none 18 bold')
but.place(relx=0.37, rely=0.3, anchor=CENTER)

but = Button(root, width=4, padx=2, pady=2, text='Refresh', command=KeeleMapGUI().refresh_input, bg='blue', font='none '
                                                                                                                 '18 '
                                                                                                                 'bold')
but.place(relx=0.53, rely=0.3, anchor=CENTER)

but = Button(root, width=4, padx=2, pady=2, text='Show', command=KeeleMapGUI.display_message, bg='blue', font='none '
                                                                                                              '18 '
                                                                                                              'bold')
but.place(relx=0.8, rely=0.845, anchor=CENTER)

but = Button(root, width=4, padx=2, pady=2, text='Exit', command=KeeleMapGUI.exit_program, bg='blue', font='none 18 '
                                                                                                           'bold')
but.place(relx=0.45, rely=0.9, anchor=CENTER)

but = Button(root, width=4, padx=2, pady=2, text='Select', command=KeeleMapGUI.select_record, bg='blue', font='none '
                                                                                                              '18 '
                                                                                                              'bold')
but.place(relx=0.20, rely=0.9, anchor=CENTER)

# binding click and enter function
root.bind('<Return>', KeeleMapGUI().enter)
my_tree.bind("<Double-1>", KeeleMapGUI().clicker)
root.mainloop()
