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

def get_lookup():
	
	tim = turtle([0,backgroundSize[1]/boxSize-1])
	movement = "L"
	for i in range(iterations):
		movement = movement.replace("L",L).replace("R",R).replace("r","R")
	movement = movement.replace("R","").replace("L","").replace("+-","").replace("-+","")
	length = movement.count("F")
	count = 0
	lookUp = []
	for i in movement:
		if i == "F":
			tim.forward()
			# tim.draw()
			lookUp.append(tim.last)
		elif i == "+":
			tim.rightTurn()
		elif i == "-":
			tim.leftTurn()
		# pygame.display.flip()
	return lookUp

iterations = 9
pygame.init()
WHITE= [255, 255, 255]
backgroundSize = [2**iterations,2**iterations]
MID = [backgroundSize[0]/2,backgroundSize[1]/2]
screen = pygame.display.set_mode(backgroundSize)
pygame.display.set_caption("Hilbert Curve")
clock = pygame.time.Clock()
L = "+rF-LFL-Fr+"
R = "-LF+RFR+FL-"
boxSize = 1
userImage = pygame.image.load('superman.jpg')
userImage = pygame.transform.scale(userImage,backgroundSize)

lookUp = get_lookup()

screen.blit(userImage,[0,0])
# pygame.display.flip()
sound = []
for i in lookUp:
	sound.append(sum(screen.get_at(i)[0:3])/3)
	# temp = sum(screen.get_at(i)[0:3])/3
	# screen.set_at(i,[temp,temp,temp])
pygame.display.flip()

########
# TODO #
# Turn sound array into sound #

done = False
while not done:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True





	
