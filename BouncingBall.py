import matplotlib.pyplot as plt

GRAVITY = -9.80665 #m/s^2
GRANULARITY = 1.0 * 10 ** -4 #seconds / step
GRANULARITY2 = GRANULARITY ** 2
NUMSECONDS = 4 #time to run experiment in seconds
ELASTICITY = 0.95
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
    def step(self):
        self.vx += self.ax * GRANULARITY
        self.vy += self.ay * GRANULARITY
        self.x  += self.vx * GRANULARITY + 0.5 * self.ax * GRANULARITY2
        self.y  += self.vy * GRANULARITY + 0.5 * self.ay * GRANULARITY2

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
    def __repr__(self):
        return "x = " + str((self.x,self.y)) + " v = " + str((self.vx,self.vy)) + " a = " + str((self.ax,self.ay))
    def getpos(self):
        return (self.x, self.y)
    def getvel(self):
        return (self.vx, self.vy)
        
ball = particle(STARTX, STARTY)
ypos = []
yvel = []

for i in xrange(int(NUMSECONDS * 1/GRANULARITY)):
    ball.step()
    ball.collide(0,0)
    ypos.append(ball.getpos()[1])
    yvel.append(ball.getvel()[1])
    if i % 100 == 0:
        plt.plot(range(i + 1), ypos, 'b')
        plt.xlim([0,int(NUMSECONDS * 1/GRANULARITY)])
        plt.show()
        plt.pause(0.01)


#plt.show()