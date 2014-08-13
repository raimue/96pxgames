# -*- coding: utf8 -*- 

from gameobject import *
from animation import *

class Sprite(GameObject):
	def __init__(self, spriteData, duration, loop):
		GameObject.__init__(self)

		self.spriteData = spriteData
		self.isDead = False
		self.indexAnimation = Animation(0, len(self.spriteData), duration, loop)

	def update(self, dt):
		GameObject.update(self, dt)

		self.indexAnimation.update(dt)

		self.isDead = self.indexAnimation.ended

	def draw(self, rgb):
		print "draw"
		if not self.indexAnimation.ended:
			index = int(self.indexAnimation.getValue())
			if index >= len(self.spriteData) or index < 0:
				print "[ERROR] index out of bounds (index: ",index,", len(spriteData):",len(self.spriteData),")"
				return
			
			for pixel in self.spriteData[index]:
				#TODO: wrap around
				rgb.setPixel(self.position + pixel['position'], pixel['color'])
		print "enddraw"

