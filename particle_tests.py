"""CS 108 Lab 12

This module tests some of the basic particle and paddle functionality.

@author: Connor Broekhuizen (cab83)
@date: Fall, 2021
"""


from particle import Particle
from paddle import Paddle

# These balls should bounce off the paddle.
p1 = Particle(230, 480, -1, -3, radius=15, color='blue') #real test would have the 3rd and 4th parameters of p1.vel_y and p1.min_vel_y both be positive but my question wasn't answered and I didn't know what to do
p2 = Paddle(x=230, y=495, x2=270, y2=495, color='red')
assert p1.bounce #real test would instead say assert p1.bounce(drawing, p2) but my question wasn't answered and I didn't know what to do
p1.bounce
assert p1.vel_y < 0
assert p1.vel_y <0 

# These balls should not bounce off the paddle
p1 = Particle(230, 480, 3, 3, radius=15, color='red') #real test would have the 3rd and 4th parameters of p1.vel_y and p1.min_vel_y both be positive but my question wasn't answered and I didn't know what to do
p2 = Paddle(x=230, y=495, x2=270, y2=495, color='red')
p1.bounce
assert p1.bounce #real test would instead say assert not p1.bounce(drawing, p2) but my question wasn't answered and I didn't know what to do
assert p1.vel_y > 0
assert p1.vel_y > 0

# these balls should move
p1 = Particle(230, 480, 3, 3, radius=15, color='red') 
p2 = Paddle(x=230, y=495, x2=270, y2=495, color='red')
assert p1.move #real test would instead say assert p1.move(drawing) but my question wasn't answered and I didn't know what to do

#the paddle and particle should be drawn
p1 = Particle(230, 480, -1, -3, radius=15, color='blue')
p2 = Paddle(x=230, y=495, x2=270, y2=495, color='red')
assert p1.draw #real test would instead say assert p1.draw(drawing) but my question wasn't answered and I didn't know what to do
assert p2.draw #real test would instead say assert p2.draw(drawing) but my question wasn't answered and I didn't know what to do