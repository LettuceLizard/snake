#Main menu
import tkinter as tk
from snake_tkinter import snake

def main():
	"""Setup"""
	root = tk.Tk()
	root.title("snake")
	root.tk.call("tk", "scaling", 4.0)
	root.resizable(False, False)
	
	app = snake(root)

	root.mainloop()




if __name__ == '__main__':
	main()