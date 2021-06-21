"""
Author: NANASAHEB, YADAV
Date: 21/06/2021
Description: It's simple code to check the host is online or offline, its designed to test hundreds of hosts at a time.

"""

import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
from tkinter import filedialog
import sys
import os
import subprocess

#constants
HEIGHT = 500
WIDTH = 600
copyright_symbol = u"\u00A9"
stop = True

root = tk.Tk()

root.title("IP Check Tool")
#root.iconphoto(True, PhotoImage(file="./sb.png"))  #C:/Users/nana/Desktop
root.resizable(0, 0)

#variable declare for IP input
IpInput = StringVar()

#main canvas
canvas = tk.Canvas(root, height= HEIGHT, width= WIDTH)
canvas.pack()

#main frame
frame = tk.Frame(canvas, borderwidth=3, relief="ridge")
frame.place(relx=0.01, rely= 0.01, relwidth = 0.98, relheight= 0.13 )

def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)
    global fname
    fname = pathlabel["text"]
    print(fname)

#function to close the window
def close_window ():
    root.destroy()

#function to clear text the window
def cleartextbox ():
    inputtext.delete("1.0",END)
    outputtext.delete("1.0",END)


#Ip status checking for the manual endpoints entred in text area
def ip_status():
    pingbutton1.configure(state=DISABLED)
    stopbutton.configure(state=NORMAL)
    endpoint = inputtext.get("1.0",END)
    endpointList = endpoint.split()
    global stop

    for ip in endpointList:
        if stop == True:
            root.update()
            response = subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],shell = True).wait() #["ping", "-n", "1", "-w", "200", ip]
            if response == 0:
                ipdict = {ip: "UP"}
                outputtext.insert(INSERT,str(ipdict).strip('{}'))
                outputtext.insert(INSERT,"\n")
            else:
                ipdict = {ip: "DOWN"}
                outputtext.insert(INSERT,str(ipdict).strip('{}'))
                outputtext.insert(INSERT,"\n")
            ipdict.clear()
        else:
            stop = True
            break
    pingbutton1.configure(state=NORMAL)

def stop_ping():
    global stop
    pingbutton1.configure(state=NORMAL)
    stopbutton.configure(state=DISABLED)
    stop = False

namelabel = tk.Label(frame, borderwidth=3,relief="groove", text= "Check IP/DNS hostname status ", fg= "#008000", font=("Italic", 12))
namelabel.place(x=125, rely=0.3,relwidth= 0.6)

#browse button to load file to ping ip/dns name
#browsebutton = Button(frame, text="Browse File", bg="#cccccc", command=browsefunc)
#browsebutton.place(x=10,y=28)

#pathlabel it shows label path on
#pathlabel = Label(frame,font=("Helvetica", 10))
#pathlabel.place(x=90, y=29,relwidth = 0.64, relheight= 0.40)

#ping  button to start ping ip/dns name for file input
#pingbutton = Button(frame, text="Start Ping", bg="#cccccc", command=browsefunc)
#pingbutton.place(relx = 0.8, y = 28, relwidth= 0.19)

#input frame left hand middle frame
inputframe = tk.Frame(canvas, borderwidth=3, relief="ridge")
inputframe.place(relx=0.01, rely= 0.15, relwidth = 0.49, relheight= 0.7 )

#input IP/DNS entry label. it shows label to enter ip /dns hostname
inputlabel = tk.Label(inputframe,text= "Enter IP/DNS hostnames", font=("Helvetica", 10), bg= "#ffebe6")
inputlabel.place(relx=0.0, rely=0.0,relwidth = 1.0, relheight= 0.07)

#IP/DNS input text box field to enter dns and IPs
inputtext = tk.Text(inputframe)
inputtext.place(relx = 0.0, rely= 0.08, relwidth = 1.0, relheight = 0.92)

#output frame i.e. right hand middle side.
outputframe = tk.Frame(canvas, borderwidth=3, relief="ridge")
outputframe.place(relx=0.50, rely= 0.15, relwidth = 0.49, relheight= 0.7 )

#output of IP/DNS status. it shows status of IP/DNS hostname
outputlabel = tk.Label(outputframe,text= "Status of IP/DNS hostnames", font=("Helvetica", 10), bg= "#ffebe6")
outputlabel.place(relx=0.0, rely=0.0,relwidth = 1.0, relheight= 0.07)

#shows status of IP/DNS hostname (UP/DOWN)
outputtext = tk.Text(outputframe)
outputtext.place(relx = 0.0, rely= 0.08, relwidth = 1.0, relheight = 0.92)

#button frame i.e. second last frame
buttonframe = tk.Frame(canvas, borderwidth=3, relief="ridge")
buttonframe.place(relx=0.01, rely= 0.85, relwidth = 0.98, relheight= 0.10 )

#ping  button to start ping ip/dns name for file input
pingbutton1 = Button(buttonframe, text="Start Ping",bg="#cccccc", command=ip_status)
pingbutton1.place(relx = 0.1, rely = 0.2, relwidth= 0.19)


#clear  button to close window
clearbutton= Button(buttonframe, text=" Clear Text", bg="#cccccc", command=cleartextbox)
clearbutton.place(relx = 0.5, rely = 0.2, relwidth= 0.19)

#stop_ping  button to stop the running script
stopbutton= Button(buttonframe, text="Stop Ping", bg="#cccccc", command=stop_ping)
stopbutton.place(relx = 0.3, rely = 0.2, relwidth= 0.19)
stopbutton.configure(state=DISABLED)

#close button to clear text area
closebutton = Button(buttonframe, text="Close", bg="#cccccc", command= close_window)
closebutton.place(relx = 0.7, rely = 0.2, relwidth= 0.19)


#copyright frame i.e. last frame
copyrightframe = tk.Frame(canvas, borderwidth=3, relief="ridge")
copyrightframe.place(relx=0.01, rely= 0.95, relwidth = 0.98, relheight= 0.05 )

#copyright label
copyrightlabel = tk.Label(copyrightframe, text= copyright_symbol+"2019 Yadav, Nanasaheb. All Rights Reserved.")
copyrightlabel.place(relx=0.52,relheight= 0.9)

root.mainloop()
