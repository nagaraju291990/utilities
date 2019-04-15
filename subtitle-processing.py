#Processing a srt file for subtitle text extraction
#pip3 install pysrt

import os
import sys
import pysrt
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox

#validator
def validateSRT():
	flag = 1
	filename = E1.get()
	no_of_langs = E2.get()
	file = open(filename,"r")
	file_content = file.read()
	lines = file_content.split("\n")
	n_lang = int(no_of_langs)
	c = n_lang+2
	ll = c
	jj = c+1
	print(c,ll,jj,sep='\t')
	for gg in range(len(lines)/jj):
		if not lines[ll].strip():
			ll = ll+c+1
		else:
			msg = tkMessageBox.showinfo( "Error", "input is not in format near group"+ str(gg+1))
			print ("input is not in format near group ",gg+1)
			flag = 0
			#sys.exit(0)
			break
			#msg = tkMessageBox.showinfo( "Hello Python", "Hello World")
	if(flag == 1):
		msg = messagebox.showinfo( "Validate", "File Format is Okay")
	file.close()




#extract sentences
def extractText():

	srtfilename = E1.get()
	subs = pysrt.open(srtfilename)
	#print(subs)
	#exit()
	out_file=open('output_file'+os.path.basename(srtfilename),"w")
	c = 1
	for sub in subs:
		out_file.write("[SUBTITLE-"+str(c)+"]\n" + sub.text+"\n")
		c = c+1
		#print(subs.text)
	msg=messagebox.showinfo( "Text Extraction ", "Text file has been Created Successfully")


def openFileDialog():
	filename =  filedialog.askopenfilename(initialdir = "~/Downloads/",title = "Select file",filetypes = (("srt files","*.srt"),("all files","*.*")))
	#E1.delete(0, root.END)
	E1.insert(0, filename)
	#E1.set(filename)

root  =  Tk()
root.geometry("600x650+350+100")
frame  =  Frame(root,relief = SUNKEN,borderwidth = 1)
frame.pack(expand = True,fill = X)



L16  =  Label(frame,text = "Extract Text from SRT Files",font = "serif 12")
L16.pack(pady = 3)

B16  =  Button(frame,text = "Browse SRT Files",font = "serif 12",command  =  openFileDialog,fg = "white",bg = "black")
B16.pack(pady = 3)

L1  =  Label(frame,text = "Enter srt Name",font = "serif 12")
L1.pack( pady = 0)

E1  =  Entry(frame, bd  = 1,bg = "whitesmoke",fg = "black")
E1.pack(pady = 5)
"""

L2  =  Label(frame,text = "Enter No languages file have",font = "serif 12")
L2.pack()

E2  =  Entry(frame, bd  = 1,bg = "whitesmoke",fg = "black")
E2.pack( pady = 5)




B  =  Button(frame, text  = "Validate   Srt", command  =  validateSRT,fg = "white",bg = "black")
#B.place(x = 215,y = 95)
B.pack( padx = 5, pady = 3)"""

B1  =  Button(frame, text  = "Extract Text", command  =  extractText,fg = "white",bg = "black")
#B1.place(x = 215,y = 135)
B1.pack( padx = 5, pady = 3)



root.title("Subtitles Tool")
root.mainloop()
