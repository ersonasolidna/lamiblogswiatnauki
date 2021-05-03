# UG 2021-05, zad. 2
# materiał pomocniczy do wyjaśnienia odpowiedzi na pytanie

import math

def znajdzLiczbyDlaSumy(mozliwasuma, debugMode = False):

	sumy = []
	for j in range(2,math.ceil(mozliwasuma//2)+1):
		sumy.append(j*(mozliwasuma-j))
		if debugMode:
			print (j,(mozliwasuma-j))
	return sumy

def main():

	mozliwesumy = [11,17,23,27,29,35,37,41,47,53]
	mozliwesumy_wykluczone = [51,57,59,65,67,71,77,79,83,87,89,93,95,97]

	mozliwesumy_wszystkie = mozliwesumy + mozliwesumy_wykluczone 

	debugMode = False
	#mozliwesumy = [51,57,59,65,67,71,77,79,83,87,89,93,95,97]

	liczby = [98,144,188,230,270,308,344,378,410,440,468,494,518,540,560,578,594,608,620,630,638,644,648,650,650] # liczby 51
	#liczby = [102,150,196,240,282,322,360,396,430,462,492,520,546,570,592,612,630,646,660,672,682,690,696,700,702] # liczby 53


	#print(liczba)
	for mozliwasuma in mozliwesumy_wszystkie:
		print ("*** możliwa suma: ", mozliwasuma)
		
		liczbyDlaSumy = znajdzLiczbyDlaSumy(mozliwasuma, debugMode)
		print ("Dostępne iloczyny P składników dla tej sumy S:", liczbyDlaSumy)
		for liczba in liczbyDlaSumy:

			liczbaPar = 0
			if debugMode:
				print ("  --- liczba: ",liczba)
			for i in range(1,math.ceil(mozliwasuma//2)):
				if liczba % i == 0:				
					if debugMode:
						print (i,"*",liczba/i)
					if (i < 100) and (liczba/i) < 100:
						liczbaPar += 1
						jedynaPara = i
			if liczbaPar == 1:
				print ("Znalazłem unikalną parę składników dającą ten iloczyn: ", liczba, "=", jedynaPara, "*",liczba/jedynaPara)

			#print(liczbaPar)\


if __name__ == "__main__":
	main()