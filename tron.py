import pygame

def out_of_bounds(x, y):
    return x < 0 or x > longeur_écran or y < 0 or y > hauteur_écran

longeur_écran = 600
hauteur_écran = 600
speed = 2

directions = {
    1: (0, -1),
    2: (0, 1),
    3: (-1, 0),
    4: (1, 0)
}
direction_1 = 2
direction_2 = 1

dx1 = 0
dy1 = 0

dx2 = 0
dy2 = 0

x1 = longeur_écran/4
y1 = hauteur_écran/4

x2 = longeur_écran/4*3
y2 = hauteur_écran/4*3


joueur1 = pygame.Surface((10, 5), pygame.SRCALPHA)
pygame.draw.rect(joueur1, (0, 0, 255), (0, 0, 10, 5))
angle1 = 90

joueur1_cache = pygame.Surface((10, 5), pygame.SRCALPHA)
pygame.draw.rect(joueur1_cache, (0, 0, 0), (0, 0, 10, 5))

joueur2 = pygame.Surface((10, 5), pygame.SRCALPHA)
pygame.draw.rect(joueur2, (255, 0, 0), (0, 0, 10, 5))
angle2 = 90

joueur2_cache = pygame.Surface((10, 5), pygame.SRCALPHA)
pygame.draw.rect(joueur2_cache, (0, 0, 0), (0, 0, 10, 5))

trainee_1 = [pygame.Rect(-5, -5, 2, 2), pygame.Rect(-5, -5, 2, 2), pygame.Rect(-5, -5, 2, 2), pygame.Rect(-5, -5, 2, 2), pygame.Rect(-5, -5, 2, 2)]
trainee_2 = [pygame.Rect(-5, -5, 2, 2), pygame.Rect(-5, -5, 2, 2), pygame.Rect(-5, -5, 2, 2), pygame.Rect(-5, -5, 2, 2), pygame.Rect(-5, -5, 2, 2)]


pygame.init()
screen = pygame.display.set_mode((longeur_écran, hauteur_écran))
pygame.display.set_caption("tron")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)

running = True
while running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	rotated_surface1_cache = pygame.transform.rotate(joueur1_cache, angle1)
	rect1_cache = rotated_surface1_cache.get_rect(center=(x1, y1))

	screen.blit(rotated_surface1_cache, rect1_cache)

	rotated_surface2_cache = pygame.transform.rotate(joueur2_cache, angle2)
	rect2_cache = rotated_surface2_cache.get_rect(center=(x2, y2))

	screen.blit(rotated_surface2_cache, rect2_cache)

	keys = pygame.key.get_pressed()

	if keys[pygame.K_z] and not direction_1 == 2: 
		direction_1 = 1
		angle1 = 90
	if keys[pygame.K_s] and not direction_1 == 1: 
		direction_1 = 2
		angle1 = 90
	if keys[pygame.K_q] and not direction_1 == 4: 
		direction_1 = 3
		angle1 = 0
	if keys[pygame.K_d] and not direction_1 == 3: 
		direction_1 = 4
		angle1 = 0

	keys = pygame.key.get_pressed()

	if keys[pygame.K_UP] and not direction_2 == 2: 
		direction_2 = 1
		angle2 = 90
	if keys[pygame.K_DOWN] and not direction_2 == 1: 
		direction_2 = 2
		angle2 = 90
	if keys[pygame.K_LEFT] and not direction_2 == 4: 
		direction_2 = 3
		angle2 = 0
	if keys[pygame.K_RIGHT] and not direction_2 == 3: 
		direction_2 = 4
		angle2 = 0

	dx1, dy1 = directions[direction_1]

	x1 += dx1 * speed
	y1 += dy1 * speed

	dx2, dy2 = directions[direction_2]

	x2 += dx2 * speed
	y2 += dy2 * speed

	
	if out_of_bounds(x1, y1) or out_of_bounds(x2, y2):
		running = False
	'''
	'''

#	screen.fill((x1, y1, 0))

	rotated_surface1 = pygame.transform.rotate(joueur1, angle1)
	rect1 = rotated_surface1.get_rect(center=(x1, y1))

	screen.blit(rotated_surface1, rect1)

	rotated_surface2 = pygame.transform.rotate(joueur2, angle2)
	rect2 = rotated_surface2.get_rect(center=(x2, y2))

	screen.blit(rotated_surface2, rect2)

	trainee_1.append(pygame.Rect(x1, y1, 2, 2))

	trainee_2.append(pygame.Rect(x2, y2, 2, 2))


	for i in range(0, len(trainee_1)-5):
		# pygame.draw.rect(screen, (0, 0, 255), trainee_1[i])
		# pygame.draw.rect(screen, (255, 0, 0), trainee_2[i])
		if trainee_1[i].colliderect(rect1) or trainee_1[i].colliderect(rect2) or trainee_2[i].colliderect(rect1) or trainee_2[i].colliderect(rect2):
			running = False

	pygame.draw.rect(screen, (0, 0, 255), trainee_1[-5])
	pygame.draw.rect(screen, (255, 0, 0), trainee_2[-5])
	pygame.draw.rect(screen, (0, 0, 255), trainee_1[-6])
	pygame.draw.rect(screen, (255, 0, 0), trainee_2[-6])

	pygame.display.flip()

pygame.quit()

