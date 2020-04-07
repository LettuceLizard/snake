#Main menu
import tkinter as tk
from snake_tkinter import snake

'''
Things to do:
figure out why the program creates 2 windows
'''

WIDTH = 300
HEIGHT = 300

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
    
    back = tk.Button(rframe, command=win1, text='Back')
    back.pack()
    app = snake(rframe, WIDTH, HEIGHT)

    


"""Setup"""
root = tk.Tk()
rframe = tk.Frame(root)
rframe.pack()
root.title("snake")
rframe.tk.call("tk", "scaling", 4.0)
root.resizable(False, False)

	
win1()
root.mainloop()
	# menu = main_menu(root, WIDTH, HEIGHT)
	# app = snake(root, WIDTH, HEIGHT)




if __name__ == '__main__':
	#main()
	pass