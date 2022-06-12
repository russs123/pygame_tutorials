import pygame

class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, width, height, scale):
		image = self.sheet.subsurface((frame * width, 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))

		return image
