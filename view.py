from Tkinter import Canvas,Scale,IntVar
from observer import *

class Screen(Observer):
    def __init__(self,parent,bg="white"):
        self.canvas=Canvas(parent,bg=bg)
        self.canvas.bind("<Configure>", self.resize)
        self.width=int(self.canvas.cget("width"))
        self.height=int(self.canvas.cget("height"))
        
        print("parent",parent.cget("width"),parent.cget("height"))
        
        self.magnitude=Scale(parent,length=250,orient="horizontal",
                         label="Magnitude", sliderlength=20,
                         showvalue=0,from_=0,to=10,
                         tickinterval=1,relief="sunken")
	
	self.frequency=Scale(parent,length=250,orient="horizontal",
                         label="Frequency", sliderlength=20,
                         showvalue=0,from_=0,to=10,
                         tickinterval=1,relief="sunken")
	
	self.phase=Scale(parent,length=250,orient="horizontal",
                         label="Phase", sliderlength=20,
                         showvalue=0,from_=0,to=10,
                         tickinterval=1,relief="sunken")
                          
                         
	
    def update(self,model):
        print("View update")
        signal=model.get_signal()
        self.plot_signal(signal)
        

    def get_magnitude(self):
        return self.magnitude
        
    def get_frequency(self):
        return self.frequency
      
    def get_phase(self):
	return self.phase
        
    def plot_signal(self,signal,color="red"):
        w,h=self.canvas.winfo_width(),self.canvas.winfo_height()
        width,height=int(w),int(h)
        print(self.canvas.find_withtag("signal"))
        if self.canvas.find_withtag("signal") :
            self.canvas.delete("signal")
        if signal and len(signal) > 1:
            plot = [(x*width, height/2.0*(y+1)) for (x, y) in signal]
            signal_id = self.canvas.create_line(plot, fill=color, smooth=1, width=3,tags="signal")
        return

    def grid(self, steps):
        w,h=self.canvas.cget("width"),self.canvas.cget("height")
        width,height=int(w),int(h)
 #       self.canvas.create_line(10,height/2,width,height/2,arrow="last")
 #       self.canvas.create_line(10,height-5,10,5,arrow="last")
        step=(width-10)/steps*1.
        for t in range(1,steps+2):
            x =t*step
            self.canvas.create_line(x,0,x,height)
            self.canvas.create_line(0,x,width,x)


    def packing(self) :
        self.canvas.pack()
        self.magnitude.pack()
        self.frequency.pack()
        self.phase.pack()
        self.canvas.pack(expand=1,fill="both",padx=6)
        self.magnitude.pack(expand=1,fill="x",padx=2)
        self.frequency.pack(expand=1,fill="x",padx=2)
        self.phase.pack(expand=1,fill="x",padx=2)


 
 
    def resize(self,event):
	wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        print("resize",wscale,hscale)
        # resize the canvas 
        #self.config(width=self.width, height=self.height)
	scale_xy= self.width*1.0/self.height     
	# rescale all the objects tagged with the "all" tag
        self.canvas.scale("all",0,0,wscale,hscale)
        

