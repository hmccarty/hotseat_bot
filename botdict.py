import os
from random import choice

class BotDictionary():
    def __init__(self):
        self.thoughts = []
        self.replies = []
        with open('thoughts.txt') as fp:
            line = fp.readline()
            while line:
                self.thoughts.append(line.rstrip())
                line = fp.readline()
        with open('replies.txt') as fp:
            line = fp.readline()
            while line:
                self.replies.append(line.rstrip())
                line = fp.readline()        

    def getRandomThought(self):
        return choice(self.thoughts)

    def getRandomReplies(self):
        return choice(self.replies)    
