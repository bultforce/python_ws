import os
# os.system("gnome-terminal -e 'bash -c \"sudo snap install curl; curl https://app.staging.workstatus.io/workstatus_1.7.1_amd64.snap -o workstatus.snap; sudo snap install workstatus.snap --devmode; rm workstatus.snap; workstatus exec bash\"'")

#Import the required library
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
#Create an instance of tkinter window
win= Tk()
win.title("Workstatus")
#Define the geometry of the window
win.geometry("750x650")
#Load the image
# bg= ImageTk.PhotoImage(file="./dot_W.png", size=)
#Create a canvas
canvas= Canvas(win,width= 100, height= 100)
canvas.pack(expand=False, padx= 170, pady=170)
# img= (Image.open("download.png"))
#Add the image in the canvas

img= (Image.open("./dot_W.png"))
resized_image= img.resize((90,90), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
#Add a text in canvas
canvas.create_image(10,10, anchor=NW, image=new_image)

def installWs():
     
     os.system("gnome-terminal -e 'bash -c \"sudo snap install curl; curl https://app.staging.workstatus.io/workstatus_1.7.1_amd64.snap -o workstatus.snap; sudo snap install workstatus.snap --devmode; rm workstatus.snap; workstatus exec bash\"'")
     win.destroy()


btn = Button(win, text = 'Install Workstatus!', bd = '5',
                          command = installWs)
 
# Set the position of button on the top of window.  
btn.pack(side = 'top')



win.mainloop()