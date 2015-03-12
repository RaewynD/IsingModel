import os, sys, math, random, io

'''
usage:
python isingmModel.py [TEMPURATURE] [DIM1] [DIM2]...
'''

#initialize global variables
lattice = []
dimensions = list()
temperature = 0


def initialize_lattice():
        depth = 0
        global lattice 
        lattice = recursive_allocator(depth)

# This recursive code is accreditted to:
# http://www.holehouse.org/programming/creating-n-dimensional-arrays-in-python/
# recursive internal function that gives a multi-dimensional array
# given an array of dimensions to create
def recursive_allocator(depth):
        # Base case
        if depth == len(dimensions)-1:
                currentDimension = dimensions[depth]
                array = []
                for i in xrange(0,currentDimension):
#                       TODO: return to random!!!
#                        array.append(random.choice([-1,1]))
                        array.append(1)
                return array

        # Recursive case 
        else:
                array=[]
                currentDimension = dimensions[depth]

                # for each element in each dimension recursivly
                # call the function    
                for i in xrange(0,currentDimension):
                        array.append(recursive_allocator(depth+1))
                return array


def calculate_hamiltonian_lattice():
        depth = 0
#        print "WHAT"
#        print lattice
        return recursive_hamiltonian(lattice,depth)

def recursive_hamiltonian(sublattice,depth):
#        print "HEY"
        if depth == len(dimensions)-1:
                sum = calculate_hamiltonian_array(sublattice)
#                print "BASE CASE"
#                print sublattice
#                print sum
                return sum
        else:
#                print "NO"
                sum = 0
#                print sublattice
#                print len(sublattice)
                for i in range(len(sublattice)):
                        sum = sum + recursive_hamiltonian(sublattice[i],depth+1)
#                        print "RECURSIVE CALL"
#                        print sublattice
#                        print sum
                return sum


# calculate the hamiltonian for any 1D array
def calculate_hamiltonian_array(array):
        sum=0
        for i in range(len(array)-1):
                sum=sum+(array[i]*array[i+1])
        return sum


def main():
        if len(sys.argv) < 3:
                print "Exception: Too few arguments"
                exit(0)

        temperature = sys.argv[1]
        for i in range(2, len(sys.argv)):
                dimensions.append(int(sys.argv[i]))

        print dimensions

        initialize_lattice()
        print lattice

        # print calculate_hamiltonian_array([1,1,1,1,1])
        H = calculate_hamiltonian_lattice()
        print H

        exit(1)


if __name__ == "__main__":
        exit(main())
