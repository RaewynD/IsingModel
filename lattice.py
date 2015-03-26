import os, sys, math, random, io

'''
usage:
python isingmModel.py [TEMPURATURE] [DIM1] [DIM2]...
'''


class Lattice:

    def __init__(self, kt, dims):
        #initialize global variables
        self.dimensions = dims
        self.kt = kt
        self.lattice = self.recursive_allocator(0)

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


    #returns a list of positions that are neighbors of the 
    #given postion
    def getNeighbors(self, position):
        neighbors = list()
        for coord  in position:
            
            neighborPositionA = position
            neighborPositionA[coord] = position[coord] + 1

            neighborPositionB = position
            neighborPositionB[coord] = position[coord] - 1
            
            neighbors.append(neighborPositionA)
            neighbors.append(neighborsPositionB)

        return neighbors

    #gets value (-1 or +1) from lattice for a given position
    def getValue(position):
        exec "return " + self.getPositionStr(position)

    #pass in a function and a closure and this method will
    #perform the function on every member of the lattice
    def mapLattice(self, lattice, func, closure):
        depth = 0
        position =  [0 for i in self.dimensions]
        self.recursiveMapHelper(func, closure, self.lattice, self.lattice, depth, position)

    def recursiveMapHelper(func, closure, lattice, sublattice, depth, position):
        if depth == len(self.dimensions)-1:
            for i in range(len(sublattice)):
                newPos = position
                newPos[depth] = i
                func(lattice, newPos, closure)
        else:
            for i in range(len(sublattice)):
                newPos = position
                newPos[depth] = i
                recursiveMapHelper(func, closure, lattice, sublattice[i], depth+1, newPos)


    # print object Lattice
    def printLattice(self):
        print "kt: ", self.kt
        print "dims: ", self.dimensions
        print "lattice: ", self.lattice

def calculate_hamiltonian_lattice(lattice):
    depth = 0
    return recursive_hamiltonian(lattice,lattice.lattice,depth)

def recursive_hamiltonian(lattice, sublattice, depth):
    if depth == len(lattice.dimensions)-1:
        sum = calculate_hamiltonian_array(sublattice)
        return sum
    else:
        sum = 0
        for i in range(len(sublattice)):
            sum = sum + recursive_hamiltonian(lattice,sublattice[i],depth+1)
        return sum

# calculate the hamiltonian for any 1D array
def calculate_hamiltonian_array(array):
    sum=0
    for i in range(len(array)):
        sum=sum+(array[i]*array[(i+1)%len(array)])
    return sum

def calculate_lattice_magnitization(lattice):
    depth = 0
    return recursive_magnitization(lattice,lattice.lattice,depth)

def recursive_magnitization(lattice, sublattice, depth):
    if depth == len(lattice.dimensions)-1:
        sum = calculate_array_magnitization(sublattice)
        return sum
    else:
        sum = 0
        for i in range(len(sublattice)):
            sum = sum + recursive_magnitization(lattice,sublattice[i],depth+1)
        return sum

# calculate the hamiltonian for any 1D array
def calculate_array_magnitization(array):
    sum=0
    for i in range(len(array)):
        sum=sum+array[i]
    return sum

def delta_hamiltonian(lattice,position):
    originalSum = 0
    newSum = 0
    positionValue = 0
    exec "positionValue = " + lattice.getPositionStr(position)
    newPositionValue = positionValue*(-1)
    for i in range(len(position)):
        maxLength = lattice.dimensions[i]
        tempPosA = position
        tempPosA[i] = (tempPosA[i] + 1)%maxLength
        tempPosB = position
        tempPosB[i] = (tempPosB[i] - 1)%maxLength
        exec "oldSum += " + positionValue*(lattice.getPositionStr(tempPosA))
        exec "oldSum += " + positionValue*(lattice.getPositionStr(tempPosB))
        exec "newSum += " + newPositionValue*(lattice.getPositionStr(tempPosA))  
        exec "newSum += " + newPositionValue*(lattice.getPositionStr(tempPosB))
    return -1*(newSum - oldSum)



# TODO REMOVE THIS LATER
def getPos(thing, position):
        temp = "temp"
        for i in position:
            temp = temp + "[" + str(i) + "]"
        return temp

def posFlipTest(lattice, position):
    if random.random() < math.exp(-lattice.delta_hamiltonian(position)/lattice.kt):
        lattice.updatePosition(position)

def main():
        if len(sys.argv) < 3:
                print "Exception: Too few arguments"
                exit(0)

        kt = sys.argv[1]
        dims = []
        for i in range(2, len(sys.argv)):
                dims.append(int(sys.argv[i]))

        print dims

        lattice = Lattice(kt, dims)
        lattice.printLattice()

        # print calculate_hamiltonian_array([1,1,1,1,1])
        H = calculate_hamiltonian_lattice(lattice)
        print "H: ",H

        temp = lattice.lattice
        exec "print " + getPos(temp,[1,1,1])
        exec (getPos(temp,[1,1,1]) + "= 5")
        exec "print " + getPos(temp,[1,1,1])

        exit(1)


if __name__ == "__main__":
        exit(main())
