class Controller :
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.view.get_magnitude().bind("<B1-Motion>",self.update_magnitude)
        self.view.get_frequency().bind("<B1-Motion>",self.update_frequency)
        self.view.get_phase().bind("<B1-Motion>",self.update_phase)


    def update_magnitude(self,event):
        print("update_magnitude")
        x=int(event.widget.get())
        self.model.set_magnitude(x)
        
    def update_frequency(self,event):
        print("update_frequency")
        x=int(event.widget.get())
        self.model.set_frequency(x)
        
    def update_phase(self,event):
        print("update_phase")
        x=int(event.widget.get())
        self.model.set_phase(x)
