import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
import subprocess
import webbrowser
import pyUnicodeSteganography as usteg


def snow_gui():
	finestra = tk.Tk()
	finestra.title("PySnow")
	finestra.geometry("600x690")
	finestra.configure(bg="black")
	finestra.iconbitmap("icouriel.ico")
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
			window.iconbitmap("icouriel.ico")
			frame1 = tk.Frame(window)
			frame1.pack()
			frame2 = tk.Frame(window, bg="black")
			frame2.pack()
			
			#Functions
			secret_message = ""
			container = "" #path
			#newfile = "" #path
			final_path = ""

			def done():
				#global newfile
				global final_path
				showinfo(
				title='Fatto!',
				message=f"Messaggio nascosto con successo!"
				)
				pathtoopen = os.path.dirname(final_path)
				print(pathtoopen)
				webbrowser.open(pathtoopen)
				refresh()
			
			def stegsnow():
				global secret_message
				global container
				#global newfile
				global final_path
				
				with open(container, "r", encoding='utf-8') as tohide:
					cont = tohide.read()
				encoded = usteg.encode(cont, secret_message)
				filetypes = (
						('testo', '*.txt'),
						('all', '.*')
						)
				final_path = fd.asksaveasfilename(initialdir="C:/", title="Salva", filetypes=filetypes, defaultextension=".txt")
				with open(final_path, "w", encoding='utf-8') as finalpath:
					finalpath.write(encoded)
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
				#newfile = newfileentry.get() + ".txt"
				#newfileentry.delete("0", tk.END)
				stegsnow()
			
			def exithide():
				window.destroy()
				snow_gui()
				
			#Widgets
			buttons_style = ttk.Style()
			buttons_style.configure('my.TButton', font=('Times', 12))
			buttons_style.configure('big.TButton', font=('Times', 13, 'bold'))
			
			title = tk.Label(frame1, text="\nSNOW",
				fg= "white",
				bg= "black",
				font=("Times", 24, "bold"))
			title.pack(fill=tk.X)
			
			message_label = tk.Label(frame1, text="\n\nScrivi qui il messaggio segreto: ", bg="black", fg="white", font=("Times", 12))
			message_label.pack(fill=tk.X)
			
			message = tk.Text(frame1, padx=15, pady=15, height=8, font=("Times", 12), wrap="word")
			message.pack()
			
			select_label = tk.Label(frame1, text="\nScegli il file di testo \nin cui nascondere il tuo messaggio: ", bg="black", fg="white", font=("Times", 12))
			select_label.pack(fill=tk.X)
			
			path = tk.Entry(frame1, state="disabled", width=60)
			path.pack(side=tk.LEFT)
			
			filebutt = ttk.Button(frame1, text="Scegli File", style="my.TButton", command=select_container)
			filebutt.pack(side=tk.RIGHT)
			
			empty = tk.Label(frame2, bg="black").pack(fill=tk.X)
			
			#final_label = tk.Label(frame2, text="\nNome del file finale: ", bg="black", fg="white", font=("Times", 12))
			#final_label.pack(fill=tk.X)
			
			#newfileentry = tk.Entry(frame2)
			#newfileentry.pack()
			
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
			file_path = None
			
			def extract2():
				global file_path
				with open(file_path, "r", encoding='utf-8') as todecode:
					todecode = open(file_path, "r", encoding='utf-8')
				mess = todecode.read()
				decoded = usteg.decode(mess)
				showtext["state"] = "normal"
				showtext.insert(tk.END, decoded)
				showtext["state"] = "disabled"
				todecode.close()
			
			def toopen():
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
			
			#Window
			window = tk.Tk()
			window.title("PySnow")
			window.configure(bg="black")
			window.iconbitmap("icouriel.ico")
			#Widgets
			title = tk.Label(text="PySnow",
				fg= "white",
				bg= "black",
				font=("Times", 24,  "bold"))
			title.pack(fill=tk.X)
			
			empty = tk.Label(bg="black")
			empty.pack(fill=tk.X)
			
			openfile = ttk.Button(text="Apri file", command=toopen)
			openfile.pack()
			
			opened = tk.Label(bg="black", fg="white", font=("Times", 12))
			opened.pack()
			
			empty = tk.Label(bg="black")
			empty.pack(fill=tk.X)
			empty = tk.Label(bg="black")
			empty.pack(fill=tk.X)
			
			showtext = tk.Text(padx=15, pady=15, height=7, wrap="word", state="disabled", font=("Times", 12))
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
	
	#Widgets
	buttons_style = ttk.Style()
	buttons_style.configure('my.TButton', font=('Times', 12))
	
	empty = tk.Label(text="° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °")
	empty.pack(fill=tk.X)	
		
	title = tk.Label(text="-   PySnow   -",
		fg= "white",
		bg= "black",
		font=("Times", 24,  "bold"),
		height=2)
	title.pack(fill=tk.X)
	
	empty = tk.Label(text="° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °")
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
	
	empty = tk.Label(text="° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °")
	empty.pack(fill=tk.X)
	
	empty = tk.Label(bg="black", text="\n\n")
	empty.pack(fill=tk.X)
	
	#Image
	logo = tk.PhotoImage(file="uriel-white.png")
	smallerlogo = logo.subsample(2, 2)
	uriel = tk.Label(image=smallerlogo, bg='black')
	uriel.pack(fill=tk.X)
	
	powered = tk.Label(text="* * * * * * * * * * * * * * * *  powered by Uriel-SG  * * * * * * * * * * * * * * * *", font=("Calibri", 8))
	powered.pack(fill=tk.X, side=tk.BOTTOM)
	
	empty = tk.Label(bg="black")
	empty.pack(fill=tk.X, side=tk.BOTTOM)
	
	def exitprog():
		finestra.destroy()

	esci = ttk.Button(text="Esci", style="my.TButton", command=exitprog)
	esci.pack(side=tk.BOTTOM)
	
	finestra.mainloop()
	
snow_gui()
