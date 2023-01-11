import time

class Sun:
    def __init__(self):
        self.shining = False
    
    def day(self):
        self.shining = not self.shining

class Tree:
    def __init__(self):
        pass

    def photosynthesis(self, oSun):
        if oSun.shining == True:
            return True
        else:
            return False

class Grass:
    def __init__(self):
        self.bunch = 1
    
    def aBunch(self):
        return self.bunch

class Frog:
    def __init__(self):
        self.energy = 3

    def awake(self, oSun, oTree, oGrass):
        if oTree.photosynthesis(oSun) == False:
            print('No Sun, so no air to breathe...')
            print('The frog is sleeping...')
            time.sleep(1)
        else:
            print('The Sun is shining...\nThe tree is producing oxygen...')
            print('The frog is awake and jumping...')
            time.sleep(1)
            while True:
                self.energy -= 1
                if self.energy < 0:
                    print('The frog is hungry...')
                    time.sleep(1)
                    self.eating(oGrass)
                    break
    
    def eating(self, oGrass):
        print('The frog is eating...')
        time.sleep(1)
        while True:
            self.energy += oGrass.aBunch()
            if self.energy > 3:
                print('The frog is full now...')
                time.sleep(1)
                break
                    
    
class World:
    def __init__(self):
        self.name = ''
    def setName(self, name):
        self.name = name
    def getName(self):
        print(self.name)

    def startSim(self, oSun, oTree, oGrass, oFrog):
        day = 1
        print(f'Welcome to {self.name}!')
        while True:
            print('Day',  day,  ': ')
            question = input('Is today the day? (y/n) ')
            question = question.lower()[0]
            if question == 'y':
                print('This morning the frog commited suicide...\nThere is nothing to watch here anymore...\nBye')
                break
            if question == 'n':
                oSun.day()
                oTree.photosynthesis(oSun)
                oFrog.awake(oSun, oTree, oGrass)
                time.sleep(1)
                oSun.day()
                print("It's nighttime...")
                time.sleep(1)
                oTree.photosynthesis(oSun)
                oFrog.awake(oSun, oTree, oGrass)
                time.sleep(1)
                day += 1




sun = Sun()
tree = Tree()
grass = Grass()
frog = Frog()
world = World()
world.setName('Serenum')
world.startSim(sun, tree, grass, frog)
