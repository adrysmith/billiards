#Adry was here
#And she retuned.
import matplotlib.pyplot as plt

GRAVITY = -9.80665 #m/s^2
GRANULARITY = 1.0 * 10 ** -3 #seconds / step
GRANULARITY2 = GRANULARITY ** 3
NUMSECONDS = 10 #time to run experiment in seconds
ELASTICITY = 0.9
STARTY = 1
STARTX = 0

class particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0
        self.ax = 0.0
        self.ay = GRAVITY
        #self.xpositions = []
        self.ypositions= []
        #self.xvelocities = []
        self.yvelocities = []
    def step(self):
        self.vx += self.ax * GRANULARITY
        self.vy += self.ay * GRANULARITY
        self.x  += self.vx * GRANULARITY + 0.5 * self.ax * GRANULARITY2
        self.y  += self.vy * GRANULARITY + 0.5 * self.ay * GRANULARITY2
        #self.xpositions.append(self.x)
        self.ypositions.append(self.y)
        #self.xvelocities.append(self.vx)
        self.yvelocities.append(self.vy)
        
    def collide(self, x, y):
        if  x > self.x:
            if x < self.x + self.vx * GRANULARITY:
                self.xv *= -1 * ELASTICITY
                self.x = x
        elif x < self.x:
            if x > self.x + self.vx * GRANULARITY:
                self.xv *= -1 * ELASTICITY
                self.x = x
        if  y > self.y:
            if y < self.y + self.vy * GRANULARITY:
                self.vy *= -1 * ELASTICITY
                self.y = y
        elif y < self.y:
            if y > self.y + self.vy * GRANULARITY:
                self.vy *= -1 * ELASTICITY
                self.y = y
        if ball.y < 0:
            self.vy = abs(self.vy)
            self.y = 0
    def __repr__(self):
        return "x = " + str((self.x,self.y)) + " v = " + str((self.vx,self.vy)) + " a = " + str((self.ax,self.ay))
    def getpos(self):
        return (self.x, self.y)
    def getvel(self):
        return (self.vx, self.vy)
    def getypositions(self):
        return self.ypositions
    def getyvelocities(self):
        return self.yvelocities
    def getxpositions(self):
        return self.xpositions
    def getxvelocities(self):
        return self.xvelocities

        
ball = particle(STARTX, STARTY)

for i in xrange(int(NUMSECONDS * 1/GRANULARITY)):
    ball.step()
    ball.collide(0,0)
    if i % 200 == 0:
        plt.figure(1)
        #plt.subplot(211)
        plt.plot(range(i + 1), ball.getypositions(), 'r')
        plt.xlim([0,int(NUMSECONDS * 1/GRANULARITY)])
        plt.show()
        plt.pause(0.01)
        
        #plt.subplot(212)
        plt.figure(2)
        plt.plot(ball.getyvelocities(), ball.getypositions(), 'b')
        plt.show()
        plt.pause(0.01)
        print ball

#plt.show()
