"""CS 108 Lab 12

This module implements helper functions for lab 12.

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author Ken Arnold (ka37): updated to use hex format strings
@date: Fall 2020
"""

import random


def get_random_color():
    """Generate random color of either red or blue
    """
    return random.choice(['red','blue'])
