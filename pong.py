import pygame
import random

max_speed = 10
accélération = 1
longeur_écran = 800
hauteur_écran = 600
vitesse_début = 6



x, y = 100, 300
x2, y2 = 700, 300
speed = 10
taille = 150

taille_balle = 20
xb = longeur_écran/2
yb = hauteur_écran/2
vxb = random.randint(-vitesse_début, vitesse_début)  # vitesse en X
vyb = random.randint(-vitesse_début, vitesse_début)   #vitesse en Y
if vxb == 0:
	vxb = 1
couleur_balle = (255, 255, 255)

paddle = pygame.Rect(x, y, 10, 150)
paddle2 = pygame.Rect(x2, y2, 10, 150)
balle = pygame.Rect(xb, yb, taille_balle, taille_balle)

point1 = 0
point2 = 0

pygame.init()
screen = pygame.display.set_mode((longeur_écran, hauteur_écran))
pygame.display.set_caption("pong")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)

running = True
while running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	xb += vxb
	yb += vyb

	keys = pygame.key.get_pressed()
	if keys[pygame.K_z]: y -= speed
	if keys[pygame.K_s]: y += speed

	if keys[pygame.K_UP]: y2 -= speed
	if keys[pygame.K_DOWN]: y2 += speed

	if balle.colliderect(paddle):
		if vxb < 0:
			vxb = -vxb
			if vxb < 0 and vxb > -max_speed:
				vxb -= accélération
			if vxb > 0 and vxb < max_speed:
				vxb += accélération
			vyb = ((y+taille/2)-yb)/4


	if balle.colliderect(paddle2):
		if vxb > 0:
			vxb = -vxb
			if vxb < 0 and vxb > -max_speed:
				vxb -= accélération
			if vxb > 0 and vxb < max_speed:
				vxb += accélération
			vyb = ((y2+taille/2)-yb)/4

	if xb - taille_balle <= 0:
		point2 += 1
		xb = longeur_écran/2
		yb = hauteur_écran/2
		vxb = random.randint(-vitesse_début, vitesse_début)  # vitesse en X
		vyb = random.randint(-vitesse_début, vitesse_début)   #vitesse en Y
		if vxb == 0:
			vxb = 1

	if xb + taille_balle >= longeur_écran:
		point1 += 1
		xb = longeur_écran/2
		yb = hauteur_écran/2
		vxb = random.randint(-vitesse_début, vitesse_début)  # vitesse en X
		vyb = random.randint(-vitesse_début, vitesse_début)   #vitesse en Y
		if vxb == 0:
			vxb = 1

	if yb - taille_balle <= 0 or yb + taille_balle >= hauteur_écran:
		vyb = -vyb  # inversion de la direction verticale
		if vyb < 0 and vyb > -max_speed:
			vyb -= accélération
		if vyb > 0 and vyb < max_speed:
			vyb += accélération

	if y < 0:
		y = 0
	if y > hauteur_écran - taille:
		y = hauteur_écran - taille

	if y2 < 0:
		y2 = 0
	if y2 > hauteur_écran - taille:
		y2 = hauteur_écran - taille


	screen.fill((0, 0, 0))

	paddle = pygame.Rect(x, y, 20, 150)
	paddle2 = pygame.Rect(x2, y2, 20, 150)
	balle = pygame.Rect(xb, yb, taille_balle, taille_balle)

	pygame.draw.rect(screen, (255, 255, 255), paddle)

	pygame.draw.rect(screen, (255, 255, 255), paddle2)

	pygame.draw.rect(screen, (255, 255, 255), balle)

	texte = font.render(f"{point1} | {point2}", True, (255, 255, 255))
	screen.blit(texte, (longeur_écran/2-20, 50))  # Affiche le texte à l'écran

	pygame.display.flip()

pygame.quit()
