#snake not oob
import tkinter as tk
from random import choice

SIZE = 5
INCREMENT = 13
GAME_SPEED = 200
class snake(tk.Canvas):
	def __init__(self, master):
		super().__init__(width=600, height=600, highlightthickness=0, background="white")

		self.snake_pos = [(125, 105, 115, 95), (120, 105, 110, 95), (105, 105, 95, 95)]
		self.food_pos = (150, 150)
		self.key= "l"
		self.after(GAME_SPEED, self.game_clock)
		self.bind_all('<Key>', self.get_key)

		self.create_objects()
		

		self.pack()

	def create_objects(self):
		"""(x_pos, y_pos) är mitten av kvadraten, SIZE är från mitt punkten tills kvadraten är ritad (radius)""" 
		for individual_snake_block in self.snake_pos:
			self.create_rectangle(*individual_snake_block, tag="snake", fill="black") #x1, y1, x2, y2

			self.create_rectangle(self.food_pos[0]+SIZE, self.food_pos[1]+SIZE, self.food_pos[0]-SIZE, \
				self.food_pos[1]-SIZE, tag="food", fill="red")

	def move_snake(self): 
		head_x1, head_y1, head_x2, head_y2 = self.snake_pos[0]

		if self.key == "l":
			new_head = (head_x1 + INCREMENT, head_y1, head_x2 + INCREMENT, head_y2)
		elif self.key == "i":
			new_head = (head_x1, head_y1 - INCREMENT , head_x2, head_y2 - INCREMENT)
		elif self.key == "j":
			new_head = (head_x1 - INCREMENT, head_y1, head_x2 - INCREMENT, head_y2)
		elif self.key == "k":
			new_head = (head_x1, head_y1 + INCREMENT, head_x2, head_y2 + INCREMENT)

		self.snake_pos = [new_head]	 + self.snake_pos[:-1]
		for current_pos, expected_pos in zip(self.find_withtag("snake"), self.snake_pos):
			# print(current_pos, expected_pos)
			self.coords(current_pos, *expected_pos)

	def game_clock(self):
		self.move_snake()
		self.after(GAME_SPEED, self.game_clock)

	def get_key(self, event):
		if event.char in ["i", "l", "k", "j"]:
			self.key = event.char
		# print(self.key)



	# def convert_format(self, all_cordinates):
	# 	for x, y in all_cordinates:

	# 	return x+SIZE, y+SIZE, x-SIZE, y-SIZE


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