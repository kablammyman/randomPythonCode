#it must be like this....not sure why
from Tkinter import *

class App:
	#can define vars here
	someClicks = 0
	def __init__(self, master):
		frame = Frame(master)
		#put the fram onto the grid
		frame.grid()
		w1 = Label(master, text="Rouge", fg="red")
		w2 = Label(master, text="Helvetica", font=("Helvetica", 16))
		w1.grid()
		w2.grid()
		
		self.label = Label(frame,text = "this is a label widget")
		#puts the lable on the window
		self.label.grid()
		
		self.button1 = Button(frame,text = "this is a button",command = self.updateClick)
		self.button1.grid()
		self.numClicks = 0 #or can define vars like this
		self.button2 = Button(frame)
		self.button2.grid()
		self.button2.configure(text = "added text")

		self.button3 = Button(frame)
		self.button3.grid()
		self.button3["text"] = "more text"
		
		self.e1 = Entry(master)
		self.e2 = Entry(master)
		self.e1.grid(row=0, column=1)
		self.e2.grid(row=1, column=1)
		
		

	def updateClick(self):
		self.numClicks += 1
		self.someClicks += 1
		print "click"
		self.button1["text"] = "clicks: "+ str(self.e1.get())+ str(self.numClicks)
	
root = Tk()
app = App(root)
root.title("simple gui")
root.geometry("500x200")

root.mainloop()