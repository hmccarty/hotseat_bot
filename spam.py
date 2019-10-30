import os
from bot import printToTopic

def run(values):
    print('WARNING: Depending on the amount you select, you could potentially destroy this hotseat discussion')
    count = (int) input('\nNumber of total posts: ')
    for i in range(count):
        for value in values:
           printToTopic(value) 
