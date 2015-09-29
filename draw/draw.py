import turtle

def draw_square(mover):	
	for i in range(1, 5):
		mover.forward(100)
		mover.right(120)
		

def draw_final():
	window = turtle.Screen()
	window.bgcolor("blue")

	mover1 = turtle.Turtle()
	mover1.shape("circle")
	mover1.color("yellow")
	mover1.speed(0)

	angle = 10
	#times = 360 / angle

	for i in range(0, 360 / angle):
		draw_square(mover1)
		mover1.right(angle)

	window.exitonclick()

draw_final()
