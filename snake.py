from tkinter import *
from random import *

class SnakeGUI():
	def __init__(self):
		self.window = Tk()
		self.window.title("Snake")
		self.window.geometry("640x740")
		
		self.page = Canvas(self.window, width=640, height=640, bg="black")
		self.page.pack()
		
		self.b1 = Button(self.window, text="Start", command=self.startGame)
		self.b1.place(x=300, y=680)

		self.page.create_rectangle(0, 0, 640, 19, fill="blue", outline="blue")
		self.page.create_rectangle(0, 621, 640, 640, fill="blue", outline="blue")
		self.page.create_rectangle(0, 20, 19, 620, fill="blue", outline="blue")
		self.page.create_rectangle(621, 20, 640, 620, fill="blue", outline="blue")

		self.up = False
		self.down = False
		self.left = False
		self.right = False
		self.pauseVar = ""
		
		self.gameOvertxt = Label(self.window, text="Game Over")
		self.scoreWidget = Label(self.window)
		
		self.window.mainloop()

	def startGame(self):
		self.b1.config(text="Pause", command=self.pauseGame)
		self.gameOvertxt.place_forget()
		self.scoreWidget.place_forget()

		self.delay = 500
		self.coordList = [(320, 320)]
		self.score = 1
		self.pause = False

		self.createPellet()
		self.createSnake()
		self.window.bind('<KeyPress>', self.keyPressed)
		self.right = True
		self.moveSnake()

	def pauseGame(self):
		self.pause = True
		
		if self.up:
			self.pauseVar = "up"
			self.up = False
			
		elif self.down:
			self.pausVar = "down"
			self.down = False
			
		elif self.left:
			self.pauseVar = "left"
			self.left = False
			
		elif self.right:
			self.pauseVar = "right"
			self.right = False
			
		self.b1.config(text="Resume", command=self.resumeGame)

	def resumeGame(self):
		self.b1.config(text="Pause", command=self.pauseGame)

		if self.pauseVar == "up":
			self.up = True
			
		elif self.pauseVar == "down":
			self.down = True
			
		elif self.pauseVar == "left":
			self.left = True
			
		elif self.pauseVar == "right":
			self.right = True

		self.pause = False

		self.window.bind('<KeyPress>', self.keyPressed)
		self.moveSnake()

	def createPellet(self):
		self.pelletx = randint(1, 30) * 20
		self.pellety = randint(1, 30) * 20
		while (self.pelletx, self.pellety) in self.coordList:
			self.pelletx = randint(1, 30) * 20
			self.pellety = randint(1, 30) * 20
		self.page.create_oval(self.pelletx, self.pellety, self.pelletx+20, self.pellety+20, fill="orange", tag="pellet")

	def createSnake(self):
		self.page.create_rectangle(320, 320, 340, 340, fill="green", tag="snake")
		self.point1x = 340
		self.point1y = 320
		self.point2x = 360
		self.point2y = 340

	def keyPressed(self, event):
		if self.score == 1:
			if event.keysym == "Up":
				self.up = True
				self.down = False
				self.left = False
				self.right = False
			
			elif event.keysym == "Down":
				self.up = False
				self.down = True
				self.left = False
				self.right = False
			
			elif event.keysym == "Left":
				self.up = False
				self.down = False
				self.left = True
				self.right = False
			
			elif event.keysym == "Right":
				self.up = False
				self.down = False
				self.left = False
				self.right = True

		else:
			if event.keysym == "Up" and self.down != True:
				self.up = True
				self.left = False
				self.right = False

			if event.keysym == "Down" and self.up != True:
				self.down = True
				self.left = False
				self.right = False

			if event.keysym == "Left" and self.right != True:
				self.up = False
				self.down = False
				self.left = True

			if event.keysym == "Right" and self.left != True:
				self.up = False
				self.down = False
				self.right = True
			
	def moveSnake(self):
		if not self.pause:
			
			self.window.after(self.delay,self.moveSnake)
			
			if self.up:
				self.point1y -= 20
				self.point2y -= 20

			elif self.down:
				self.point1y += 20
				self.point2y += 20

			elif self.left:
				self.point1x -= 20
				self.point2x -= 20

			elif self.right:
				self.point1x += 20
				self.point2x += 20

			if (self.point1x, self.point1y) in self.coordList or self.point1x == 0 or self.point1y == 0 or self.point1x == 620 or self.point1y == 620:
				self.gameOver()

			elif self.point1x == self.pelletx and self.point1y == self.pellety:
				self.page.delete("pellet")
				self.page.create_rectangle(self.point1x, self.point1y, self.point2x, self.point2y, fill="green", tag="snake")
				self.coordList.append((self.point1x, self.point1y))

				self.score += 1
				if self.delay != 50:
					self.delay -= 10
			
				self.createPellet()
			       
			elif self.up or self.down or self.left or self.right:
				tup = self.coordList[0]
				tail = self.page.find_closest(tup[0]+1, tup[1]+1)
				self.coordList.append((self.point1x, self.point1y))
				del self.coordList[0]
				self.page.delete(tail)
				self.page.create_rectangle(self.point1x, self.point1y, self.point2x, self.point2y, fill="green", tag="snake")

	def gameOver(self):
		self.up = False
		self.down = False
		self.left = False
		self.right = False
		self.pause = True

		self.scoreWidget.config(text="Score: "+str(self.score))
		self.gameOvertxt.place(x=300,y=320)
		self.scoreWidget.place(x=300, y=350)
		
		self.page.delete("snake", "pellet")
		self.b1.config(text="New Game", command=self.startGame)


SnakeGUI()
