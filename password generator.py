# 1. Vraag de gebruiker om een wachtwoord lengte
# 2. Vraag de gebruiker om een keuze te maken uit de volgende opties:
# 	1. Digits
# 	2. Letters
# 	3. Special characters
# 	4. Exit (Genereer wachtwoord)
# 3. Maak een lijst aan met de gekozen opties
# 4. Maak een wachtwoord aan met de lengte die de gebruiker heeft ingevoerd
# 5. Print het wachtwoord


import string
import random

lengte = int(input("Enter password length (Best to pick a number higher than 14) : "))

print('''Your password will contain the following options (pick a number)
		1. Digits
		2. Letters
		3. Special characters
		4. Exit (Generate password)''')

characterList = ""

while(True):
	keuze = int(input("Pick a number "))
	if(keuze == 1):
		
		characterList += string.ascii_letters
	elif(keuze == 2):
		
		characterList += string.digits
	elif(keuze == 3):
		
		characterList += string.punctuation
	elif(keuze == 4):
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(lengte):

	randomchar = random.choice(characterList)
	
	password.append(randomchar)

print("Generated password:\n" + "".join(password))