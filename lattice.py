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


    def calculate_hamiltonian_lattice(self):
        depth = 0
        return self.recursive_hamiltonian(self.lattice,depth)

    def recursive_hamiltonian(self, sublattice,depth):
        if depth == len(self.dimensions)-1:
            sum = self.calculate_hamiltonian_array(sublattice)
            return sum
        else:
            sum = 0
            for i in range(len(sublattice)):
                sum = sum + self.recursive_hamiltonian(sublattice[i],depth+1)
            return sum


    # calculate the hamiltonian for any 1D array
    def calculate_hamiltonian_array(self,array):
        sum=0
        for i in range(len(array)):
            sum=sum+(array[i]*array[(i+1)%len(array)])
        return sum

    def delta_hamiltonian(self,position):
        originalSum = 0
        newSum = 0
        positionValue = 0
        exec "positionValue = " + getPositionStr(position)
        newPositionValue = positionValue*-1
        for i in range(len(position)):
            maxLength = self.dimensions[i]
            tempPosA = position
            tempPosA[i] = (tempPosA[i] + 1)%maxLength
            tempPosB = position
            tempPosB[i] = (tempPosB[i] - 1)%maxLength
            exec "oldSum += " + positionValue*self.getPositionStr(tempPosA)
            exec "oldSum += " + positionValue*self.getPositionStr(tempPosB)
            exec "newSum += " + positionValue*self.getPositionStr(tempPosA)
            exec "newSum += " + newPositionValue*self.getPositionStr(tempPosB)
        return -1*abs(newSum - oldSum)



    def getPositionStr(self, position):
        temp = "self.lattice"
        for i in position:
            temp = temp + "[" + str(i) + "]"
        return temp

    # print object Lattice
    def printLattice(self):
        print "kt: ", self.kt
        print "dims: ", self.dimensions
        print "lattice: ", self.lattice

# TODO REMOVE THIS LATER
def getPos(thing, position):
        temp = "temp"
        for i in position:
            temp = temp + "[" + str(i) + "]"
        return temp

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
        H = lattice.calculate_hamiltonian_lattice()
        print H

        temp = lattice.lattice
        exec "print " + getPos(temp,[1,1,1])
        exec (getPos(temp,[1,1,1]) + "= 5")
        exec "print " + getPos(temp,[1,1,1])

        exit(1)


if __name__ == "__main__":
        exit(main())
