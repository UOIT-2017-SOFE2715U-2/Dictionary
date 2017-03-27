from Tkinter import *
from dictionary_class import *


class Application(Frame):

    __dictionary = dictionary()

    def search(self):
        #self.__dictionary.print_definition(self.Word.get())
        result = self.__dictionary.search(self.Word.get())
        if not result:
            return ""
        else:
            self.Definition.delete("1.0", "end")
            i = 0
            for r in result:
                i += 1
                self.Definition.insert('end',str(i) + "\t" + r + "\n")

    def add(self):
        self.__dictionary.add(self.Word.get(), self.Definition.get('1.0', 'end'))

    def delete(self):
        self.__dictionary.delete(self.Word.get())
    def edit(self):
        self.__dictionary.edit(self.Word.get(), 0, self.Definition.get('1.0', 'end'))




    def createWidgets(self):
        self.EntryLabel = Label(self,text="Word")
        self.EntryLabel.pack(side=TOP)

        self.Word = Entry(self)
        self.Word.pack(side=TOP)

        self.Definition = Text(self)
        self.Definition.pack(side=BOTTOM)


        self.SEARCH = Button(self)
        self.SEARCH["text"] = "SEARCH"
        self.SEARCH["command"] = self.search
        self.SEARCH.pack(side=BOTTOM)

        self.ADD = Button(self)
        self.ADD["text"] = "ADD"
        self.ADD["command"] = self.add
        self.ADD.pack(side=BOTTOM)

        self.DELETE = Button(self)
        self.DELETE["text"] = "DELETE"
        self.DELETE["command"] = self.delete
        self.DELETE.pack(side=BOTTOM)

        self.EDIT = Button(self)
        self.EDIT["text"] = "EDIT"
        self.EDIT["command"] = self.edit
        self.EDIT.pack(side=BOTTOM)


        '''
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        '''
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()