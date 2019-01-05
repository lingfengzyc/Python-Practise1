from tkinter import *
from backend import Database

database=Database("books.db")

class Labels:

    def __init__(self):

        self.l1=Label(window,text="Title")
        self.l2=Label(window,text="Author")
        self.l3=Label(window,text="Year")
        self.l4=Label(window,text="ISBN")

    def grid_labels(self):

        self.l1.grid(row=0,column=0)
        self.l2.grid(row=0,column=2)
        self.l3.grid(row=1,column=0)
        self.l4.grid(row=1,column=2)

class Buttons:

    def __init__(self):
        self.b1=Button(window,text="View all",width=12,command=self.view_command)
        self.b2=Button(window,text="Search entry",width=12,command=self.search_command)
        self.b3=Button(window,text="Add entry",width=12,command=self.add_command)
        self.b4=Button(window,text="Update",width=12,command=self.update_command)
        self.b5=Button(window,text="Delete",width=12,command=self.delete_command)
        self.b6=Button(window,text="Close",width=12,command=window.destroy)

    def grid_buttons(self):
        self.b1.grid(row=2,column=3)
        self.b2.grid(row=3,column=3)
        self.b3.grid(row=4,column=3)
        self.b4.grid(row=5,column=3)
        self.b5.grid(row=6,column=3)
        self.b6.grid(row=7,column=3)

    def view_command(self):
        list1.delete(0,END)
        for row in database.view():
            list1.insert(END,row)

    def search_command(self):
        list1.delete(0,END)
        for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
            list1.insert(END,row)

    def add_command(self):
        database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        list1.delete(0,END)
        list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

    def delete_command(self):
        database.delete(selected_tuple[0])

    def update_command(self):
        database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())




class TextEntry:

    def __init__(self):

        self.title_text=StringVar()
        self.e1=Entry(window,textvariable=self.title_text)
        self.author_text=StringVar()
        self.e2=Entry(window,textvariable=self.author_text)
        self.year_text=StringVar()
        self.e3=Entry(window,textvariable=self.year_text)
        self.isbn_text=StringVar()
        self.e4=Entry(window,textvariable=self.isbn_text)

    def grid_text(self):
        self.e1.grid(row=0,column=1)
        self.e2.grid(row=0,column=3)
        self.e3.grid(row=1,column=1)
        self.e4.grid(row=1,column=3)





class BooksList:
    def __init__(self):

        self.list1=Listbox(window,height=6,width=35)
        self.sb1=Scrollbar(window)

    def grid_list_scrollbar(self):
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)
        self.sb1.grid(row=2,column=2,rowspan=6)

    def setup_list_scrollbar(self):

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)
        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

    def get_selected_row(self,event):
        try:
            global selected_tuple
            self.index=list1.curselection()[0]
            self.selected_tuple=list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,selected_tuple[4])
        except IndexError:
            pass


window=Tk()

window.wm_title("BookStore")
text = TextEntry()
label = Labels()
button = Buttons()
bookslist = BooksList()

text.grid_text()
label.grid_labels()
button.grid_buttons()
bookslist.grid_list_scrollbar()

bookslist.setup_list_scrollbar()

window.mainloop()
