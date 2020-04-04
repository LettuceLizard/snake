import tkinter as tk
from random import randrange
"""Constants"""
INCREMENT = 15
GAME_SPEED = 200
WIDTH = 300
HEIGHT = 300

class snake(tk.Canvas):
	def __init__(self, master):
		super().__init__(width=WIDTH, height=HEIGHT, highlightthickness=0, background="white")

		self.snake_pos = [self.random_square(), (0, 0, 0, 0) , (0, 0, 0, 0)]
		self.fruit_pos = self.random_square()
		self.key= "l"
		self.after(GAME_SPEED, self.game_clock)
		self.bind_all('<Key>', self.get_key)

		self.create_objects()
		

		self.pack()

	def create_objects(self):
		for individual_snake_block in self.snake_pos:
			self.create_rectangle(*individual_snake_block, tag="snake", fill="black") #x1, y1, x2, y2

			self.create_rectangle(*self.fruit_pos, tag="fruit", fill="red")

	def move_snake(self): 
		head_x1, head_y1, head_x2, head_y2 = self.snake_pos[0]

		if self.key == "l":   new_head = (head_x1 + INCREMENT, head_y1, head_x2 + INCREMENT, head_y2)
		elif self.key == "i": new_head = (head_x1, head_y1 - INCREMENT, head_x2, head_y2 - INCREMENT)
		elif self.key == "j": new_head = (head_x1 - INCREMENT, head_y1, head_x2 - INCREMENT, head_y2)
		elif self.key == "k": new_head = (head_x1, head_y1 + INCREMENT, head_x2, head_y2 + INCREMENT)

		"""Adding a block to the snake if the snake head == fruit_cordinates"""
		if self.snake_pos[0] == self.fruit_pos:
			print(self.snake_pos[0], self.fruit_pos) 
			self.create_rectangle(*self.snake_pos[0], fill="black", tag="snake")
			self.snake_pos = [new_head]	 + self.snake_pos

			self.move_fruit()

			"""Removing the last block and adding a new head"""
		else:
			self.snake_pos = [new_head]	 + self.snake_pos[:-1]


		for current_pos, expected_pos in zip(self.find_withtag("snake"), self.snake_pos):
			self.coords(current_pos, *expected_pos)

	def game_clock(self):
		self.move_snake()
		self.check_collsion()
		# print(self.snake_pos)
		self.after(GAME_SPEED, self.game_clock)

	def check_collsion(self):
		if self.snake_pos[0] in self.snake_pos[1:]:
			self.quit()
		

	def move_fruit(self):
		self.delete("fruit")
		self.fruit_pos = self.random_square()
		self.create_rectangle(*self.fruit_pos, fill="red", tag="fruit")

	def random_square(self):
		random_location = randrange(30, WIDTH, 30) #min size, screen size, step size
		return random_location-10, random_location-30, random_location, random_location-20


	def get_key(self, event):
		if event.char in ["i", "l", "k", "j"]:
			self.key = event.char

def main():
	"""Setup"""
	root = tk.Tk()
	root.title("snake")
	root.tk.call("tk", "scaling", 4.0)
	root.resizable(False, False)
	"""Main"""

	app = snake(root)

	root.mainloop()






if __name__ == '__main__':
	main()