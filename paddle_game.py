"""CS 108 Lab 12

This module implements a GUI controller for a particle simulation.
Since the project 3 walkthrough, I got the leveling and scoring to be both displayed and calculated properly as well as function properly. I also got the paddle to move using the arrow keys.
I added ways for the player to lose the game and got the canvas to pause if they did lose. I added multiple features to the new game button so the game fully reset all of the needed features when
restarting the game. I also added a file-based leaderboard to display the top 3 scores after each game has been played. 

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Fall, 2018 - updated to use callback animation
@date: Spring, 2021 - ported to GuiZero
@author: ka37
@date: Spring 2021 - separated out the timer model
@author: Justin Mayer
@date: Spring, 2019
@author: Connor Broekhuizen (Cab83)
@date: Fall, 2021
"""

from guizero import App, Drawing, Box, PushButton, Text
from helpers import get_random_color
from paddle import Paddle
from particle import Particle
from random import randint
from datetime import datetime
from timer import Timer


class paddle_game:
    """ParticleSimulation runs a simulation of multiple particles interacting
    on a single canvas.
    """

    def __init__(self, app):
        """Instantiate the simulation GUI app."""
        app.title = 'Particle Simulation'
        UNIT = 500
        CONTROL_UNIT = 50
        app.width = UNIT
        app.height = UNIT + CONTROL_UNIT

        # Add the widgets.
        box = Box(app, layout='grid', width=UNIT, height=UNIT + CONTROL_UNIT)
        
        
        self.drawing = Drawing(box, width=UNIT, height=UNIT, grid=[0, 0, 10, 1])
        self.drawing.bg = "black"
        newgame_button = PushButton(box, self.new_game, text='New Game', grid=[1,1])
        timer_text = Text(box, text='Timer:', grid=[2, 1])
        self.timer = Timer()
        self.text = Text(app)
        self.timer_count = Text(box, text='', grid=[3, 1])
        self.gameover_text = Text(box, text='Game Over', grid=[3, 0])
        self.gameover_text.hide()
        self.level_text = Text(box, text='Level:', grid=[5, 1])
        self.level_count = Text(box, text='1', grid=[6, 1])
        self.score_text = Text(box, text='Score:', grid=[7, 1])
        self.score_count = Text(box, text='0', grid=[8, 1])
        self.score = 0
        self.vel_y = 3
        self.min_vel_y = 3
        self.score_count.value = str(self.score)
        self.p1 = Particle()
        self.p_list = []
        self.p1.draw(self.drawing)
        self.p = Paddle(x=(app.width/2) - 20, y=app.height - 55, x2=(app.width/2) + 20, y2=app.height - 50, color='red')
        app.when_key_pressed = self.process_key_event
        app.repeat(10000, self.next_level)
        app.repeat(30, self.draw_frame)
        app.repeat(1000, self.add_particle)
        app.repeat(10, self.update_clock)
        self.paused = False

        
        
    def draw_frame(self):
        """Implements drawing, moving, and bouncing of particles"""
        if self.paused == False:
            self.drawing.clear()
            for p1 in self.p_list:
                p1.move(self.drawing)
                p1.draw(self.drawing)
                p1.bounce(self.drawing, self.p)
                if p1.bounce(self.drawing, self.p) == True and self.level_count.value == '1':  #50 points per hit for level 1
                    self.score += 50
                    p1.min_vel_y *= -1
                if p1.bounce(self.drawing, self.p) == True and self.level_count.value == '2':  #100 points per hit for level 1
                    self.score += 100
                    p1.min_vel_y *= -1
                if p1.bounce(self.drawing, self.p) == True and self.level_count.value == '3':  #150 points per hit for level 1
                    self.score += 150
                    p1.min_vel_y *= -1
            self.score_count.value = str(self.score) #displays the score next to the score text
            self.p.draw(self.drawing)
            self.timer_count.value = self.timer.get_time() #displays the time next to the timer text
            self.game_over()
            self.leaderboard()
        
        
    
        
    def process_key_event(self, event):
        """Move the paddle based on the arrow keys.
        """
        #Get the key symbol. event.key doesn't work for all keys.
        key = event.tk_event.keysym
        #print('keysym: ' + key)
        if key == 'Right':
            self.p.x += 50
        if key == 'Right':
            self.p.x2 += 50
        if key == 'Left':
            self.p.x -= 50
        if key == 'Left':
            self.p.x2 -= 50
            
    def add_particle(self):
        """drops multiple particles from the top of the canvas"""
        radius = 15
        x = randint(25, self.drawing.width - 25)
        y = 15
        vel_y = self.vel_y
        min_vel_y = self.min_vel_y
        color = get_random_color()
        p = Particle(x, y, vel_y, min_vel_y, radius, color)
        self.p_list.append(p)
    
    def new_game(self):
        """Clears the canvas and begins a new game"""
        self.drawing.clear()
        self.p_list.clear()
        self.timer.reset()
        self.gameover_text.hide()
        self.level_reset()
        self.score_reset()
        self.vel_reset()
        app.repeat(5000, self.next_level)
        self.paused = False
        
    def update_clock(self):
        """Here, we update the value of the timer display on the GUI."""
        self.text.value = '{:.2f}'.format(self.timer.get_time())
        
    def pause(self):
        """ Stop the paddle_game animation temporarily. """
        self.paused = True
            
    def game_over(self):
        """ends the game and displays game over text when a blue particle falls or red particle hits the paddle"""
        for p1 in self.p_list:
            if p1.y + p1.radius > app.height and p1.color == 'blue': #if blue particle falls below canvas, the game ends
                self.pause()
                self.gameover_text.show()
                app.cancel(self.next_level)
            if p1.y + p1.radius == self.p.y and p1.x + p1.radius >= self.p.x and p1.x <= self.p.x2 and p1.color == 'red': #if red particle hits paddle, the game ends
                self.pause()
                self.gameover_text.show()
                app.cancel(self.next_level) #cancels the next level method in order to make sure the next level initiates when it's supposed to
            
    def next_level(self):
        """creates new levels in which the particles fall faster"""
        if self.paused == False:
            for p1 in self.p_list:
                self.vel_y += 0.5
                self.min_vel_y = self.vel_y #keeps the minimum velocity updating so each particle is created at the correct speed for each level
            self.level_count.value = str(int(self.level_count.value) + 1)
            
    def vel_reset(self):
        """resets the velocity of the particles when starting a new game"""
        self.vel_y = 3
        self.min_vel_y = 3
            
    def level_reset(self):
        """resets the level when starting a new game"""
        self.level_count.value = 1
    
    def score_reset(self):
        """resets the score when starting a new game"""
        self.score = 0
        
    def leaderboard(self):
        """creates a leaderboard of the top 3 scores"""
        if self.paused == True:
            print('Leaderboard:')
            file = open('leaderboard.txt', 'a')  # Open file
            file.write(str(self.score))  # Write score as string
            file.write('\n')
            file.close()  # Close the file
            file = open('leaderboard.txt', 'r')  # Open file
            lines = list(file) #creates list of strings
            file.close()# Close the file
            updated_lines = []
            for line in lines:
                if line.strip():
                    self.score = line.split(' ')[0] #split the text on each space and take the first item
                    self.score = int(self.score)
                    updated_lines.append([self.score, line])
            sorted_updated_lines = sorted(updated_lines, reverse = True) #sorts the list based on highest number
            for line in sorted_updated_lines[0:3]:
                print(line[1].strip()) #print the string version of each high score




app = App()
paddle_game(app)
app.display()