"""
This module implements a simple timer/stopwatch.

Save the Timer class in a timer.py module, import that module, and use the
timer object as shown in the sample TimerApp. You can use this approach to
display a timer value and/or to handle periodic events.

@author: kvlinden
@date: Summer, 2016
@date: Spring, 2021 - ported to GuiZero
@author: ka37
@date: Spring 2021 - separated out the model
"""

from datetime import datetime

class Timer:
    def __init__(self):
        """instantiate a timer object"""
        self.reset()

    def reset(self):
        """resets the timer"""
        self.start_time = datetime.now()

    def get_time(self):
        """calculate how much time has passed"""
        time_since_start = datetime.now() - self.start_time
        return time_since_start.total_seconds()


