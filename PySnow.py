import pyUnicodeSteganography as usteg
import time
import os
import sys


print("\n####### PySnow #######")
time.sleep(0.5)

absolutepath = os.path.abspath(__file__)

fileDirectory = os.path.dirname(absolutepath)

dirlist = os.listdir(fileDirectory)

if "outputs" not in dirlist:
	outputpath = fileDirectory + "/" + "outputs"
	os.mkdir(outputpath)

def snow():
	global fileDirectory
	print("\n1- Nascondi\n2- Estrai\n3- Esci\n")
	scelta = str(input("--> "))
	if scelta == "1":
		try: 
			text = input("Percorso file Contenitore: ")
			secret_msg = input("\nMessaggio segreto: ")
			newfile = input("\nNuovo nome: ") + ".txt"
			with open(text, "r") as dec:
				contain = dec.read()
			encoded = usteg.encode(contain, secret_msg)
			outputfolder = fileDirectory + "/outputs/"
			outputpath = outputfolder + newfile
			with open(outputpath, "w") as steg:
				steg.write(encoded)
			time.sleep(0.5)
			print("\nFatto... Messaggio nascosto...")
			time.sleep(0.5)
			print(f"\nTroverai il nuovo file in {outputfolder}")
			time.sleep(0.5)
			print("\nDigita invio per tornare al menu iniziale")
			input()
			snow()
		except ValueError:
			print("\nIl messaggio contenitore è troppo corto rispetto al messaggio segreto...! Digita un tasto per ricominciare\n")
			input()
			snow()
	elif scelta == "2":
		try:
			file = input("\nFile: ")
			with open(file, "r") as steg:
				message = steg.read()
				decoded = usteg.decode(message)
				time.sleep(0.5)
				print("\nMessaggio segreto:\n\n" + decoded)
				time.sleep(0.5)
				input("\nDigita un tasto per continuare")
				snow()
		except FileNotFoundError:
			print("File non trovato... Sicuro di aver inserito il percorso esatto? Digita un tasto per riprovare...\n")
			input()
			snow()
	elif scelta == "3":
		exit
	else:
		print("\nScegli tra le 3 opzioni...\n")
		time.sleep(1)
		snow()
snow()