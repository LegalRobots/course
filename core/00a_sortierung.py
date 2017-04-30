def sortiere(liste):
	istSortiert = False
	
	while istSortiert == False:
		istSortiert = True
		
		for position in range(0, len(liste)-1):
			if liste[position] > liste[position+1]:
				temp = liste[position]
				liste[position] = liste[position+1]
				liste[position+1] = temp
				istSortiert = False
	

eineListe = [54,26,93,17,77,31,44,55,20]
sortiere(eineListe)
print(eineListe)