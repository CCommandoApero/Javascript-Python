texte = input ("Mets ta phrase wesh :")
mot_long = "" 

mots = texte.split()              
for mot in mots:
	if len(mot) > len(mot_long):
		mot_long = mot

print (mot_long)                         
