import lattice, os, sys, io, random, math
from lattice import Lattice


# calcluate hamiltonian for lattice
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

# calculate magnitization for lattice
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

    newSum = 0
    oldSum = 0
    positionValue = lattice.getValue(position)
    newPositionValue = -1*positionValue
    neighbors = lattice.getNeighbors(position)
    for i in neighbors:
        oldSum += positionValue*lattice.getValue(i)
	newSum += newPositionValue*lattice.getValue(i)
    return -1*(newSum - oldSum)



# TODO REMOVE THIS LATER
def getPos(thing, position):
        temp = "temp"
        for i in position:
            temp = temp + "[" + str(i) + "]"
        return temp

def posFlipTest(lattice, position, closure):
    if random.random() < math.exp(delta_hamiltonian(lattice, position)/lattice.kt):
        lattice.flipPositionValue(position)

def make2(lattice, pos, closure):
    lattice.updatePositionValue(pos, 2)

def runMetropolis(lattice):
    lattice.mapLattice(posFlipTest, None)

def main():
        if len(sys.argv) < 3:
                print "Exception: Too few arguments"
                exit(0)

        time = sys.argv[1]
        kt = float(sys.argv[2])
        dims = []
        for i in range(3, len(sys.argv)):
            dims.append(int(sys.argv[i]))

        print dims

        lattice = Lattice("lattice", kt, dims)
        lattice.printLattice()

	print "neighbors: ", lattice.getNeighbors([1,1,2])
	print "H: ", delta_hamiltonian(lattice,[1,1,2])
	print "Latt: ", runMetropolis(lattice)

        for i in range(1000):
                runMetropolis(lattice)
                print lattice.lattice
        exit(1)


if __name__ == "__main__":
        exit(main())
