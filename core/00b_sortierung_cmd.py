import sys

def sortiere(input):
	liste = input
	istSortiert = False
	
	while istSortiert == False:
		istSortiert = True
		
		for position in range(0, len(liste)-1):
			if liste[position] > liste[position+1]:
				# Shortcut in Python: Parallel Assignment (advanced)
				liste[position], liste[position+1] = liste[position+1], liste[position]
				istSortiert = False
	return liste

# Was ist hier moeglicherweise problematisch?
try:
	eineListe = [float(arg) for arg in sys.argv[1:]]
	print(sortiere(eineListe))
except ValueError:
	print('Bitte eine Liste von Zahlen eingeben!')
		
