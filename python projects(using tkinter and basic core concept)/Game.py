import tkinter as tk
import random

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Catch the Falling Object")
        
        self.canvas = tk.Canvas(master, width=400, height=400, bg='lightblue')
        self.canvas.pack()
        
        self.paddle = self.canvas.create_rectangle(150, 350, 250, 370, fill='blue')
        self.falling_object = self.canvas.create_oval(190, 0, 210, 20, fill='red')
        
        self.score = 0
        self.score_label = tk.Label(master, text=f"Score: {self.score}")
        self.score_label.pack()
        
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        
        self.fall_speed = 5
        self.game_over = False
        self.start_game()

    def start_game(self):
        self.move_falling_object()
        
    def move_falling_object(self):
        if not self.game_over:
            self.canvas.move(self.falling_object, 0, self.fall_speed)
            pos = self.canvas.coords(self.falling_object)
            
            if pos[3] >= 400:  # If the object hits the bottom
                self.game_over = True
                self.canvas.create_text(200, 200, text="Game Over", font=("Arial", 24), fill="black")
            elif self.check_collision(pos):
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.reset_falling_object()
            else:
                self.master.after(100, self.move_falling_object)

    def check_collision(self, pos):
        paddle_pos = self.canvas.coords(self.paddle)
        return (pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] and
                pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3])

    def reset_falling_object(self):
        self.canvas.coords(self.falling_object, random.randint(0, 380), 0, random.randint(20, 400), 20)

    def move_left(self, event):
        self.canvas.move(self.paddle, -20, 0)

    def move_right(self, event):
        self.canvas.move(self.paddle, 20, 0)

if __name__ == "_main_":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()