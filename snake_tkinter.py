import tkinter as tk
from random import randrange
'''
~ = might not be possible to do

Things to do:
fix (1)
fix(2)
~Accept key inputs during the 200ms wait time (3)
'''

"""Constants"""
INCREMENT = 15
GAME_SPEED = 200

class snake(tk.Canvas):
	def __init__(self, master, width, height):
		super().__init__(width=width, height=width, highlightthickness=0, background="white")
		self.WIDTH = width
		self.HEIGHT = height

		self.snake_pos = [(65, 15, 75, 25), (0, 0, 0, 0), (0, 0, 0, 0)]
		self.create_the_snake()

		self.score = -1
		self.create_text(self.WIDTH/2, 20, text=(self.score), font=("Pixel", 5), fill="grey", tag="text")

		self.move_fruit()
		self.key= "l"

		self.bind_all('<Key>', self.get_key)
		self.after(GAME_SPEED, self.game_clock)
		self.pack()

	def create_the_snake(self):
		for individual_snake_block in self.snake_pos:
			self.create_rectangle(*individual_snake_block, tag="snake", fill="black") #x1, y1, x2, y2


	def move_snake(self): 
		head_x1, head_y1, head_x2, head_y2 = self.snake_pos[0]

		if self.key == "l":   new_head = (head_x1 + INCREMENT, head_y1, head_x2 + INCREMENT, head_y2)
		elif self.key == "i": new_head = (head_x1, head_y1 - INCREMENT, head_x2, head_y2 - INCREMENT)
		elif self.key == "j": new_head = (head_x1 - INCREMENT, head_y1, head_x2 - INCREMENT, head_y2)
		elif self.key == "k": new_head = (head_x1, head_y1 + INCREMENT, head_x2, head_y2 + INCREMENT)

		"""Adding a block to the snake if the snake head == fruit_cordinates"""
		if self.snake_pos[0] == self.fruit_pos:
			self.create_rectangle(*self.snake_pos[0], fill="black", tag="snake")
			self.snake_pos = [new_head]	 + self.snake_pos
			self.move_fruit()

			"""Removing the last block and adding a new head"""
		else:
			self.snake_pos = [new_head]	 + self.snake_pos[:-1]

		for snake_object, expected_pos in zip(self.find_withtag("snake"), self.snake_pos):
			self.coords(snake_object, *expected_pos)

	def game_clock(self):
		self.move_snake()
		self.check_collsion()
		self.after(GAME_SPEED, self.game_clock) #(3)

	def check_collsion(self):
		if self.snake_pos[0] in self.snake_pos[1:]:
			self.quit()
			"""(1)!!! the pixel x and y size of the screen needs to be the same atm"""
		for number in self.snake_pos[0]:
			if number > self.WIDTH or number < 0:
				self.quit()

	def move_fruit(self):
		self.delete("fruit")
		self.fruit_pos = self.random_fruit_pos()
		self.create_rectangle(*self.fruit_pos, fill="red", tag="fruit")
		self.score += 1
		self.itemconfig("text", text=self.score)

	def random_fruit_pos(self):
			while True:
				random_location = float(randrange(30, self.WIDTH, 30)) #min size, screen size, step size
				e = random_location-10, random_location-30, random_location, random_location-20	
				if e not in self.snake_pos:
					return e	

	def get_key(self, event):
		if event.char in ["i", "l", "k", "j"]:
			"""prohibits the snake from killing itself
			(2)!!! curently a bug that allows the snake to kill itself if you press 2 buttons at
			the same time"""
			if not self.key == "l" and event.char == "j":
				self.key = event.char
			elif not self.key == "k" and event.char == "i":
				self.key = event.char
			elif not self.key == "j" and event.char == "l":
				self.key = event.char
			elif not self.key == "i" and event.char == "k":
				self.key = event.char


