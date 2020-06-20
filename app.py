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
        self.about_app["font"] = font.Font(family='Comic Sans MS', size = 15, weight='bold', underline=True)
        self.about_app.pack()
        s = ttk.Style()
        s.theme_create( "MyStyle", parent="alt", settings={"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },"TNotebook.Tab": {"configure": {"padding": [50, 10],"font" : ('Comic Sans MS', '13', 'bold')},}})
        s.theme_use("MyStyle")
        parent.title("Tab Widget")         
        tabControl =  ttk.Notebook(parent)
        tab1 = ttk.Frame(tabControl) 
        tab2 = ttk.Frame(tabControl) 
        tabControl.add(tab1, text ='Online Imgae Classification')
        tab3 = ttk.Frame(tabControl) 
        tabControl.add(tab3, text ='Speech to Text') 
        tab4 = ttk.Frame(tabControl)
        tabControl.add(tab4, text ='Text to Speech')
        tabControl.add(tab2, text ='Local Image Classification') 
        tabControl.pack(expand = 1, fill ="both") 
        tab1_info = ttk.Label(tab1,text ='''We will send the image to IBM Watson Visual Recognition service for classification.\nWe do not save your images.\nInput: URL\nOutput: Classifications will be appeared on the screen with confident score for each classification.\n''',justify=CENTER)
        #tab1_info.configure(anchor=CENTER)
        tab1_info["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold')
        tab1_info.pack() 
        ttk.Label(tab2, text ="Go").pack()
        url = Entry(tab1)
        entry = Label(tab1,text="Enter the URL below")
        entry["font"] = font.Font(family='Comic Sans MS', size=10)
        classify_btn = Button(tab1,text = "Classify", command = online_image_classify, bg="yellow")
        entry.pack()
        url.pack()
        classify_btn["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
       # empty_line(tab1)
        Label(tab1,text="").pack()
        classify_btn.pack()
        result = Label(tab1,text= "Result",pady=10)
        result["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold')
        result.pack()

def empty_line(master):
        line = Label(master)
        return line.pack()

def online_image_classify():
        print('hello')
      

if __name__ == "__main__":
    root = Tk()
    MainApplication(root)
    root.mainloop()
