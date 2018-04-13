import pygame
import colorsys
import math
import numpy
import random

UP = [0,1]
RIGHT = [1,0]
DOWN = [0,-1]
LEFT = [-1,0]
direction = [UP,RIGHT,DOWN,LEFT]

class turtle(object):
	def __init__(self, coords):
		self.coords = coords
		self.last = coords
		self.dire = 1
		self.point = None

	def draw(self,color=[255,255,255]):
		pygame.draw.line(screen,color,[self.last[0]*(boxSize)+boxSize/2,self.last[1]*boxSize+boxSize/2],[self.coords[0]*boxSize+boxSize/2,self.coords[1]*boxSize+boxSize/2],1)

	def forward(self):
		self.last = self.coords[:]
		self.coords[0]+= direction[self.dire][0]
		self.coords[1]+= direction[self.dire][1]

	def rightTurn(self):
		self.dire+=1
		self.dire%=4
	def leftTurn(self):
		self.dire-=1
		if self.dire < 0:
			self.dire = 3
	def Point(self):
		self.point = [int(self.coords[0]*boxSize+boxSize/2),int(self.coords[1]*boxSize+boxSize/2)]
		
		

def map(value,changed,og):
	return (value-changed[0])*(float(og[1]-og[0])/float(changed[1]-changed[0]))+og[0]


pygame.init()
WHITE= [255, 255, 255]
backgroundSize = [1024,1024]
MID = [backgroundSize[0]/2,backgroundSize[1]/2]
screen = pygame.display.set_mode(backgroundSize)
pygame.display.set_caption("Hilbert Curve")
clock = pygame.time.Clock()
L = "+rF-LFL-Fr+"
R = "-LF+RFR+FL-"

done = False
Log = int(math.log(backgroundSize[0])/math.log(2))

randomPoint = random.randint(0,1000)/1000.0
print randomPoint

for iteration in range(Log+1):
	screen.fill(0)
	boxSize=2**(Log-iteration)
	tim = turtle([0,backgroundSize[1]/boxSize-1])
	movement = "L"
	for i in range(iteration):
		movement = movement.replace("L",L).replace("R",R).replace("r","R")
	movement = movement.replace("R","").replace("L","").replace("+-","").replace("-+","")
	length = movement.count("F")
	count = 0
	for i in movement:
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				done = True
		if done:
			break 
		if i == "F":
			tim.forward()
			count+=1
			tim.draw(colorsys.hsv_to_rgb(map(count,[0,length],[0,1]),1,255))
			
		elif i == "+":
			tim.rightTurn()
		elif i == "-":
			tim.leftTurn()
		if count == int(length*randomPoint):
			tim.Point()
		if tim.point:	
			pygame.draw.circle(screen,WHITE,tim.point,5)
	pygame.display.flip()
	clock.tick(1)
	if done:
		break 





	
