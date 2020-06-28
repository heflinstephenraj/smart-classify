from tkinter  import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
from ibm_watson import VisualRecognitionV3 as vr
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from tkinterhtml import HtmlFrame

class MainApplication():
    def __init__(self, parent, *args, **kwargs):
            self.parent = parent
            parent.config(bg="red")
            about_app =  Label(parent,text='''This application is developed by Heflin Stephen Raj S to classify images and convert text document to speech and vice versa.\nContact the developer at www.heflin.dev''', fg ="white",bg="red")
            about_app["font"] = font.Font(family='Comic Sans MS', size = 15, weight='bold', underline=True)
            about_app.pack()
            s = ttk.Style()
            s.theme_create( "MyStyle", parent="alt", settings={"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },"TNotebook.Tab": {"configure": {"padding": [50, 10],"background": "sky blue","font" : ('Comic Sans MS', '13', 'bold')},"map":       {"background": [("selected", "white")]},}})
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
            tab1_info["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold')
            tab1_info.pack() 
            url = ttk.Entry(tab1)
            entry = ttk.Label(tab1,text="Enter the URL below")
            entry["font"] = font.Font(family='Comic Sans MS', size=12)
            classify_btn = Button(tab1,text = "Classify",  bg="yellow", command=lambda master=tab1: online_image_classify(master))
            entry.pack()
            url.pack()
            classify_btn["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
            ttk.Label(tab1).pack()
            classify_btn.pack()
            
            def online_image_classify(tab1):
                    vr_api = IAMAuthenticator("hMgDpMfCbeDZOIwAWwgTl3VUrZlEGVWqaAhftsZcjsuu") #paste your API Key
                    vr1=vr(version="2018-03-19",authenticator=vr_api)
                    vr1.set_service_url("https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/28c57a28-94d0-4837-a75b-73b89034f60d") #paste your service URL
                    try:

                        ibm_result=vr1.classify(url=url.get()).get_result()
                        empt = ttk.Label(tab1)
                        empt.pack()
                        result = ttk.Label(tab1,text= "Result")
                        clear_btm=Button(tab1,text="Clear result",bg="black",fg="white")
                        result["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold',underline = True )
                        result1='''<html><head></head><body><table style="width:100%" border="1"><tr><th><h2 style="color:red;font-family:Comic Sans MS">Classification</h2></th><th><h2 style="color:red;font-family:Comic Sans MS">Confident Score<h2></th></tr>'''
                        for i in range(len(ibm_result["images"][0]["classifiers"][0]["classes"])):
                                result1=result1+f'<tr><td><center><h3 style="color:blue;font-family:Comic Sans MS">{ibm_result["images"][0]["classifiers"][0]["classes"][i]["class"]}</h3> </center></td><td><center><h3 style="color:blue;font-family:Comic Sans MS"> {str(round(ibm_result["images"][0]["classifiers"][0]["classes"][i]["score"]*100))}%</h3> </center></td></tr>'
                        result1=result1+f'</table></body></html>'
                        frame = HtmlFrame(tab1,height=10)
                        frame.set_content(result1)
                        clear_btm["command"] = lambda one=result, two=clear_btm, three = empt, four=frame: clear(one,two,three,four)
                        clear_btm["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
                        clear_btm.pack()
                        result.pack()
                        frame.pack()

                        print(ibm_result)
                    except:
                        wrg=messagebox.showwarning(title="URL Error", message=f'''
Please enter the proper image URL to classify. 
The given URl is not a image URL.
The given URL is "{url.get()}".
''')
                    

            def clear(*widgets):
                    for widget in widgets:
                            widget.destroy()

if __name__ == "__main__":
    root = Tk()
    MainApplication(root)
    root.mainloop()
