import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
import subprocess
import pyUnicodeSteganography as usteg

def snow_gui():
	finestra = tk.Tk()
	finestra.title("PySnow")
	finestra.configure(bg="black")
	
	frame1 = tk.Frame(finestra, bg="black")
	frame1.pack()
	
	def hide():
		finestra.destroy()
		def start_gui():
			global window
			
			#Window and frames
			
			window = tk.Tk()
			window.title("PySnow")
			window.configure(bg="black")
			
			frame1 = tk.Frame(window)
			frame1.pack()
			frame2 = tk.Frame(window, bg="black")
			frame2.pack()
			
			#Functions
			
			secret_message = ""
			container = ""
			password = ""
			compression = False
			newfile = ""
			
			def done():
				showinfo(
		        title='Fatto!',
		        message=f"Messaggio nascosto nel file {newfile}!"
		    	)
				refresh()
			
			def stegsnow():
				global secret_message
				global container
				global newfile
				encoded = usteg.encode(container, secret_message)
				with open(newfile, "w") as final:
					final.write(encoded)
				done()
			
			def select_container():
				global container
				filetypes = (
				        ('testo', '*.txt'),
				        ('all', '.*')
				        )
				container = fd.askopenfilename(
				title='Testo Contenitore:  ',
				initialdir='/storage/emulated/0',
				filetypes=filetypes)
				path["state"] = "normal"
				path.insert(tk.END, container)
				path["state"] = "disabled"
						
			def hide():
				global secret_message
				global container
				global newfile
				secret_message = message.get("1.0", tk.END)
				message.delete("1.0", tk.END)
				newfile = fd.asksaveasfilename(title='Nome file finale:  ',
				filetypes=(('testo', '*.txt'), ("all", ".*")))
				stegsnow()
			
			def exithide():
				window.destroy()
				snow_gui()
				
			#Widgets
			
			buttons_style = ttk.Style()
			buttons_style.configure('my.TButton', font=('Times', 8))
			buttons_style.configure('big.TButton', font=('Times', 9, 'bold'))
			
			title = tk.Label(frame1, text="SNOW",
				fg= "white",
				bg= "black",
				font=("Times", 14, "bold"))
			title.pack(fill=tk.X)
			
			message_label = tk.Label(frame1, text="\n\nScrivi qui il messaggio segreto: ", bg="black", fg="white", font=("Times", 7))
			message_label.pack(fill=tk.X)
			
			message = tk.Text(frame1, padx=15, pady=15, height=8, font=("Times", 7), wrap="word")
			message.pack()
			
			select_label = tk.Label(frame1, text="\nScegli il file di testo \nin cui nascondere il tuo messaggio: ", bg="black", fg="white", font=("Times", 7))
			select_label.pack(fill=tk.X)
			
			path = tk.Entry(frame1, state="disabled")
			path.pack(side=tk.LEFT)
			
			filebutt = ttk.Button(frame1, text="Scegli File", style="my.TButton", command=select_container)
			filebutt.pack(side=tk.RIGHT)
			
			empty = tk.Label(frame2, bg="black").pack(fill=tk.X)
			
			hidebutton = ttk.Button(frame2, text="Nascondi", style="big.TButton", command=hide)
			hidebutton.pack()
			
			empty = tk.Label(frame2, text="\n\n", bg="black").pack(fill=tk.X)
			
			refreshbutton = ttk.Button(frame2, text="Pulisci", style="my.TButton", command=refresh)
			refreshbutton.pack(side=tk.LEFT)
			
			empty = tk.Label(frame2, bg="black").pack(side=tk.LEFT)
			
			exitbutton = ttk.Button(frame2, text="Esci", style="my.TButton", command=exithide)
			exitbutton.pack(side=tk.LEFT)
			
			window.mainloop()
	
		def refresh():
			window.destroy()
			start_gui()
			
		start_gui()
	
	def extract():
		finestra.destroy()
		def startgui():
			global window
			file_path = ""
			
			def extract2():
				global file_path
				decoded = usteg.decode(file_path)
				showtext["state"] = "normal"
				showtext.insert(tk.END, decoded)
				showtext["state"] = "disabled"
			
			def open():
				global file_path
				file_path = fd.askopenfilename(
					title='Testo Contenitore:  ',
					initialdir='/storage/emulated/0', 
					filetypes=(('text', '*.txt'), ('all', '.*'))
					)
				opened["text"] = file_path
			
			def principal():
				window.destroy()
				snow_gui()
			
			window = tk.Tk()
			window.title("PySnow")
			window.configure(bg="black")
			title = tk.Label(text="PySnow",
				fg= "white",
				bg= "black",
				font=("Times", 20,  "bold"))
			title.pack(fill=tk.X)
			empty = tk.Label(bg="black")
			empty.pack(fill=tk.X)
			openfile = ttk.Button(text="Apri file", command=open)
			openfile.pack()
			opened = tk.Label(bg="black", fg="white", font=("Times", 7))
			opened.pack()
			empty = tk.Label(bg="black")
			empty.pack(fill=tk.X)
			empty = tk.Label(bg="black")
			empty.pack(fill=tk.X)
			showtext = tk.Text(state="disabled", font=("Times", 14), height=7)
			showtext.pack()
			extractbutt = ttk.Button(text="Estrai", command=extract2)
			extractbutt.pack()
			cleanbutt = ttk.Button(text="Pulisci", command=refresh)
			cleanbutt.pack(side=tk.LEFT)
			exitbutt = ttk.Button(text="Esci", command=principal)
			exitbutt.pack(side=tk.RIGHT)
			window.mainloop()
			
		def refresh():
			window.destroy()
			startgui()
		startgui()
	
	buttons_style = ttk.Style()
	buttons_style.configure('my.TButton', font=('Times', 8))
	
	empty = tk.Label()
	empty.pack(fill=tk.X)	
		
	title = tk.Label(text="PySnow",
		fg= "white",
		bg= "black",
		font=("Times", 20,  "bold"))
	title.pack(fill=tk.X)
	
	empty = tk.Label()
	empty.pack(fill=tk.X)
	
	empty = tk.Label(bg="black")
	empty.pack(fill=tk.X)
	
	nascondibutt = ttk.Button(text="Nascondi",style="my.TButton", command=hide)
	nascondibutt.pack()
	
	empty = tk.Label(bg="black")
	empty.pack(fill=tk.X)
	
	estraibutt = ttk.Button(text="Estrai", style="my.TButton", command=extract)
	estraibutt.pack()
	
	empty = tk.Label(bg="black")
	empty.pack(fill=tk.X)
	
	empty = tk.Label()
	empty.pack(fill=tk.X)
	
	empty = tk.Label(bg="black")
	empty.pack(fill=tk.X)
	
	esci = ttk.Button(text="Esci", style="my.TButton", command=exit)
	esci.pack()
	
	powered = tk.Label(text="\npowered by Uriel-SG", font=("Calibri", 5), bg="black", fg="white")
	powered.pack(fill=tk.X)
	
	empty = tk.Label()
	empty.pack(fill=tk.X, side=tk.BOTTOM)
	
	finestra.mainloop()
snow_gui()