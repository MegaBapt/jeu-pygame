import pygame
import random
import math

def init(taille):
	# 0 = point normal
	# 1 = mur
	# 2 = super pacgum
	# 3 = case vide
	# 4 = entrée
	for y in range(len(matrice)):
		for x in range(len(matrice[y])):
			if matrice[y][x] == 0:
				pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x*taille + (taille/5)*2, y*taille + (taille/5)*2, taille/5, taille/5))
			elif matrice[y][x] == 1:
				pygame.draw.rect(screen, (20, 20, 255), pygame.Rect(x*taille, y*taille, taille, taille))
			elif matrice[y][x] == 2:
				pygame.draw.rect(screen, (255, 255, 200), pygame.Rect(x*taille + taille/3, y*taille + taille/3, taille/3, taille/3))
			elif matrice[y][x] == 4:
				pygame.draw.rect(screen, (150, 255, 255), pygame.Rect(x*taille, y*taille + (taille/5)*2, taille, taille/5))

class pacman(object):
	"""docstring for pacman"""
	def __init__(self, x, y, taille):
		super(pacman, self).__init__()
		self.x = x
		self.y = y
		self.body = pygame.Rect(x*taille, y*taille, taille, taille)
		self.speed = taille
		self.direction = 0
		self.couleur = (255, 255, 0)
		self.point = 0
		self.invincible = False

	def move(self, rouge, bleu, rose, orange):
		if matrice[self.y][self.x] == 0:
			self.point += 1
			matrice[self.y][self.x] = 3

		elif matrice[self.y][self.x] == 2:
			self.point += 3
			matrice[self.y][self.x] = 3
			pygame.time.set_timer(PACGUMTIME, 10000, loops=1)
			self.invincible = True
			self.couleur = (255, 255, 255)
			rouge.start_pacgum_time()
			bleu.start_pacgum_time()
			rose.start_pacgum_time()
			orange.start_pacgum_time()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP] and matrice[self.y-1][self.x] not in [1, 4]: self.direction = 1
		if keys[pygame.K_DOWN] and matrice[self.y+1][self.x] not in [1, 4]: self.direction = 2
		if keys[pygame.K_LEFT] and matrice[self.y][self.x-1] not in [1, 4]: self.direction = 3
		if keys[pygame.K_RIGHT] and matrice[self.y][self.x+1] not in [1, 4]: self.direction = 4


		if self.direction == 1 and matrice[self.y-1][self.x] not in [1, 4]: 
			self.body.y -= self.speed
			self.y -= 1
		if self.direction == 2 and matrice[self.y+1][self.x] not in [1, 4]: 
			self.body.y += self.speed
			self.y += 1
		if self.direction == 3 and matrice[self.y][self.x-1] not in [1, 4]: 
			self.body.x -= self.speed
			self.x -= 1
		if self.direction == 4 and matrice[self.y][self.x+1] not in [1, 4]: 
			self.body.x += self.speed
			self.x += 1

	def end_pacgum_time(self):
		self.couleur = (255, 255, 0)
		self.invincible = False





class blinky(object):
	"""docstring for blinky"""
	def __init__(self, x, y, taille):
		super(blinky, self).__init__()
		self.x = x
		self.y = y
		self.body = pygame.Rect(x*taille, y*taille, taille, taille)
		self.speed = taille
		self.direction = 1
		self.couleur  = (255, 0, 0)
		self.etat = "scatter"

	def move(self, joueur):
		action = 0
		actions = [1, 2, 3, 4]
		if [self.x, self.y] == [9, 8] and self.etat == "eaten":
			self.revive()
		if matrice[self.y-1][self.x] == 1 or self.direction == 2:
			actions.remove(1)
		if matrice[self.y+1][self.x] in [1, 4] or self.direction == 1:
			actions.remove(2)
		if matrice[self.y][self.x-1] in [1, 4] or self.direction == 4:
			actions.remove(3)
		if matrice[self.y][self.x+1] in [1, 4] or self.direction == 3:
			actions.remove(4)
		if self.etat == "frighten":
			action = actions[random.randint(0, len(actions)-1)]
		else:
			if self.etat == "chase":
				target = [joueur.x, joueur.y]
			elif self.etat == "eaten":
				target = [9, 8]
			elif self.etat == "scatter":
				target = [19, 0]

			distances = []
			if 1 in actions:
				distances.append(math.sqrt((self.x - target[0])**2 + ((self.y-1) - target[1])**2))
			if 2 in actions:
				distances.append(math.sqrt((self.x - target[0])**2 + ((self.y+1) - target[1])**2))
			if 3 in actions:
				distances.append(math.sqrt(((self.x-1) - target[0])**2 + (self.y - target[1])**2))
			if 4 in actions:
				distances.append(math.sqrt(((self.x+1) - target[0])**2 + (self.y - target[1])**2))

			action = actions[distances.index(min(distances))]

		if action == 1:
			self.body.y -= self.speed
			self.y -= 1
		if action == 2:
			self.body.y += self.speed
			self.y += 1
		if action == 3:
			self.body.x -= self.speed
			self.x -= 1
		if action == 4:
			self.body.x += self.speed
			self.x += 1
		self.direction = action

	def start_pacgum_time(self):
		if self.etat != "eaten":
			self.etat = "frighten"
			self.couleur = (0, 0, 255)
			actions = [2, 1, 4, 3]
			self.direction = actions[self.direction-1]

	def end_pacgum_time(self):
		if self.etat != "eaten":
			self.etat = "chase"
			self.couleur = (255, 0, 0)

	def die(self):
		self.etat = "eaten"
		self.couleur = (255, 255, 255)

	def revive(self):
		self.etat = "chase"
		self.couleur = (255, 0, 0)
		actions = [2, 1, 4, 3]
		self.direction = actions[self.direction-1]

class inky(object):
	"""docstring for blinky"""
	def __init__(self, x, y, taille):
		super(inky, self).__init__()
		self.x = x
		self.y = y
		self.body = pygame.Rect(x*taille, y*taille, taille, taille)
		self.speed = taille
		self.direction = 1
		self.couleur  = (50, 50, 255)
		self.etat = "scatter"

	def move(self, joueur):
		action = 0
		actions = [1, 2, 3, 4]
		if [self.x, self.y] == [9, 8] and self.etat == "eaten":
			self.revive()
		if matrice[self.y-1][self.x] == 1 or self.direction == 2:
			actions.remove(1)
		if matrice[self.y+1][self.x] in [1, 4] or self.direction == 1:
			actions.remove(2)
		if matrice[self.y][self.x-1] in [1, 4] or self.direction == 4:
			actions.remove(3)
		if matrice[self.y][self.x+1] in [1, 4] or self.direction == 3:
			actions.remove(4)
		if self.etat == "frighten":
			action = actions[random.randint(0, len(actions)-1)]
		else:
			target = [0, 0]
			if self.etat == "chase":
				if joueur.direction == 1:
					target = [-(rouge.x-(joueur.x-2)), -(rouge.y-(joueur.y-2))]
				if joueur.direction == 2:
					target = [-(rouge.x-(joueur.x)), -(rouge.y-(joueur.y+2))]
				if joueur.direction == 3:
					target = [-(rouge.x-(joueur.x-2)), -(rouge.y-(joueur.y))]
				if joueur.direction == 4:
					target = [-(rouge.x-(joueur.x+2)), -(rouge.y-(joueur.y))]
			elif self.etat == "eaten":
				target = [9, 8]
			elif self.etat == "scatter":
				target = [19, 21]

			distances = []
			if 1 in actions:
				distances.append(math.sqrt((self.x - target[0])**2 + ((self.y-1) - target[1])**2))
			if 2 in actions:
				distances.append(math.sqrt((self.x - target[0])**2 + ((self.y+1) - target[1])**2))
			if 3 in actions:
				distances.append(math.sqrt(((self.x-1) - target[0])**2 + (self.y - target[1])**2))
			if 4 in actions:
				distances.append(math.sqrt(((self.x+1) - target[0])**2 + (self.y - target[1])**2))

			action = actions[distances.index(min(distances))]

		if action == 1:
			self.body.y -= self.speed
			self.y -= 1
		if action == 2:
			self.body.y += self.speed
			self.y += 1
		if action == 3:
			self.body.x -= self.speed
			self.x -= 1
		if action == 4:
			self.body.x += self.speed
			self.x += 1
		self.direction = action

	def start_pacgum_time(self):
		if self.etat != "eaten":
			self.etat = "frighten"
			self.couleur = (0, 0, 255)
			actions = [2, 1, 4, 3]
			self.direction = actions[self.direction-1]

	def end_pacgum_time(self):
		if self.etat != "eaten":
			self.etat = "chase"
			self.couleur = (50, 50, 255)

	def die(self):
		self.etat = "eaten"
		self.couleur = (255, 255, 255)

	def revive(self):
		self.etat = "chase"
		self.couleur = (50, 50, 255)
		actions = [2, 1, 4, 3]
		self.direction = actions[self.direction-1]

class pinky(object):
	"""docstring for blinky"""
	def __init__(self, x, y, taille):
		super(pinky, self).__init__()
		self.x = x
		self.y = y
		self.body = pygame.Rect(x*taille, y*taille, taille, taille)
		self.speed = taille
		self.direction = 1
		self.couleur  = (255, 100, 100)
		self.etat = "scatter"

	def move(self, joueur):
		action = 0
		actions = [1, 2, 3, 4]
		if [self.x, self.y] == [9, 8] and self.etat == "eaten":
			self.revive()
		if matrice[self.y-1][self.x] == 1 or self.direction == 2:
			actions.remove(1)
		if matrice[self.y+1][self.x] in [1, 4] or self.direction == 1:
			actions.remove(2)
		if matrice[self.y][self.x-1] in [1, 4] or self.direction == 4:
			actions.remove(3)
		if matrice[self.y][self.x+1] in [1, 4] or self.direction == 3:
			actions.remove(4)
		if self.etat == "frighten":
			action = actions[random.randint(0, len(actions)-1)]
		else:
			target = [0, 0]
			if self.etat == "chase":
				if joueur.direction == 1:
					target = [joueur.x-4, joueur.y-4]
				if joueur.direction == 2:
					target = [joueur.x, joueur.y+4]
				if joueur.direction == 3:
					target = [joueur.x-4, joueur.y]
				if joueur.direction == 4:
					target = [joueur.x+4, joueur.y]
			elif self.etat == "eaten":
				target = [9, 8]
			elif self.etat == "scatter":
				target = [0, 0]

			distances = []
			if 1 in actions:
				distances.append(math.sqrt((self.x - target[0])**2 + ((self.y-1) - target[1])**2))
			if 2 in actions:
				distances.append(math.sqrt((self.x - target[0])**2 + ((self.y+1) - target[1])**2))
			if 3 in actions:
				distances.append(math.sqrt(((self.x-1) - target[0])**2 + (self.y - target[1])**2))
			if 4 in actions:
				distances.append(math.sqrt(((self.x+1) - target[0])**2 + (self.y - target[1])**2))

			action = actions[distances.index(min(distances))]

		if action == 1:
			self.body.y -= self.speed
			self.y -= 1
		if action == 2:
			self.body.y += self.speed
			self.y += 1
		if action == 3:
			self.body.x -= self.speed
			self.x -= 1
		if action == 4:
			self.body.x += self.speed
			self.x += 1
		self.direction = action

	def start_pacgum_time(self):
		if self.etat != "eaten":
			self.etat = "frighten"
			self.couleur = (0, 0, 255)
			actions = [2, 1, 4, 3]
			self.direction = actions[self.direction-1]

	def end_pacgum_time(self):
		if self.etat != "eaten":
			self.etat = "chase"
			self.couleur = (255, 100, 100)

	def die(self):
		self.etat = "eaten"
		self.couleur = (255, 255, 255)

	def revive(self):
		self.etat = "chase"
		self.couleur = (255, 100, 100)
		actions = [2, 1, 4, 3]
		self.direction = actions[self.direction-1]

class clyde(object):
	"""docstring for blinky"""
	def __init__(self, x, y, taille):
		super(clyde, self).__init__()
		self.x = x
		self.y = y
		self.body = pygame.Rect(x*taille, y*taille, taille, taille)
		self.speed = taille
		self.direction = 1
		self.couleur  = (255, 200, 200)
		self.etat = "scatter"

	def move(self, joueur):
		action = 0
		actions = [1, 2, 3, 4]
		if [self.x, self.y] == [9, 8] and self.etat == "eaten":
			self.revive()
		if matrice[self.y-1][self.x] == 1 or self.direction == 2:
			actions.remove(1)
		if matrice[self.y+1][self.x] in [1, 4] or self.direction == 1:
			actions.remove(2)
		if matrice[self.y][self.x-1] in [1, 4] or self.direction == 4:
			actions.remove(3)
		if matrice[self.y][self.x+1] in [1, 4] or self.direction == 3:
			actions.remove(4)
		if self.etat == "frighten":
			action = actions[random.randint(0, len(actions)-1)]
		else:
			target = [0, 0]
			if self.etat == "chase":
				if math.sqrt((self.x - target[0])**2 + ((self.y-1) - target[1])**2) > 8:
					target = [joueur.x, joueur.y]
				else:
					target = [0, 21]
			elif self.etat == "eaten":
				target = [9, 8]
			elif self.etat == "scatter":
				target = [0, 21]

			distances = []
			if 1 in actions:
				distances.append(math.sqrt((self.x - target[0])**2 + ((self.y-1) - target[1])**2))
			if 2 in actions:
				distances.append(math.sqrt((self.x - target[0])**2 + ((self.y+1) - target[1])**2))
			if 3 in actions:
				distances.append(math.sqrt(((self.x-1) - target[0])**2 + (self.y - target[1])**2))
			if 4 in actions:
				distances.append(math.sqrt(((self.x+1) - target[0])**2 + (self.y - target[1])**2))

			action = actions[distances.index(min(distances))]

		if action == 1:
			self.body.y -= self.speed
			self.y -= 1
		if action == 2:
			self.body.y += self.speed
			self.y += 1
		if action == 3:
			self.body.x -= self.speed
			self.x -= 1
		if action == 4:
			self.body.x += self.speed
			self.x += 1
		self.direction = action

	def start_pacgum_time(self):
		if self.etat != "eaten":
			self.etat = "frighten"
			self.couleur = (0, 0, 255)
			actions = [2, 1, 4, 3]
			self.direction = actions[self.direction-1]

	def end_pacgum_time(self):
		if self.etat != "eaten":
			self.etat = "chase"
			self.couleur = (255, 200, 200)

	def die(self):
		self.etat = "eaten"
		self.couleur = (255, 255, 255)

	def revive(self):
		self.etat = "chase"
		self.couleur = (255, 200, 200)
		actions = [2, 1, 4, 3]
		self.direction = actions[self.direction-1]

running  = True

matrice = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 2, 1],
[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
[3, 3, 3, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 3, 3, 3],
[3, 3, 3, 1, 0, 1, 0, 1, 1, 4, 1, 1, 0, 1, 0, 1, 3, 3, 3],
[3, 3, 3, 1, 0, 0, 0, 1, 3, 3, 3, 1, 0, 0, 0, 1, 3, 3, 3],
[3, 3, 3, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 3, 3, 3],
[3, 3, 3, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 3, 3, 3],
[1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
[1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1],
[1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
taille = 20

rouge = blinky(9, 8, taille)
bleu = inky(9, 8, taille)
rose = pinky(9, 8, taille)
orange = clyde(9, 8, taille)
joueur = pacman(9, 16, taille)
PACGUMTIME = pygame.USEREVENT + 1
CHASE = pygame.USEREVENT + 1
SCATTER = pygame.USEREVENT + 1


pygame.init()
screen = pygame.display.set_mode((len(matrice[0])*taille, len(matrice)*taille))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)
pygame.time.set_timer(CHASE, 7000, loops=1)

init(taille)

while running:
	clock.tick(5)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == PACGUMTIME:
			joueur.end_pacgum_time()
			rouge.end_pacgum_time()
			bleu.end_pacgum_time()
			rose.end_pacgum_time()
			orange.end_pacgum_time()

		if event.type == SCATTER:
			if not rouge.etat not in ["eaten", "frighten"]:
				rouge.etat == "scatter"
			if not bleu.etat not in ["eaten", "frighten"]:
				bleu.etat == "scatter"
			if not rose.etat not in ["eaten", "frighten"]:
				rose.etat == "scatter"
			if not orange.etat not in ["eaten", "frighten"]:
				orange.etat == "scatter"
			pygame.time.set_timer(CHASE, 7000, loops=1)
			print("change")

		if event.type == CHASE:
			if not rouge.etat not in ["eaten", "frighten"]:
				rouge.etat == "chase"
			if not bleu.etat not in ["eaten", "frighten"]:
				bleu.etat == "chase"
			if not rose.etat not in ["eaten", "frighten"]:
				rose.etat == "chase"
			if not orange.etat not in ["eaten", "frighten"]:
				orange.etat == "chase"
			pygame.time.set_timer(SCATTER, 20000, loops=1)
			print("change")

	pygame.draw.rect(screen, (0, 0, 0), joueur.body)
	pygame.draw.rect(screen, (0, 0, 0), rouge.body)
	x = rouge.x
	y = rouge.y
	if matrice[y][x] == 0:
		pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x*taille + (taille/5)*2, y*taille + (taille/5)*2, taille/5, taille/5))
	elif matrice[y][x] == 2:
		pygame.draw.rect(screen, (255, 255, 200), pygame.Rect(x*taille + taille/3, y*taille + taille/3, taille/3, taille/3))
	elif matrice[y][x] == 4:
		pygame.draw.rect(screen, (150, 255, 255), pygame.Rect(x*taille, y*taille + (taille/5)*2, taille, taille/5))
	pygame.draw.rect(screen, (0, 0, 0), bleu.body)
	x = bleu.x
	y = bleu.y
	if matrice[y][x] == 0:
		pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x*taille + (taille/5)*2, y*taille + (taille/5)*2, taille/5, taille/5))
	elif matrice[y][x] == 2:
		pygame.draw.rect(screen, (255, 255, 200), pygame.Rect(x*taille + taille/3, y*taille + taille/3, taille/3, taille/3))
	elif matrice[y][x] == 4:
		pygame.draw.rect(screen, (150, 255, 255), pygame.Rect(x*taille, y*taille + (taille/5)*2, taille, taille/5))
	pygame.draw.rect(screen, (0, 0, 0), rose.body)
	x = rose.x
	y = rose.y
	if matrice[y][x] == 0:
		pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x*taille + (taille/5)*2, y*taille + (taille/5)*2, taille/5, taille/5))
	elif matrice[y][x] == 2:
		pygame.draw.rect(screen, (255, 255, 200), pygame.Rect(x*taille + taille/3, y*taille + taille/3, taille/3, taille/3))
	elif matrice[y][x] == 4:
		pygame.draw.rect(screen, (150, 255, 255), pygame.Rect(x*taille, y*taille + (taille/5)*2, taille, taille/5))
	pygame.draw.rect(screen, (0, 0, 0), orange.body)
	x = orange.x
	y = orange.y
	if matrice[y][x] == 0:
		pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x*taille + (taille/5)*2, y*taille + (taille/5)*2, taille/5, taille/5))
	elif matrice[y][x] == 2:
		pygame.draw.rect(screen, (255, 255, 200), pygame.Rect(x*taille + taille/3, y*taille + taille/3, taille/3, taille/3))
	elif matrice[y][x] == 4:
		pygame.draw.rect(screen, (150, 255, 255), pygame.Rect(x*taille, y*taille + (taille/5)*2, taille, taille/5))

	joueur.move(rouge, bleu, rose, orange)

	if joueur.body.colliderect(rouge.body):
		if joueur.invincible:
			rouge.die()
		else:
			running = False
	if joueur.body.colliderect(bleu.body):
		if joueur.invincible:
			bleu.die()
		else:
			running = False
	if joueur.body.colliderect(rose.body):
		if joueur.invincible:
			rose.die()
		else:
			running = False
	if joueur.body.colliderect(orange.body):
		if joueur.invincible:
			orange.die()
		else:
			running = False

	rouge.move(joueur)
	bleu.move(joueur)
	rose.move(joueur)
	orange.move(joueur)

	if joueur.body.colliderect(rouge.body):
		if joueur.invincible:
			rouge.die()
		else:
			running = False
	if joueur.body.colliderect(bleu.body):
		if joueur.invincible:
			bleu.die()
		else:
			running = False
	if joueur.body.colliderect(rose.body):
		if joueur.invincible:
			rose.die()
		else:
			running = False
	if joueur.body.colliderect(orange.body):
		if joueur.invincible:
			orange.die()
		else:
			running = False

	pygame.draw.rect(screen, joueur.couleur, joueur.body)
	pygame.draw.rect(screen, rouge.couleur, rouge.body)
	pygame.draw.rect(screen, bleu.couleur, bleu.body)
	pygame.draw.rect(screen, rose.couleur, rose.body)
	pygame.draw.rect(screen, orange.couleur, orange.body)
	pygame.display.flip()

print(joueur.point)