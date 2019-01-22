import tkinter
import re
import os	 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad: 

	__root = Tk() 

	# default window width and height 
	__thisWidth = 300
	__thisHeight = 300
	__thisTextArea = Text(__root) 
	__thisMenuBar = Menu(__root) 
	__thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
	__thisEditMenu = Menu(__thisMenuBar, tearoff=0) 
	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0) 
	
	# To add scrollbar 
	__thisScrollBar = Scrollbar(__thisTextArea)	 
	__file = None

	def __init__(self,**kwargs): 

		# Set icon 
		try: 
				self.__root.wm_iconbitmap("Notepad.ico") 
		except: 
				pass

		# Set window size (the default is 300x300) 

		try: 
			self.__thisWidth = kwargs['width'] 
		except KeyError: 
			pass

		try: 
			self.__thisHeight = kwargs['height'] 
		except KeyError: 
			pass

		# Set the window text 
		self.__root.title("Untitled - Notepad") 

		# Center the window 
		screenWidth = self.__root.winfo_screenwidth() 
		screenHeight = self.__root.winfo_screenheight() 
	
		# For left-alling 
		left = (screenWidth / 2) - (self.__thisWidth / 2) 
		
		# For right-allign 
		top = (screenHeight / 2) - (self.__thisHeight /2) 
		
		# For top and bottom 
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
											self.__thisHeight, 
											left, top)) 

		# To make the textarea auto resizable 
		self.__root.grid_rowconfigure(0, weight=1) 
		self.__root.grid_columnconfigure(0, weight=1) 

		# Add controls (widget) 
		self.__thisTextArea.grid(sticky = N + E + S + W) 
		
		# To open new file 
		self.__thisFileMenu.add_command(label="New", 
										command=self.__newFile)	 
		
		# To open a already existing file 
		self.__thisFileMenu.add_command(label="Open", 
										command=self.__openFile) 
		
		# To save current file 
		self.__thisFileMenu.add_command(label="Save", 
										command=self.__saveFile)	 

		# To create a line in the dialog		 
		self.__thisFileMenu.add_separator()										 
		self.__thisFileMenu.add_command(label="Exit", 
										command=self.__quitApplication) 
		self.__thisMenuBar.add_cascade(label="File", 
									menu=self.__thisFileMenu)	 
		
		# To give a feature of cut 
		self.__thisEditMenu.add_command(label="Cut", 
										command=self.__cut)			 
	
		# to give a feature of copy	 
		self.__thisEditMenu.add_command(label="Copy", 
										command=self.__copy)		 
		
		# To give a feature of paste 
		self.__thisEditMenu.add_command(label="Paste", 
										command=self.__paste)		 
		
		# To give a feature of editing 
		self.__thisMenuBar.add_cascade(label="Edit", 
									menu=self.__thisEditMenu)	 
		
		# To create a feature of description of the notepad 
		self.__thisHelpMenu.add_command(label="Run and visualise", 
										command=self.__showAbout) 
		self.__thisMenuBar.add_cascade(label="Run", 
									menu=self.__thisHelpMenu)
		
		self.__root.config(menu=self.__thisMenuBar) 

		self.__thisScrollBar.pack(side=RIGHT,fill=Y)					 
		
		# Scrollbar will adjust automatically according to the content		 
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)	 
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
	
		
	def __quitApplication(self): 
		self.__root.destroy() 
		# exit()
	def __showAbout(self):
				visual = Tk()
				canvas = Canvas(visual, width = 1000, height = 1000)
				canvas.pack()
				#os.system("gcc ")
				file_name_here = self.__file
				file_name_here = file_name_here[3:]
				#print(file_name_here)
				os.system("cd .. & cd .. & gcc" + file_name_here + "& a.exe")
				os.system("cd ..")
				#print(self.__thisTextArea.get(1.0, END))
				#err = "return"
				inbuilts = re.findall(r"(\w+\s\w+);",self.__thisTextArea.get(1.0, END))
				arrays=re.findall(r"\w+\s\w+\[\w+\](?!,);",self.__thisTextArea.get(1.0,END))
				pointers = re.findall(r"(\w+[\*]+\s\w+);", self.__thisTextArea.get(1.0, END))
				#array_of_pointers = re.findall(
				#print(pointers)
				err = 'return 0'
				#print(inbuilts)
				if err in inbuilts:
						inbuilts.remove(err)
				k = 0
				for j in range(0, len(inbuilts)):
					inbuilt_num = inbuilts[j]
					spl = inbuilt_num.split()
					type_of_inbuilt = spl[0]
					name_of_inbuilt = spl[1]
					canvas.create_text(25, 55+95*k, font = ("bold", 20), text = name_of_inbuilt)
					canvas.create_oval(55, 15+95*k, 135, 95+95*k)
					canvas.create_text(95, 55+95*k, text = type_of_inbuilt)
					k = k + 1
				for j in range(0, len(arrays)):
						array_num = arrays[j]
						#print("working")
						spl = array_num.split()
						type_of_array = spl[0]
						name_and_length = spl[1]
						init_pos = name_and_length.find("[")
						final_pos = name_and_length.find("]")
						name = name_and_length[:init_pos]
						length_arr = int(name_and_length[(init_pos) + 1 : final_pos])
						canvas.create_text(25, 55+95*k, font = ("bold", 20), text = name)
						for i in range(0, length_arr):
								canvas.create_oval(55+90*i, 15+95*k, 135+90*i, 95+95*k)
								canvas.create_text(95+90*i, 55+95*k, text=type_of_array)
								canvas.create_rectangle(50+90*i, 10+95*k, 140+90*i, 100+95*k)
						k = k + 1
				for j in range(0, len(pointers)):
					pointer_num = pointers[j]
					spl = pointer_num.split()
					type_pointer = spl[0]
					pos = type_pointer.find('*')
					#print(pos)
					type_of_variable = type_pointer[: pos]
					number_of = len(type_pointer) - pos;
					name_of_pointer = spl[1]
					canvas.create_text(25, 55+95*k, font = ("bold", 20), text = name_of_pointer)
					for i in range(0, number_of):
						canvas.create_rectangle(55+130*i, 25+95*k, 115+130*i, 85+95*k)
						canvas.create_line(95+130*i, 55+95*k, 180+130*i, 55+95*k, arrow=tkinter.LAST)
					#canvas.create_rectangle(55, 25+95*k, 115, 85+95*k)
					#canvas.create_line(95, 55+95*k, 180, 55+95*k, arrow=tkinter.LAST)
					canvas.create_oval(185+130*i, 15+95*k, 265+130*i, 95+95*k)
					canvas.create_text(225+130*i, 55+95*k, text = type_of_variable)
					k= k + 1

	def __openFile(self): 
		
		self.__file = askopenfilename(defaultextension=".txt", 
									filetypes=[("All Files","*.*"), 
										("Text Documents","*.txt")]) 

		if self.__file == "": 
			
			# no file to open 
			self.__file = None
		else: 
			
			# Try to open the file 
			# set the window title 
			self.__root.title(os.path.basename(self.__file) + " - Notepad") 
			self.__thisTextArea.delete(1.0,END) 

			file = open(self.__file,"r") 

			self.__thisTextArea.insert(1.0,file.read()) 

			file.close() 

		
	def __newFile(self): 
		self.__root.title("Untitled - Notepad") 
		self.__file = None
		self.__thisTextArea.delete(1.0,END) 

	def __saveFile(self): 

		if self.__file == None: 
			# Save as new file 
			self.__file = asksaveasfilename(initialfile='Untitled.txt', 
											defaultextension=".txt", 
											filetypes=[("All Files","*.*"), 
												("Text Documents","*.txt")])
			print(self.__file)

			if self.__file == "": 
				self.__file = None
			else: 
				
				# Try to save the file 
				file = open(self.__file,"w") 
				file.write(self.__thisTextArea.get(1.0,END)) 
				file.close() 
				
				# Change the window title 
				self.__root.title(os.path.basename(self.__file) + " - Notepad") 
				
			
		else: 
			file = open(self.__file,"w") 
			file.write(self.__thisTextArea.get(1.0,END)) 
			file.close() 

	def __cut(self): 
		self.__thisTextArea.event_generate("<<Cut>>") 

	def __copy(self): 
		self.__thisTextArea.event_generate("<<Copy>>") 

	def __paste(self): 
		self.__thisTextArea.event_generate("<<Paste>>") 

	def run(self): 

		# Run main application 
		self.__root.mainloop() 




# Run main application 
notepad = Notepad(width=600,height=400) 
notepad.run() 
