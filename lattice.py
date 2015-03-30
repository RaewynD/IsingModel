import os, sys, math, random, io

'''
usage:
python isingmModel.py [TEMPURATURE] [DIM1] [DIM2]...
'''


class Lattice:

    def __init__(self, name, kt, dims):
        #initialize global variables
        self.dimensions = dims
        self.kt = kt
        self.lattice = self.recursive_allocator(0)
	self.name = name

    # This recursive code is accreditted to:
    # http://www.holehouse.org/programming/creating-n-dimensional-arrays-in-python/
    # recursive internal function that gives a multi-dimensional array
    # given an array of dimensions to create
    def recursive_allocator(self, depth):
        # Base case
        if depth == len(self.dimensions)-1:
            currentDimension = self.dimensions[depth]
            array = []
            for i in xrange(0,currentDimension):
#               TODO: return to random!!!
                array.append(random.choice([-1,1]))
#               array.append(1)
            return array

        # Recursive case
        else:
            array=[]
            currentDimension = self.dimensions[depth]

            # for each element in each dimension recursivly
            # call the function
            for i in xrange(0,currentDimension):
                array.append(self.recursive_allocator(depth+1))
            return array

    def getPositionStr(self, position):
        temp = "self.lattice"
        for i in position:
            temp = temp + "[" + str(i) + "]"
        return temp

    #flips the value at a given position
    def flipPositionValue(self, position):
        exec self.getPositionStr(position) + " = " + self.getPositionStr(position) + "*(-1)"
        return self.getValue(position)



    def updatePositionValue(self, position, newVal):
        exec self.getPositionStr(position) + " = newVal"


    #returns a list of positions that are neighbors of the
    #given postion
    def getNeighbors(self, position):
        neighbors = list()
        for i in range(len(position)):
            maxLen = self.dimensions[i]

            neighborPositionA = position[:]
#            print "nA: ", neighborPositionA
            neighborPositionA[i] = (position[i] + 1)%maxLen
#            print "nA: ", neighborPositionA

            neighborPositionB = position[:]
#            print "nB: ", neighborPositionB
            neighborPositionB[i] = (position[i] - 1)%maxLen
#            print "nB: ", neighborPositionB

            neighbors.append(neighborPositionA)
            neighbors.append(neighborPositionB)
#            print "neighbors ", neighbors

        return neighbors

    #gets value (-1 or +1) from lattice for a given position
    def getValue(self,position):
	val = 0
	exec "val = " + self.getPositionStr(position)
        return val

    #pass in a function and a closure and this method will
    #perform the function on every member of the lattice
    def mapLattice(self, func, closure):
        depth = 0
        position =  [0 for i in self.dimensions]
        self.recursiveMapHelper(func, closure, self.lattice, depth, position)

    def recursiveMapHelper(self, func, closure, sublattice, depth, position):
        if depth == len(self.dimensions)-1:
            for i in range(len(sublattice)):
                newPos = position
                newPos[depth] = i
                func(self, newPos, closure)
        else:
            for i in range(len(sublattice)):
                newPos = position
                newPos[depth] = i
                self.recursiveMapHelper(func, closure, sublattice[i], depth+1, newPos)


    # print object Lattice
    def printLattice(self):
	print "name: ", self.name
        print "kt: ", self.kt
        print "dims: ", self.dimensions
        print "lattice: ", self.lattice

