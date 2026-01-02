import pygame
import random
from math import *

longeur_écran = 600
hauteur_écran = 600
speed = 8
longeur = 100
tailleb = 10

direction = 1

x = longeur_écran/2
y = 550

xb = x
yb = y-100

speedy = 4
speedx = random.randint(-speedy*1.5, speedy*1.5)
if speedx == 0:
	speedx = 1

paddle = pygame.Rect(x, y, longeur, 10)

balle = pygame.Rect(xb, yb, tailleb, tailleb)

# paramètres des blocs
nb_blocs_ligne = 8
nb_lignes = 5
largeur_bloc = longeur_écran // nb_blocs_ligne
hauteur_bloc = 20

# liste pour stocker les blocs
blocs = []
for ligne in range(nb_lignes):
	for col in range(nb_blocs_ligne):
		bloc = pygame.Rect(col * largeur_bloc, ligne * hauteur_bloc, largeur_bloc, hauteur_bloc)
		blocs.append(bloc)


pygame.init()
screen = pygame.display.set_mode((longeur_écran, hauteur_écran))
pygame.display.set_caption("casse bloc")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)

running = True
while running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]: x -= speed
	if keys[pygame.K_RIGHT]: x += speed

	xb -= speedx
	yb -= speedy

	if x < 0:
		x = 0
	if x > longeur_écran - longeur:
		x = longeur_écran - longeur

	if yb - tailleb <= 0:
		speedy = -speedy  # inversion de la direction verticale

	if paddle.colliderect(balle) and speedy < 0:
		speedy = -speedy
		speedx = ((x+longeur/2)-xb)/4


	if xb - tailleb <= 0 or xb + tailleb >= longeur_écran:
		speedx = -speedx  # inversion de la direction verticale

	if yb + tailleb >= hauteur_écran:
		running = False

	paddle = pygame.Rect(x, y, longeur, 10)

	balle = pygame.Rect(xb, yb, tailleb, tailleb)

	screen.fill((0, 0, 0))

	pygame.draw.rect(screen, (255, 255, 255), paddle)

	pygame.draw.rect(screen, (255, 255, 255), balle)

	for bloc in blocs[:]:  # [:] = copie pour pouvoir enlever pendant qu’on parcourt
		if balle.colliderect(bloc):
			blocs.remove(bloc)
			speedy = -speedy  # la balle rebondit
			break

	for bloc in blocs:
		pygame.draw.rect(screen, (200, 0, 0), bloc)  # couleur rouge
		pygame.draw.rect(screen, (255, 255, 255), bloc, 2)  # contour blanc

	pygame.display.flip()

pygame.quit()
