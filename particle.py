"""CS 108 Lab 12

This module implements a model of a particle.

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Ken Arnold (ka37)
@date: Fall, 2019 - updated bounce algorithm
@author: Keith VanderLinden (kvlinden)
@date: Spring, 2021 - ported to GuiZero
@author: Connor Broekhuizen (Cab83)
@date: Fall, 2021
"""
class Particle:
    """ Particle models a single particle that may be rendered to a canvas. """

    def __init__(self, x=30, y=30, vel_y=1, min_vel_y=10, radius=30, color="red"):
        """Instantiate a particle object."""
        self.x = x
        self.y = y
        self.vel_y = vel_y
        self.min_vel_y = min_vel_y
        self.radius = radius
        self.color = color
        
        
    
    def draw(self, drawing):
        """draw a circular representation of the particle"""
        drawing.oval(self.x - self.radius,
             self.y - self.radius,
             self.x + self.radius,
             self.y + self.radius,
             color=self.color
             )
    
    def move(self, drawing):
        """make the particle appear to move around the screen"""
        self.y += self.min_vel_y


    def bounce(self, drawing, paddle):
        """Allows particles to bounce off the paddle"""
        self.p = paddle
        if self.y + self.radius >= self.p.y and self.x + self.radius >= self.p.x and self.x <= self.p.x2 and self.color == 'blue':
            self.min_vel_y *= -1
            return True
        return False