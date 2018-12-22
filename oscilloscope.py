from Tkinter import Tk,Toplevel,Canvas,Scale,Label
from observer import *
from generator import *
from view import *
from controller import *
from menubar import * 
 
if  __name__ == "__main__" : 
    root=Tk()
    #root.option_readfile('fichier_options.txt')
    model=Generator()
    MonNom= Label(root,text="JALLOULI Khaled, k7jallou@enib.fr",foreground= "blue")
    MonNom.pack()
    menubar = Menubar(root,model)
    view=Screen(root)
    view.grid(8)
    view.update(model)
    model.attach(view)
    ctrl=Controller(model,view)
    view.packing()
    root.mainloop()
    
     
