import time

class Sun:
    def __init__(self, shining = True):
        self.shining = shining

class Tree:
    def photosynthesis(self):
        if sun.shining == True:
            print('The tree is producing oxygen...')
            return True
        else:
            print('No sun, so no air to breathe...')
            return False

class Grass:
    def __init__(self, bunch = 1):
        self.bunch = bunch
    
    def aBunch(self):
        return self.bunch

class Frog:
    def __init__(self, energy = 3):
        self.energy = energy

    def awake(self):
        if tree.photosynthesis() == False:
            print('The frog is sleeping...')
            time.sleep(1)
        else:
            print('The frog is jumping...')
            time.sleep(1)
            while True:
                self.energy -= 1
                if self.energy < 0:
                    print('The frog is hungry...')
                    time.sleep(1)
                    self.eating()
                    break
    
    def eating(self):
        print('The frog is eating...')
        time.sleep(1)
        while True:
            self.energy += grass.aBunch()
            if self.energy > 3:
                print('The frog is full now...')
                time.sleep(1)
                break
                    
    
class World:
    def startSim(self):
        day = 1
        while True:
            print('Day',  day,  ': ')
            q = input('Is today the day? (y/n) ')
            if q == 'y':
                print('This morning the frog commited suicide...\nThere is nothing to watch here anymore...\nBye')
                break
            if q == 'n':
                tree.photosynthesis()
                frog.awake()
                time.sleep(1)
                sun.shining = False
                print("It's nighttime...")
                time.sleep(1)
                tree.photosynthesis()
                frog.awake()
                time.sleep(1)
                sun.shining = True
                day += 1




sun = Sun()
tree = Tree()
grass = Grass()
frog = Frog()
world = World()

world.startSim()
