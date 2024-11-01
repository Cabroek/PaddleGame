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
class Paddle:
    """ Particle models a single particle that may be rendered to a canvas. """

    def __init__(self, x=50, y=50, x2=50, y2=50, color='red'):
        """Instantiate a paddle object."""
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.color = color

    
    def draw(self, drawing):
        """draw a rectangular representation of the paddle"""
        drawing.rectangle(self.x,
             self.y,
             self.x2,
             self.y2,
             color=self.color
             )
        

    
        
        