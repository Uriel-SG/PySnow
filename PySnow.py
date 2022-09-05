import pyUnicodeSteganography as usteg
import time

print("\n####### PySnow #######")
time.sleep(0.5)

def snow():
	print("\n1- Nascondi\n2- Estrai\n3- Esci\n")
	scelta = str(input("--> "))
	if scelta == "1":
		try: 
			text = input('''\nContenitore: ''')
			secret_msg = input("\nMessaggio segreto: ")
			newfile = input("\nNuovo nome: ") + ".txt"
			encoded = usteg.encode(text, secret_msg)
			with open(newfile, "w") as steg:
				steg.write(encoded)
			print("\nFatto... Messaggio nascosto...")
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
				print("Messaggio segreto:\n\n" + decoded)
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