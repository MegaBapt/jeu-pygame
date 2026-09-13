import utile

continuer = 0	

plateau = {
	1 : {"a" : "t", "b" : "c", "c" : "f", "d" : "d", "e" : "r", "f" : "f", "g" : "c", "h" : "t"},
	2 : {"a" : "p", "b" : "p", "c" : "p", "d" : "p", "e" : "p", "f" : "p", "g" : "p", "h" : "p"},
	3 : {"a" : ".", "b" : ".", "c" : ".", "d" : ".", "e" : ".", "f" : ".", "g" : ".", "h" : "."},
	4 : {"a" : ".", "b" : ".", "c" : ".", "d" : ".", "e" : ".", "f" : ".", "g" : ".", "h" : "."},
	5 : {"a" : ".", "b" : ".", "c" : ".", "d" : ".", "e" : ".", "f" : ".", "g" : ".", "h" : "."},
	6 : {"a" : ".", "b" : ".", "c" : ".", "d" : ".", "e" : ".", "f" : ".", "g" : ".", "h" : "."},
	7 : {"a" : "\033[1;31mp\033[1;37m", "b" : "\033[1;31mp\033[1;37m", "c" : "\033[1;31mp\033[1;37m", "d" : "\033[1;31mp\033[1;37m", "e" : "\033[1;31mp\033[1;37m", "f" : "\033[1;31mp\033[1;37m", "g" : "\033[1;31mp\033[1;37m", "h" : "\033[1;31mp\033[1;37m"},
	8 : {"a" : "\033[1;31mt\033[1;37m", "b" : "\033[1;31mc\033[1;37m", "c" : "\033[1;31mf\033[1;37m", "d" : "\033[1;31md\033[1;37m", "e" : "\033[1;31mr\033[1;37m", "f" : "\033[1;31mf\033[1;37m", "g" : "\033[1;31mc\033[1;37m", "h" : "\033[1;31mt\033[1;37m"}
}

coup = ""

def affiche():
	utile.clear_screen()
	string = ""
	for clé, ligne in plateau.items():
		string += str(clé)+" "
		for clé, case in ligne.items():
			string += case
			string += " "
		print(string)
		string = ""
	print("  a b c d e f g h")

def input_valide(coup):
	if len(coup) < 2:
		return False, None, None
	if coup == "O-O":
		return True, "rogue", coup[-2]+coup[-1]
	if coup == "O-O-O":
		return True, "ROGUE", coup[-2]+coup[-1]
	if coup[-1] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
		return False, None, None
	if coup[-2] not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
		return False, None, None
	if len(coup) == 2:
		return True, "p", coup[-2]+coup[-1]
	if coup[-3] in ["t", "c", "f", "d", "r"]:
		return True, coup[-3], coup[-2]+coup[-1]
	return False, None, None

def piece_éxiste(pièce, position):
	if pièce == "rogue":
		if plateau[1]["f"] == "." and plateau[1]["g"] == ".":
			return True, 1
		else:
			return False, None
	elif pièce == "ROGUE":
		if plateau[1]["b"] == "." and plateau[1]["c"] == "." and plateau[1]["d"] == ".":
			return True, 1
		else:
			return False, None
	elif pièce == "p":
		if plateau[int(position[1])-2][position[0]] == "p" and plateau[int(position[1])][position[0]] == ".":
			return True, position[0] + str(int(position[1])-2)

		if plateau[int(position[1])-1][position[0]] == "p" and plateau[int(position[1])][position[0]] == ".":
			return True, position[0] + str(int(position[1])-1)

		elif plateau[int(position[1])-1][chr(ord(position[0])-1)] == "p" and plateau[int(position[1])][position[0]] != ".":
			return True, chr(ord(position[0])-1) + str(int(position[1])-1)

		elif plateau[int(position[1])-1][chr(ord(position[0])+1)] == "p" and plateau[int(position[1])][position[0]] != ".":
			return True, chr(ord(position[0])+1) + str(int(position[1])-1)

		else:
			return False, None
	elif pièce == "r":
		return roi(position)

	elif pièce == "c":
		return cavalier(position)

	elif pièce == "t":
		return tour(position)

	elif pièce == "f":
		return fou(position)

	elif pièce == "d":
		return dame(position)

	else:
		return True, "b2"

def pièce_éxiste2(pièce, position):
	if pièce == "rogue":
		if plateau[8]["f"] == "." and plateau[8]["g"] == ".":
			return True, 8
		else:
			return False, None
	elif pièce == "ROGUE":
		if plateau[8]["b"] == "." and plateau[8]["c"] == "." and plateau[8]["d"] == ".":
			return True, 8
		else:
			return False, None
	elif pièce == "p":
		if plateau[int(position[1])+2][position[0]] == "\033[1;31mp\033[1;37m" and plateau[int(position[1])][position[0]] == ".":
			return True, position[0] + str(int(position[1])+2)

		if plateau[int(position[1])+1][position[0]] == "\033[1;31mp\033[1;37m" and plateau[int(position[1])][position[0]] == ".":
			return True, position[0] + str(int(position[1])+1)

		elif plateau[int(position[1])+1][chr(ord(position[0])-1)] == "\033[1;31mp\033[1;37m" and plateau[int(position[1])][position[0]] != ".":
			return True, chr(ord(position[0])-1) + str(int(position[1])+1)

		elif plateau[int(position[1])+1][chr(ord(position[0])+1)] == "\033[1;31mp\033[1;37m" and plateau[int(position[1])][position[0]] != ".":
			return True, chr(ord(position[0])+1) + str(int(position[1])+1)

		else:
			return False, None
	elif pièce == "r":
		return roi(position)

	elif pièce == "c":
		return cavalier(position)

	elif pièce == "t":
		return tour(position)

	elif pièce == "f":
		return fou(position)

	elif pièce == "d":
		return dame(position)

	else:
		return True, "b2"

def cavalier(position):
	if plateau[int(position[1])-2][chr(ord(position[0])-1)] == "c" or plateau[int(position[1])-2][chr(ord(position[0])-1)] == "\033[1;31mc\033[1;37m":
		return True, chr(ord(position[0])-1) + str(int(position[1])-2)

	elif plateau[int(position[1])-2][chr(ord(position[0])+1)] == "c" or plateau[int(position[1])-2][chr(ord(position[0])+1)] == "\033[1;31mc\033[1;37m":
		return True, chr(ord(position[0])+1) + str(int(position[1])-2)

	elif plateau[int(position[1])+2][chr(ord(position[0])-1)] == "c" or plateau[int(position[1])+2][chr(ord(position[0])-1)] == "\033[1;31mc\033[1;37m":
		return True, chr(ord(position[0])-1) + str(int(position[1])+2)

	elif plateau[int(position[1])+2][chr(ord(position[0])+1)] == "c" or plateau[int(position[1])+2][chr(ord(position[0])+1)] == "\033[1;31mc\033[1;37m":
		return True, chr(ord(position[0])+1) + str(int(position[1])+2)

	elif plateau[int(position[1])-1][chr(ord(position[0])-2)] == "c" or plateau[int(position[1])-1][chr(ord(position[0])-2)] == "\033[1;31mc\033[1;37m":
		return True, chr(ord(position[0])-2) + str(int(position[1])-1)

	elif plateau[int(position[1])+1][chr(ord(position[0])-2)] == "c" or plateau[int(position[1])+1][chr(ord(position[0])-2)] == "\033[1;31mc\033[1;37m":
		return True, chr(ord(position[0])-2) + str(int(position[1])+1)

	elif plateau[int(position[1])-1][chr(ord(position[0])+2)] == "c" or plateau[int(position[1])-1][chr(ord(position[0])+2)] == "\033[1;31mc\033[1;37m":
		return True, chr(ord(position[0])+2) + str(int(position[1])-1)

	elif plateau[int(position[1])+1][chr(ord(position[0])+2)] == "c" or plateau[int(position[1])+1][chr(ord(position[0])+2)] == "\033[1;31mc\033[1;37m":
		return True, chr(ord(position[0])+2) + str(int(position[1])+1)

	else:
		return False, None

def roi(position):
	if plateau[int(position[1])-1][chr(ord(position[0])-1)] == "r" or plateau[int(position[1])-1][chr(ord(position[0])-1)] == "\033[1;31mr\033[1;37m":
		return True, chr(ord(position[0])-1) + str(int(position[1])-1)

	elif plateau[int(position[1])-1][position[0]] == "r" or plateau[int(position[1])-1][position[0]] == "\033[1;31mr\033[1;37m":
		return True, position[0] + str(int(position[1])-1)

	elif plateau[int(position[1])-1][chr(ord(position[0])+1)] == "r" or plateau[int(position[1])-1][chr(ord(position[0])+1)] == "\033[1;31mr\033[1;37m":
		return True, chr(ord(position[0])+1) + str(int(position[1])-1)

	elif plateau[int(position[1])][chr(ord(position[0])-1)] == "r" or plateau[int(position[1])][chr(ord(position[0])-1)] == "\033[1;31mr\033[1;37m":
		return True, chr(ord(position[0])-1) + position[1]

	elif plateau[int(position[1])][chr(ord(position[0])+1)] == "r" or plateau[int(position[1])][chr(ord(position[0])+1)] == "\033[1;31mr\033[1;37m":
		return True, chr(ord(position[0])+1) + position[1]

	elif plateau[int(position[1])+1][chr(ord(position[0])-1)] == "r" or plateau[int(position[1])+1][chr(ord(position[0])-1)] == "\033[1;31mr\033[1;37m":
		return True, chr(ord(position[0])-1) + str(int(position[1])+1)

	elif plateau[int(position[1])+1][position[0]] == "r" or plateau[int(position[1])+1][position[0]] == "\033[1;31mr\033[1;37m":
		return True, position[0] + str(int(position[1])+1)

	elif plateau[int(position[1])+1][chr(ord(position[0])+1)] == "r" or plateau[int(position[1])+1][chr(ord(position[0])+1)] == "\033[1;31mr\033[1;37m":
		return True, chr(ord(position[0])+1) + str(int(position[1])+1)

	else:
		return False, None

def tour(position):
	ligne = int(position[1])+1
	colonne = position[0]
	while ligne < 9:
		if plateau[ligne][colonne] == "t" or plateau[ligne][colonne] == "\033[1;31mt\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		ligne += 1

	ligne = int(position[1])-1
	while ligne > 0:
		if plateau[ligne][colonne] == "t" or plateau[ligne][colonne] == "\033[1;31mt\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		ligne -= 1

	ligne = int(position[1])
	colonne = chr(ord(position[0])+1)
	while colonne != "i":
		if plateau[ligne][colonne] == "t" or plateau[ligne][colonne] == "\033[1;31mt\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		colonne = chr(ord(colonne)+1)

	colonne = chr(ord(position[0])-1)
	while colonne != "`":
		if plateau[ligne][colonne] == "t" or plateau[ligne][colonne] == "\033[1;31mt\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		colonne = chr(ord(colonne)-1)

	return False, None

def fou(position):
	ligne = int(position[1])+1
	colonne = chr(ord(position[0])+1)

	while ligne < 9 and colonne != "i":
		if plateau[ligne][colonne] == "f" or plateau[ligne][colonne] == "\033[1;31mf\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		colonne = chr(ord(colonne)+1)
		ligne += 1

	ligne = int(position[1])+1
	colonne = chr(ord(position[0])-1)
	while ligne < 9 and colonne != "`":
		if plateau[ligne][colonne] == "f" or plateau[ligne][colonne] == "\033[1;31mf\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		colonne = chr(ord(colonne)-1)
		ligne += 1

	ligne = int(position[1])-1
	colonne = chr(ord(position[0])+1)
	while ligne > 0 and colonne != "i":
		if plateau[ligne][colonne] == "f" or plateau[ligne][colonne] == "\033[1;31mf\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		colonne = chr(ord(colonne)+1)
		ligne -= 1

	ligne = int(position[1])-1
	colonne = chr(ord(position[0])-1)
	while ligne > 0 and colonne != "`":
		if plateau[ligne][colonne] == "f" or plateau[ligne][colonne] == "\033[1;31mf\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		colonne = chr(ord(colonne)-1)
		ligne -= 1

	return False, None

def dame(position):
	ligne = int(position[1])+1
	colonne = position[0]
	while ligne < 9:
		if plateau[ligne][colonne] == "d" or plateau[ligne][colonne] == "\033[1;31md\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		ligne += 1

	ligne = int(position[1])-1
	while ligne > 0:
		if plateau[ligne][colonne] == "d" or plateau[ligne][colonne] == "\033[1;31md\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		ligne -= 1

	ligne = int(position[1])
	colonne = chr(ord(position[0])+1)
	while colonne != "i":
		if plateau[ligne][colonne] == "d" or plateau[ligne][colonne] == "\033[1;31md\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		colonne = chr(ord(colonne)+1)

	colonne = chr(ord(position[0])-1)
	while colonne != "`":
		if plateau[ligne][colonne] == "d" or plateau[ligne][colonne] == "\033[1;31md\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		colonne = chr(ord(colonne)-1)

	ligne = int(position[1])+1
	colonne = chr(ord(position[0])+1)
	while ligne < 9 and colonne != "i":
		if plateau[ligne][colonne] == "d" or plateau[ligne][colonne] == "\033[1;31md\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		colonne = chr(ord(colonne)+1)
		ligne += 1

	ligne = int(position[1])+1
	colonne = chr(ord(position[0])-1)
	while ligne < 9 and colonne != "`":
		if plateau[ligne][colonne] == "d" or plateau[ligne][colonne] == "\033[1;31md\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		colonne = chr(ord(colonne)-1)
		ligne += 1

	ligne = int(position[1])-1
	colonne = chr(ord(position[0])+1)
	while ligne > 0 and colonne != "i":
		if plateau[ligne][colonne] == "d" or plateau[ligne][colonne] == "\033[1;31md\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		colonne = chr(ord(colonne)+1)
		ligne -= 1

	ligne = int(position[1])-1
	colonne = chr(ord(position[0])-1)
	while ligne > 0 and colonne != "`":
		if plateau[ligne][colonne] == "d" or plateau[ligne][colonne] == "\033[1;31md\033[1;37m":
			return True, colonne + str(ligne)
		if plateau[ligne][colonne] != ".":
			break
		colonne = chr(ord(colonne)-1)
		ligne -= 1

	return False, None


def bouger(position_départ, position_arrivé, pièce):
	arrivé = "0"
	if pièce != "rogue" and pièce != "ROGUE":
		plateau[int(position_départ[1])][position_départ[0]] = "."
		plateau[int(position_arrivé[1])][position_arrivé[0]] = pièce
		arrivé = plateau[int(position_arrivé[1])][position_arrivé[0]]
	elif pièce == "rogue":
		plateau[départ]["g"] = "r"
		plateau[départ]["f"] = "t"
		plateau[départ]["e"] = "."
		plateau[départ]["h"] = "."
	else:
		plateau[départ]["c"] = "t"
		plateau[départ]["d"] = "r"
		plateau[départ]["e"] = "."
		plateau[départ]["a"] = "."
	if arrivé == "r":
		return 1
	if arrivé == "\033[1;31mr\033[1;37m":
		return 2
	return 0

while continuer == 0:
	stop1 = False
	stop2 = False
	pièce = ""
	position = ""
	départ = ""
	affiche()
	while not stop1 or not stop2:
		coup = str(input())
		stop1, pièce, position = input_valide(coup)
		stop2, départ = piece_éxiste(pièce, position)
	continuer = bouger(départ, position, pièce)

	stop1 = False
	stop2 = False
	pièce = ""
	position = ""
	départ = ""
	affiche()
	while not stop1 or not stop2:
		coup = str(input())
		stop1, pièce, position = input_valide(coup)
		stop2, départ = pièce_éxiste2(pièce, position)
	continuer = bouger(départ, position, f"\033[1;31m{pièce}\033[1;37m")

affiche()
print(f"tu as gagné joueur {continuer}")
