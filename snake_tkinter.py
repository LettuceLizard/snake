#snake not oob
import tkinter as tk
from random import choice

SIZE = 6
INCREMENT = 10
class snake(tk.Canvas):
	def __init__(self, master):
		super().__init__(width=600, height=600, highlightthickness=0)

		self.snake_pos = [(130, 100), (115, 100), (100, 100)]
		self.food_pos = (150, 150)

		self.create_objects()
		self.move_snake()
		

		self.pack()

	def create_objects(self):
		"""(x_pos, y_pos) är mitten av kvadraten, SIZE är från mitt punkten tills kvadraten är ritad (radius)""" 
		for x_pos, y_pos in self.snake_pos:
			self.create_rectangle(x_pos+SIZE, y_pos+SIZE, x_pos-SIZE, y_pos-SIZE, tag="snake") #x1, y1, x2, y2

			self.create_rectangle(self.food_pos[0]+SIZE, self.food_pos[1]+SIZE, self.food_pos[0]-SIZE, \
				self.food_pos[1]-SIZE, tag="food", fill="red")

	def move_snake(self):
		head_x, head_y = self.snake_pos[0]

		new_head = (head_x + INCREMENT, head_y)
		self.snake_pos = [new_head]	 + self.snake_pos[:-1]
		print(self.snake_pos)


		

 

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