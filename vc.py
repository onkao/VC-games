from tkinter import *
import random

boardWidth =30
boardHeight = 30
tilesize = 20

class Snake():

    def __init__(self):

        self.snakeX = [20, 20, 20]
        self.snakeY = [20, 21, 22]
        self.snakeLength = 1
        self.key ='u'
        self.points = 0

    def move(self): # move and change direction with wasd

        for i in range(self.snakeLength - 1, 0, -1):
                self.snakeX[i] = self.snakeX[i-1]
                self.snakeY[i] = self.snakeY[i-1]

        if self.key == "u":
            self.snakeY[0] = self.snakeY[0] - 1

        elif self.key == "d":
            self.snakeY[0] = self.snakeY[0] + 1

        elif self.key == "l":
            self.snakeX[0] = self.snakeX[0] - 1

        elif self.key == "r":
            self.snakeX[0] = self.snakeX[0] + 1
        
        self.eatApple()


    def eatApple(self):

        if self.snakeX[0] == apple.getAppleX() and self.snakeY[0] == apple.getAppleY():

            self.snakeLength = self.snakeLength + 1


            x = self.snakeX[len(self.snakeX)-1] # Snake grows
            y = self.snakeY[len(self.snakeY) - 1]
            self.snakeX.append(x+1)
            self.snakeY.append(y)

            self.points = self.points + 1


            apple.createNewApple()



    def checkGameOver(self):

        if self.snakeX[0] < 1 or self.snakeX[0] >= boardWidth-1 or self.snakeY[0] < 1 or self.snakeY[0] >= boardHeight-1:
            return True # Snake out of Bounds

        return False

    def getKey(self, event):

        if event.char == "u" or event.char == "r" or event.char == "d" or event.char == "l" or event.char == " ":
            self.key = event.char

    def getSnakeX(self, index):
        return self.snakeX[index]

    def getSnakeY(self, index):
        return self.snakeY[index]

    def getSnakeLength(self):
        return self.snakeLength
    
    def getPoints(self):
        return self.points

class Apple:

    def __init__(self):
        self.appleX = random.randrange(1, boardWidth - 2)
        self.appleY = random.randrange(1, boardHeight - 2)

    def getAppleX(self):
        return self.appleX

    def getAppleY(self):
        return self.appleY

    def createNewApple(self):
        self.appleX = random.randrange(1, boardWidth - 2)

class GameLoop:
    def repaint(self):

        canvas.after(300, self.repaint)
        canvas.delete(ALL)

        if snake.checkGameOver() == False:
            snake.move()
            snake.checkGameOver()

            canvas.create_rectangle(snake.getSnakeX(0) * tilesize, snake.getSnakeY(0) * tilesize,
                                    snake.getSnakeX(0) * tilesize + tilesize,
                                    snake.getSnakeY(0) * tilesize + tilesize, fill="yellow")  # Head
            
            for i in range(1, snake.getSnakeLength(), 1):

                canvas.create_rectangle(snake.getSnakeX(i) * tilesize, snake.getSnakeY(i) * tilesize,
                                        snake.getSnakeX(i) * tilesize + tilesize,
                                        snake.getSnakeY(i) * tilesize + tilesize, fill="red")  # Body
            canvas.create_oval(apple.getAppleX() * tilesize, apple.getAppleY() * tilesize,
                                    apple.getAppleX() * tilesize + tilesize,
                                    apple.getAppleY() * tilesize + tilesize, fill="black")  # Apple

        else:   # GameOver Message
            canvas.delete(ALL)
            canvas.create_text(150, 100, fill="lightblue", font="Times 20 italic bold", text="Game Over!")
            canvas.create_text(150, 150, fill="lightblue", font="Times 20 italic bold",
                                   text="Points:" + str(snake.getPoints()))
         

snake = Snake()
apple = Apple()
root = Tk()

canvas = Canvas(root, width=600, height=600)
canvas.configure(background="green")
canvas.pack()

gameLoop = GameLoop()
gameLoop.repaint()

root.title("Snake")
root.bind('<KeyPress>', snake.getKey)
root.mainloop()

