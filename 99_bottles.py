bottles = 99

while bottles != 0:
	if bottles == 1:
		print(str(bottles) + " bottle of beer on the wall " + str(bottles) + " bottle of beer, take one down pass it around, " + str(bottles) + " bottle of beer on the wall.")
		break
	else:
		print(str(bottles) + " bottles of beer on the wall " + str(bottles) + " bottles of beer, take one down pass it around, " + str(bottles) + " of beer.")
		bottles -= 1