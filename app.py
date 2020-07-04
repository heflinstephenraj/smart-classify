from tkinter  import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from tkinterhtml import HtmlFrame
from tkinter.filedialog import askopenfilename, asksaveasfilename
from ibm_watson import SpeechToTextV1 , TextToSpeechV1 , VisualRecognitionV3 as vr

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
                url_img_info = ttk.Label(tab1,text ='''We will send the image to IBM Watson Visual Recognition service for classification.\nWe do not save your images.\nInput: URL\nOutput: Classifications will be appeared on the screen with confident score for each classification.\n''',justify=CENTER)
                url_img_info["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold')
                url_img_info.pack() 
                url = ttk.Entry(tab1)
                entry = ttk.Label(tab1,text="Enter the URL below")
                entry["font"] = font.Font(family='Comic Sans MS', size=12)
                entry.pack()
                url.pack()
                classify_url_btn = Button(tab1,text = "Classify",  bg="yellow", command=lambda master=tab1,img_url=url: self.online_image_classify(master,url=img_url))
                classify_url_btn["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
                ttk.Label(tab1).pack()
                classify_url_btn.pack()
                ttk.Label(tab1).pack()
                loc_img_info = ttk.Label(tab2,text="We will send the image to IBM Watson Visual Recognition service for classification.\nWe do not save your images.\nInput: JPEG (.jpg) and PNG (.png) \nOutput: Classifications will be appeared on the screen with confident score for each classification.",justify=CENTER)
                loc_img_info["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold')
                loc_img_info.pack()
                ttk.Label(tab2).pack()
                classify_loc_btn = Button(tab2,text = "Classify",  bg="yellow", command=lambda master=tab2: self.local_image_classify(master))
                classify_loc_btn["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
                classify_loc_btn.pack()
                ttk.Label(tab2).pack()
                speech_2_text_info = ttk.Label(tab3,text="We will send the audio to IBM Watson Speech to Text service for classification.\nWe do not save your audio file.\nInput: MP3 (.mp3) \nOutput: Text will be displayed on your screen with confident score.",justify=CENTER)
                speech_2_text_info["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold')
                speech_2_text_info.pack()
                ttk.Label(tab3).pack()
                convert_sph_2_txt = Button(tab3,text = "Convert",  bg="yellow", command=lambda master=tab3: self.speech_to_text(master))
                convert_sph_2_txt["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
                convert_sph_2_txt.pack()
                ttk.Label(tab3).pack()
                text_2_speech_info = ttk.Label(tab4,text="We will send the text file to IBM Watson Text to Speech service for classification.\nWe do not save your text file.\nInput: Text file (.txt) \nOutput: Mp3 (.mp3)",justify=CENTER)
                text_2_speech_info["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold')
                text_2_speech_info.pack()
                ttk.Label(tab4).pack()
                convert_txt_2_sph = Button(tab4,text = "Convert",  bg="yellow", command=lambda master=tab4: self.text_to_speech(master))
                convert_txt_2_sph["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
                convert_txt_2_sph.pack()
                ttk.Label(tab4).pack()
            
                              
        def text_to_speech(self,master):
                def convert():
                        api_text_2_speech = IAMAuthenticator("api-key")
                        text_2_speech = TextToSpeechV1(authenticator=api_text_2_speech)
                        text_2_speech.set_service_url("service-url")
                        if var.get() == "male voice":
                                audio_result = asksaveasfilename(defaultextension=".mp3",filetypes=[("mp3 file","*.mp3")])
                                with open(audio_result,"wb") as audio:
                                        audio.write(text_2_speech.synthesize(text,accept="audio/mp3",voice="en-US_HenryV3Voice").get_result().content)
                                        audio.close()
                                messagebox.showinfo("Done","Your text file is successfully converted into audio file. Your audio file saved in male voice at " + audio_result)
                        elif var.get() == "female voice":
                                audio_result = asksaveasfilename(defaultextension=".mp3",filetypes=[("mp3 file","*.MP3")])
                                with open(audio_result,"wb") as audio:
                                        audio.write(text_2_speech.synthesize(text,accept="audio/mp3",voice="en-US_AllisonVoice").get_result().content)
                                        audio.close()
                                messagebox.showinfo("Done","Your text file is successfully converted into audio file. Your audio file is saved in female voice at " + audio_result)
                                
                        else:
                                messagebox.showwarning(title="Voice Error", message=f'''Please select the voice and save again.''')
                                
                def sel():
                        selection = "Your audio will be saved in " + str(var.get())
                        label.config(text = selection)
                text_file = askopenfilename(filetypes=[("text file","*.txt")])
                with open(text_file) as text_data:
                        text = text_data.read()
                text_html = f'''<html><head></head><body><p>{text}</p></body><html>'''
                result_loc = ttk.Label(master,text= "The Text")
                clear_loc_btm=Button(master,text="Clear",bg="black",fg="white")
                result_loc["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold',underline = True )
                frame_loc = HtmlFrame(master,horizontal_scrollbar="auto",vertical_scrollbar="auto")
                frame_loc.set_content(text_html)
                clear_loc_btm["font"] = font.Font(family='Comic Sans MS', size=12,weight='bold')
                var = StringVar()
                R1 = Radiobutton(master, text="Save as male voice", variable=var, value="male voice",command=sel)
                R1["font"] = font.Font(family='Comic Sans MS', size=11)
                R1.pack()
                R2 = Radiobutton(master, text="Save as female voice", variable=var, value="female voice",command=sel)
                R2["font"] = font.Font(family='Comic Sans MS', size=11)
                R2.pack() 
                label = ttk.Label(master)
                label["font"] = font.Font(family='Comic Sans MS', size=11)
                label.pack()
                save_audio = Button(master,text="Save",bg="blue",fg="white",command=convert)
                save_audio["font"] = font.Font(family='Comic Sans MS', size=11, weight='bold')
                save_audio.pack()
                em = ttk.Label(master)
                em.pack()
                clear_loc_btm["command"] = lambda one=result_loc, two=clear_loc_btm, three=frame_loc, four=R1, five=R2, six=label, seven = save_audio,egith = em: self.clear(one,two,three,four,five,six,seven,egith)
                clear_loc_btm.pack()
                result_loc.pack()
                frame_loc.pack(fill="x")


                

        def speech_to_text(self,master):
                speech_to_text_api = IAMAuthenticator('api-key')
                speech_to_text = SpeechToTextV1(authenticator=speech_to_text_api)
                speech_to_text.set_service_url('service-url')
                audio = askopenfilename(filetypes=[("mp3 file","*.mp3")])
                with open(audio,"rb") as audio_file:
                        speech_to_text_results = speech_to_text.recognize(audio=audio_file,content_type='audio/mp3').get_result()
                result_s_2_t='''<html><head></head><body><table style="width:100%" border="1"><tr><th><h3 style="color:red;font-family:Comic Sans MS">Classification</h3></th><th><h3 style="color:red;font-family:Comic Sans MS">Confident\nScore<h3></th></tr>'''
                for result in speech_to_text_results["results"]:
                        for classification in result:
                                if classification != "final":
                                        result_s_2_t=result_s_2_t+f'<tr><td><center><h3 style="color:blue;font-family:Comic Sans MS">{result[classification][0]["transcript"]}</h3> </center></td><td><center><h3 style="color:blue;font-family:Comic Sans MS"> {str(round(result[classification][0]["confidence"]*100))}%</h3> </center></td></tr>'
                result_s_2_t=result_s_2_t+f'</table></body></html>'
                result_loc = ttk.Label(master,text= "Result")
                clear_loc_btm=Button(master,text="Clear result",bg="black",fg="white")
                result_loc["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold',underline = True )
                frame_loc = HtmlFrame(master,horizontal_scrollbar="auto",vertical_scrollbar="auto")
                frame_loc.set_content(result_s_2_t)
                clear_loc_btm["command"] = lambda one=result_loc, two=clear_loc_btm, three=frame_loc: self.clear(one,two,three)
                clear_loc_btm["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
                clear_loc_btm.pack()
                result_loc.pack()
                frame_loc.pack(fill="x")





        def local_image_classify(self,tab2):
                img_file = askopenfilename(filetypes=[("Image files",("*.png","*.jpeg","*.jpg"))])                   
                vr_api = IAMAuthenticator("api-key") #paste your API Key
                vr1=vr(version="2018-03-19",authenticator=vr_api)
                vr1.set_service_url("service-url") #paste your service URL
                with open(img_file,"rb") as img:
                        loc_img_result=vr1.classify(images_file=img).get_result()
                result_loc = ttk.Label(tab2,text= "Result")
                clear_loc_btm=Button(tab2,text="Clear result",bg="black",fg="white")
                result_loc["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold',underline = True )
                result_loc1='''<html><head></head><body><table style="width:100%" border="1"><tr><th><h2 style="color:red;font-family:Comic Sans MS">Classification</h2></th><th><h2 style="color:red;font-family:Comic Sans MS">Confident Score<h2></th></tr>'''
                for i in range(len(loc_img_result["images"][0]["classifiers"][0]["classes"])):
                        result_loc1=result_loc1+f'<tr><td><center><h3 style="color:blue;font-family:Comic Sans MS">{loc_img_result["images"][0]["classifiers"][0]["classes"][i]["class"]}</h3> </center></td><td><center><h3 style="color:blue;font-family:Comic Sans MS"> {str(round(loc_img_result["images"][0]["classifiers"][0]["classes"][i]["score"]*100))}%</h3> </center></td></tr>'
                result_loc1=result_loc1+f'</table></body></html>'
                frame_loc = HtmlFrame(tab2,horizontal_scrollbar="auto",vertical_scrollbar="auto")
                frame_loc.set_content(result_loc1)
                clear_loc_btm["command"] = lambda one=result_loc, two=clear_loc_btm, three=frame_loc: self.clear(one,two,three)
                clear_loc_btm["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
                clear_loc_btm.pack()
                result_loc.pack()
                frame_loc.pack()

            

        def online_image_classify(self,tab1,url):
                vr_api = IAMAuthenticator("api-key") #paste your API Key
                vr1=vr(version="2018-03-19",authenticator=vr_api)
                vr1.set_service_url("service-url") #paste your service URL
                try:
                        ibm_result=vr1.classify(url=url.get()).get_result()
                        result = ttk.Label(tab1,text= "Result")
                        clear_btm=Button(tab1,text="Clear result",bg="black",fg="white")
                        result["font"] = font.Font(family='Comic Sans MS', size=15, weight='bold',underline = True )
                        result1='''<html><head></head><body><table style="width:100%" border="1"><tr><th><h2 style="color:red;font-family:Comic Sans MS">Classification</h2></th><th><h2 style="color:red;font-family:Comic Sans MS">Confident Score<h2></th></tr>'''
                        for i in range(len(ibm_result["images"][0]["classifiers"][0]["classes"])):
                                result1=result1+f'<tr><td><center><h3 style="color:blue;font-family:Comic Sans MS">{ibm_result["images"][0]["classifiers"][0]["classes"][i]["class"]}</h3> </center></td><td><center><h3 style="color:blue;font-family:Comic Sans MS"> {str(round(ibm_result["images"][0]["classifiers"][0]["classes"][i]["score"]*100))}%</h3> </center></td></tr>'
                        result1=result1+f'</table></body></html>'
                        frame = HtmlFrame(tab1,horizontal_scrollbar="auto",vertical_scrollbar="auto")
                        frame.set_content(result1)
                        clear_btm["command"] = lambda one=result, two=clear_btm, three=frame: self.clear(one,two,three)
                        clear_btm["font"] = font.Font(family='Comic Sans MS', size=10,weight='bold')
                        clear_btm.pack()
                        result.pack()
                        frame.pack()
                except:
                        messagebox.showwarning(title="URL Error", message=f'''Please enter the proper image URL to classify.\nThe given URl is not a image URL.\nThe given URL is "{url.get()}".''')
                    

        def clear(self,*widgets):
                for widget in widgets:
                        widget.destroy()

if __name__ == "__main__":
    root = Tk()
    MainApplication(root)
    root.mainloop()
