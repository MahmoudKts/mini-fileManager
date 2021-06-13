from tkinter import *
from tkinter import filedialog
import tkinter as tk
import shutil
import os


def copyFiles(directoryName): 
	filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File")
	desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
	path=desktop+chr(92)+"files"+chr(92)+directoryName
	label_file_explorer.configure(text="File Opened: "+filename+"\n"+"copied in: "+path) 
	try:
		os.makedirs(path)
	except OSError:
		print ("directory already exist!")
	else:
    		print ("Successfully created the directory %s" % path)
	filename_w_ext = os.path.basename(filename)
	newPath=path+chr(92)+filename_w_ext
	shutil.copyfile(filename,newPath)

def listFiles(directoryName): 
	
	desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
	path=desktop+chr(92)+"files"+chr(92)+directoryName
	arr = os.listdir(path)
	label_file_list.configure(text=arr)
	
	
	

window = tk.Tk() 

label_file_explorer = Label(window, text = "Click button to copy file") 
button_sgbd = Button(window, text = "copy to sgbd", command =lambda: copyFiles("sgbd")) 
button_math = Button(window, text = "copy to math", command =lambda: copyFiles("math"))  
button_fr = Button(window, text = "copy to fr", command =lambda: copyFiles("fr")) 
button_list_sgbd = Button(window, text = "files in sgbd", command =lambda: listFiles("sgbd")) 
button_list_math = Button(window, text = "files in math", command =lambda: listFiles("math")) 
button_list_fr = Button(window, text = "files in fr", command =lambda: listFiles("fr")) 
label_file_list =Label(window,text="")

label_file_explorer.grid(columnspan=2, sticky=W,pady=10,padx=30)
button_sgbd.grid(row=1, column=0,padx=30)
button_list_sgbd.grid(row=1, column=1)
button_fr.grid(row=2, column=0)
button_list_fr.grid(row=2, column=1)
button_math.grid(row=3, column=0)
button_list_math.grid(row=3, column=1)
label_file_list.grid(columnspan=2, sticky=W)


window.geometry("300x150+500+250")
window.mainloop() 
