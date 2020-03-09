import random

class Ghost:
    def __init__(self):
        colors = ['white', 'yellow', 'red', 'purple']
        self.color = (random.choice(colors))