mat = [2, 45, 2, 12, 34] 
print(max(mat)) 


from random import *

texminiReq = randint(1,100)
print("100 ile 0 arasndan Seçin") 
while True:
	texmin= int (input (" Texminvizi yazin:"))
	if texmin == texminiReq:
		for i in range (5):
			print("Duz cavab") 
		break 
	elif texmin < texminiReq:
		print ("Daha Boyuk")
	elif texmin> texminiReq:
		print("Daha balaca")
