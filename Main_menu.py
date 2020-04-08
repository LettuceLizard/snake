#Main menu
import tkinter as tk
from snake_tkinter import snake

'''
Things to do:
figure out why the program creates 2 windows?
	-The problem was that the instanse of the object snake is the Canvas
'''
WIDTH = 300	
HEIGHT = 300

# class main_menu(tk.Frame):
# 	def __init__(self, master):
# 		super().__init__(width=600, height=600, background="white")
# 		self.Button(master, text="yeet")


def clearwin(event=None):
    '''Clear the main windows frame of all widgets'''
    for child in rframe.winfo_children():
        child.destroy()

def win1(event=None):
    '''Create the main window'''
    clearwin()
    b1 = tk.Button(rframe, command=win2, text='Window 2')
    b1.pack()

def win2(event=None):
    '''Create the second sub window'''
    clearwin()
    
    app = snake(WIDTH, HEIGHT)
    back = tk.Button(rframe, command=win1, text='Back')
    back.pack()

    


"""Setup"""
root = tk.Tk()
rframe = tk.Frame(root)
rframe.pack()
root.title("snake")
root.tk.call("tk", "scaling", 4.0)
root.resizable(False, False)
# menu = main_menu(root)
win1()

root.mainloop()
# win1()
	# menu = main_menu(root, WIDTH, HEIGHT)
	# app = snake(root, WIDTH, HEIGHT)




if __name__ == '__main__':
	#main()
	pass