#Main menu
import tkinter as tk
from snake_tkinter import snake

WIDTH = 300
HEIGHT = 300


# class Main_menu(tk.Frame):
# 	super().__init__(self)
# 	pass

def main():
	"""Setup"""
	root = tk.Tk()
	root.title("snake")
	root.tk.call("tk", "scaling", 4.0)
	root.resizable(False, False)
	
	app = snake(root, WIDTH, HEIGHT)

	root.mainloop()




if __name__ == '__main__':
	main()