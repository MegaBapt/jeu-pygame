import turtle
import keyboard
import math

def collision(x, y, trace):
    for px, py in trace:
        if math.hypot(px - x, py - y) < 1:  # distance seuil
            return True
    return False

def out_of_bounds(x, y):
	return x < -screen.window_width()/2 or x > screen.window_width()/2 or y < -screen.window_height()/2 or y > screen.window_height()/2

def carré(t, speed):
	t.begin_fill()
	for _ in range(4):
		t.right(90)
		for _ in range(16):
			t.forward(speed)
			x, y = t.position()
	t.end_fill()

longeur = 90
zoom = 1

screen = turtle.Screen()
'''
zoom = 100*zoom
screen.setworldcoordinates(-zoom, -zoom, zoom, zoom)
'''

t1 = turtle.Turtle()
t1.speed(0)
t1.penup()
t1.goto(-100, -100)
t1.pendown() 
t1.color("red")
t1.setheading(90)   # vers le haut (Nord)2
t1.begin_fill()

t2 = turtle.Turtle()
t2.speed(0)
t2.penup()
t2.goto(100, 100)
t2.pendown()
t2.color("blue")
t2.setheading(270)  # vers le bas (Sud)4
t2.begin_fill()

speed = 2

last_x1 = -100
last_y1 = -100

last_x2 = 100
last_y2 = 100

trace1 = []
trace2 = []

last_trace1 = []
last_trace2 = []

direction_1 = 2
direction_2 = 1

'''
t.setheading(0)	# vers la droite (Est)1
t.setheading(90)   # vers le haut (Nord)2
t.setheading(180)  # vers la gauche (Ouest)3
t.setheading(270)  # vers le bas (Sud)4
'''

carré(t1, speed)
carré(t2, speed)

running = True
while running:

	if keyboard.is_pressed('z') and not direction_1 == 2: 
		direction_1 = 1
		t1.setheading(90)   # vers le haut (Nord)2
	if keyboard.is_pressed('s') and not direction_1 == 1: 
		direction_1 = 2
		t1.setheading(270)  # vers le bas (Sud)4
	if keyboard.is_pressed('q') and not direction_1 == 4: 
		direction_1 = 3
		t1.setheading(180)  # vers la gauche (Ouest)3
	if keyboard.is_pressed('d') and not direction_1 == 3: 
		direction_1 = 4
		t1.setheading(0)

	if keyboard.is_pressed('up') and not direction_2 == 2: 
		direction_2 = 1
		t2.setheading(90)   # vers le haut (Nord)2
	if keyboard.is_pressed('down') and not direction_2 == 1: 
		direction_2 = 2
		t2.setheading(270)  # vers le bas (Sud)4
	if keyboard.is_pressed('left') and not direction_2 == 4: 
		direction_2 = 3
		t2.setheading(180)  # vers la gauche (Ouest)3
	if keyboard.is_pressed('right') and not direction_2 == 3: 
		direction_2 = 4
		t2.setheading(0)

	x1, y1 = t1.position()

	if collision(x1, y1, trace1):
		t1.goto(last_x1, y1)
		t1.goto(last_x1, last_y1)
		t1.end_fill()
		t1.goto(x1, y1)
		last_x1 = x1
		last_y1 = y1
		last_trace1 = []
		t1.begin_fill()

	trace1.append((x1, y1))
	last_trace1.append((x1, y1))

	x2, y2 = t2.position()

	if collision(x2, y2, trace2):
		t2.goto(last_x2, y2)
		t2.goto(last_x2, last_y2)
		t2.end_fill()
		t2.goto(x2, y2)
		last_x2 = x2
		last_y2 = y2
		last_trace2 = []
		t2.begin_fill()

	trace2.append((x2, y2))
	last_trace2.append((x2, y2))



	t1.forward(speed)
	t2.forward(speed)

	
	if out_of_bounds(x1, y1) or out_of_bounds(x2, y2) or collision(x1, y1, last_trace2) or collision(x2, y2, last_trace1) :
		running = False

turtle.done()
keyboard.unhook_all()
