import pygame
import random

longeur_écran = 600
hauteur_écran = 600
speed = 40
taille = 40

direction = 1

x = longeur_écran/2
y = hauteur_écran/2

xp = random.randint(taille, longeur_écran-taille)
yp = random.randint(taille, hauteur_écran-taille)

tete = pygame.Rect(x, y, taille, taille)

corps = []

pomme = pygame.Rect(xp, yp, taille, taille)


pygame.init()
screen = pygame.display.set_mode((longeur_écran, hauteur_écran))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)

running = True
while running:
	clock.tick(6)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	if len(corps) != 0:
		corps.pop(-1)
		corps.insert(0, pygame.Rect(x, y, taille, taille))


	keys = pygame.key.get_pressed()

	if keys[pygame.K_UP]: direction = 1
	if keys[pygame.K_DOWN]: direction = 2
	if keys[pygame.K_LEFT]: direction = 3
	if keys[pygame.K_RIGHT]: direction = 4

	if direction == 1: y -= speed
	if direction == 2: y += speed
	if direction == 3: x -= speed
	if direction == 4: x += speed

	'''
	
	if y < 0:
		break
	if y > hauteur_écran - taille:
		running = False
	if x < 0:
		break
	if x > longeur_écran - taille:
		running = False
	'''
	
	if tete.colliderect(pomme):
		if len(corps) != 0:
			corps.append(corps[-1])
		else:
			corps.append(pygame.Rect(-taille-10, -taille-10, taille, taille))
		xp = random.randint(taille, longeur_écran-taille)
		yp = random.randint(taille, hauteur_écran-taille)

	screen.fill((0, 0, 0))


	pomme = pygame.Rect(xp, yp, taille, taille)
	tete = pygame.Rect(x, y, taille, taille)

	for partie in corps:
		pygame.draw.rect(screen, (0, 255, 0), partie)
		# if tete.colliderect(partie):
			# running = False

	pygame.draw.rect(screen, (0, 155, 0), tete)

	pygame.draw.rect(screen, (255, 0, 0), pomme)

	pygame.display.flip()

pygame.quit()

print(len(corps))
