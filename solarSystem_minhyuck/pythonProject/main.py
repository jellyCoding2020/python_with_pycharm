class Sun:
    def __init__(self, iName, iRad, iM, iTemp):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__temp = iTemp
        self.__y = 0
        self.__x = 0

        self.__sTurtle = turtle.Turtle()
        self.__sTurtle.shape("circle")
        self.__sTurtle.color("yellow")

    def getMass(self):
        return self.__mass

    def getXpos(self):
        return self.__x

    def getYpos(self):
        return self.__y


class SolarSystem:

    def __init__(self, width, height):
        print('hello')
        self.__thesun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.setworldcoordinates(-width / 2.0, -height / 2.0, width / 2.0, height / 2.0)

    def addPlanet(self, aplanet):
        self.__planets.append(aplanet)

    def addsun(self, asun):
        self.__thesun = asun

    def showPlanet(self):
        for aplanet in self.__planets:
            print(aplanet)

    def freeze(self):
        self.__ssScreen.exitonclick()


class Planet:

    def __init__(self, iName, iRad, iM, iDist, iC):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDist
        self.__y = 0
        self.__x = self.__distance
        self.___color = iC
        self.__pTurtle = turtle.Turtle()
        self.__pTurtle.color(self.___color)
        self.__pTurtle.shape("circle")

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x, self.__y)
        self.__pTurtle.down()
        #self.__velx = iVx
        #self.__vely = iVy

        self.__pTurtle.speed(0)

    def getXpos(self):
        return self.__x

    def getYpos(self):
        return self.__y

    def getRadius(self):
        return self.__radius

    def setRadius(self, r):
        self.__radius = r

    def getMass(self):
        return self.__mass

    def getDistance(self):
        return self.__distance
    def moveTo(self, newX,newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)

    def getXvel(self):
        return self.__velX

    def getYvel(self):
        return self.__velY

    def setXVel(self, newVx):
        self.__velx = newVx

    def setYVel (self, newVy):
        self.__vely = newVy

    def movePlanets(self):
        G = .1
        dt = .001
    def getVolume(self):
        import math
        v = 4 / 3 * math.pi * self.__radius ** 3
        return v

    def getSurfaceArea(self):
        import math
        sa = 4 * math.pi * self.__radius ** 2
        return sa

    def getDestiny(self):
        d = self.__mass / self.getVolume()
        return d


import turtle

ss = SolarSystem(2, 2)

sun = Sun("Sun", 5000, 10, 5800)
ss.addsun(sun)

m = Planet("Mecurury", 19.5, 1000, .25, "blue")
ss.addPlanet(m)

m = Planet("Earth", 47.5, 5000, 0.3, "green")
ss.addPlanet(m)

m = Planet("Mars", 50, 9000, 0.5, "red")
ss.addPlanet(m)

m = Planet("Jupiter", 100, 49000, 0.7, "black")
ss.addPlanet(m)

ss.freeze()
