#snake not oob
import tkinter as tk
from random import randint

class snake(tk.Canvas):
	def __init__(self, master):
		super().__init__(width=600, height=600, highlightthickness=0)

		self.snake_positions = [(100, 100), (115, 100), (130, 100)]

		self.draw_snake_rect()

		self.pack()

	def draw_snake_rect(self):
		for x_pos, y_pos in self.snake_positions:
			size = 6
			self.create_rectangle(x_pos+size, y_pos+size, x_pos-size, y_pos-size) #x1, y1, x2, y2

		
 


def main():
	root = tk.Tk()
	root.title("snake")
	root.tk.call("tk", "scaling", 4.0)
	root.resizable(False, False)

	app = snake(root)

	root.mainloop()






if __name__ == '__main__':
	main()