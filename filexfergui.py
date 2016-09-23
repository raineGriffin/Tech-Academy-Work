from Tkinter import *
from ttk import *
import filexfer
import tkFileDialog
import sqlite3

class Transfertool:

    def reader(self):
        for row in self.c.execute(self.lastDate): self.strdate.set("Last check was on " + str(row))

    def __init__(self, root):

        self.conn = sqlite3.connect('xfertimes.db')
        self.c = self.conn.cursor()

        root.resizable(False, False)

        self.c.execute("CREATE TABLE IF NOT EXISTS cTimes(ID INT, date TEXT, checktime REAL)")

        self.lastDate = "SELECT date FROM cTimes GROUP BY date HAVING MAX(checktime)"

        self.strdate = StringVar()

        self.reader()

        self.frame1 = Frame(root, width = 256, height = 128, padding = 10)
        self.frame2 = Frame(root, width = 256, height = 128, padding = 10)

        self.frame1.grid(row = 1, column = 0, rowspan = 2, columnspan = 2)
        self.frame2.grid(row = 4, column = 0, rowspan = 2, columnspan = 2)

        label_header = Label(root, text = "File Transfer Tool").grid(row=0,column=0,columnspan=2)

        label_from = Label(self.frame1, text = "Choose the folder to be scanned for movable files.")
        label_from.grid(row=1,column=0, columnspan=2)

        self.filestring1 = StringVar()
        self.filloc1 = Entry(self.frame1, width = 50, textvariable = self.filestring1)
        self.filloc1.grid(row = 2, column = 0, columnspan = 2)

        browse1 = Button(self.frame1, text = "Browse", command = lambda: self.Openfilepath(self.filloc1))
        browse1.grid(row = 3, column = 0,pady=5, columnspan=2)

        label_to = Label(self.frame2, text = "Choose the folder that the files are to go to.")
        label_to.grid(row=4,column=0,pady=5, columnspan=2)

        self.filestring2 = StringVar()
        self.filloc2 = Entry(self.frame2, width = 50, textvariable = self.filestring2)
        self.filloc2.grid(row = 5, column = 0, columnspan = 2)

        browse2 = Button(self.frame2, text = "Browse", command = lambda: self.Openfilepath(self.filloc2))
        browse2.grid(row =6, column = 0,pady=5, columnspan=2)

        self.lastCheck = Label(root, textvariable = self.strdate)
        self.lastCheck.grid(row = 9, column = 0, pady=5, columnspan=2)

        commit = Button(root, text = "Commit Transfer", command = self.Commit)
        commit.grid(row=10, column=0, columnspan=2, pady=15)

    def Openfilepath(self,filloc):
        self.path = tkFileDialog.askdirectory()
        filloc.delete(0, END)
        filloc.insert(0, self.path)

    def Commit(self):
        filexfer.checkMTime(self.filloc1.get(),self.filloc2.get(),self.conn)
        self.reader()
        
        
        

def main():

    root = Tk()
    transfertool = Transfertool(root)
    root.mainloop()

if __name__ == "__main__": main()
