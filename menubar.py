
from Tkinter import *
import  tkFileDialog,tkMessageBox
from observer import Observer
from generator import *
import csv

class Menubar(object):

    def __init__(self,parent,model):
        print("menubar __init__ ")
        self.model=model
        self.parent=parent
        
	menubar = Menu(parent)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Save as...", command=self.save)
	filemenu.add_command(label="Load", command=self.load)
	
	filemenu.add_separator()

	filemenu.add_command(label="Exit", command=self.exitt)
	menubar.add_cascade(label="File", menu=filemenu)
	editmenu = Menu(menubar, tearoff=0)
	editmenu.add_command(label="Undo", command=self.undo)

	editmenu.add_separator()

	#editmenu.add_command(label="Cut", command=self.cut)
	#editmenu.add_command(label="Copy", command=self.copy)
	#editmenu.add_command(label="Paste", command=self.paste)
	#editmenu.add_command(label="Delete", command=self.delete)
	#editmenu.add_command(label="Select All", command=self.selectall)

	#menubar.add_cascade(label="Edit", menu=editmenu)
	helpmenu = Menu(menubar, tearoff=0)
	helpmenu.add_command(label="About...", command=self.about)
	menubar.add_cascade(label="Help", menu=helpmenu)

	parent.config(menu=menubar)
	      
        
        
    def save(self):
    
        csvfile=tkFileDialog.asksaveasfile(mode="w",defaultextension=".csv",title="Save signal")
        w = csv.writer(csvfile,delimiter=";")
	w.writerow([str(self.model.get_magnitude()),str(self.model.get_frequency()) ,str(self.model.get_phase())])           
        csvfile.close()

    def exitt(self):
        tkMessageBox.askquestion("Quitter","are you sure !!",icon='warning')
        if 'yes' :
            self.parent.destroy();
        else :
            print "OK"
        

    def load(self):
      name= tkFileDialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
      csvfile=open(name,"r")      
      reader = csv.reader(csvfile, delimiter=';')
      for row in reader:
	self.model.set_magnitude(float(row[0]))
	self.model.set_frequency(float(row[1]))
	self.model.set_phase(float(row[2]))	

	print(row)
      csvfile.close()
      
      
        
    def packing(self):
        pass
    def cut(self):
	pass
    def copy(self):
	pass
    def paste(self):
	pass
    def delete(self):
	pass
    def selectall(self):
	pass
    def undo(self):
	pass
    def about(self):
	tkMessageBox.showinfo("Oscillo", "Si vous avez besoin d'aide")    
    
