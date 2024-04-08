# reference: https://github.com/baraltech/Menu-System-PyGame

# CONTROLLER
class Button():

	def __init__(self, pos, input, font, base, hover):
		self.x = pos[0]
		self.y = pos[1]
		self.font = font
		self.base, self.hover = base, hover
		self.input = input
		self.text = self.font.render(self.input, True, self.base)
		self.rect = self.text.get_rect(center=(self.x, self.y))

	def update(self, screen):
		screen.blit(self.text, self.rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.input, True, self.hover)
		else:
			self.text = self.font.render(self.input, True, self.base)
