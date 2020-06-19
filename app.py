from tkinter  import *
from tkinter import ttk
import tkinter.font as font

class MainApplication():
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        parent.config(bg="red")
        self.about_app =  Label(parent,text='''
This application is developed by Heflin Stephen Raj S to classify images and convert text document to speech and vice versa.
contact the developer at www.heflin.dev
''', fg ="white",bg="red")
        self.about_app["font"] = font.Font(family='Comic Sans MS',  weight='bold', underline=True)
        self.about_app.pack()
        s = ttk.Style()
        s.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [50, 10],
                                        "font" : ('Comic Sans MS', '13', 'bold')},}})
        s.theme_use("MyStyle")
        parent.title("Tab Widget")         
      #  ttk.Style().configure("TNotebook", background="White")
        tabControl =  ttk.Notebook(parent)
        tab1 = ttk.Frame(tabControl,relief = 'sunken') 
        tab2 = ttk.Frame(tabControl,relief = 'sunken') 
        tabControl.add(tab1, text ='Online Imgae Classification')
        tab3 = ttk.Frame(tabControl,relief = 'sunken') 
        tabControl.add(tab3, text ='Speech to Text') 
        tab4 = ttk.Frame(tabControl,relief = 'sunken')
        tabControl.add(tab4, text ='Text to Speech')
        tabControl.add(tab2, text ='Local Image Classification') 
        tabControl.pack(expand = 1, fill ="both") 
        ttk.Label(tab1,  
          text ="Welcome").grid(column = 0,  
                               row = 0, 
                               padx = 30, 
                               pady = 30)   
        ttk.Label(tab2, 
          text ="Go").grid(column = 0, 
                                    row = 0,  
                                    padx = 30, 
                                    pady = 30)
        

      

if __name__ == "__main__":
    root = Tk()
    MainApplication(root)
    root.mainloop()
