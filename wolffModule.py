import lattice, os, sys, io, random, math, copy
from scipy.io import savemat
from lattice import Lattice

def runWolff(lat):
        lat.mapLattice(wolffCallback, None)


# a function with the correct structure to be passed to Lattice's
# mapLattice function.
# This function invokes the wolffDFS function
def wolffCallback(lat, position, closure):
        wolffDFS(lat, position)

def wolffDFS(lat, start):

        if not shouldFlip(lat, start, start, 1):
                return

        #visited is a set string corresponding to
        #indecies that have already been visited
        #flipList is a running list of vertices that need to be flipped
        visited, flipList = set(), [tuple(start)]
        delta_H = 0
        while flipList:
                #note: conversion to tuple from list is made for hashing
                pos = tuple(flipList.pop())
                if pos not in visited:
                        neighbors = lat.getNeighbors(list(pos))
                        for neighbor in neighbors:
                                if shouldFlip(lat, pos, neighbor, delta_H):
                                        flipList.append(neighbor)

                        #add current pos to visited and then flip it in lattice
                        visited.add(tuple(pos))
                        delta_H += lat.flipPositionValue(pos)

#first checks to see whether previousPosition and newPostion are of same sign
#if so uses deltaE and the probability exp(-deltaE/kT) from the lattice to
#calculate
#whether a position should be added to the list to flip
def shouldFlip(lat, previousPosition, newPosition, delta_H):
        preVal = lat.getValue(previousPosition)
        newVal = lat.getValue(newPosition)
        #check to see if different sign (I'm proud of this cleverness)
        #if so return false
        if preVal*newVal < 0:
                return False


        return random.random() < (1 - math.exp((-1)*delta_H/lat.kt))

def main():
        if len(sys.argv) < 3:
                print "Exception: Too few arguments"
                exit(0)

        time = sys.argv[1]
        kt = float(sys.argv[2])
        dims = []
        for i in range(3, len(sys.argv)):
            dims.append(int(sys.argv[i]))

 #       print dims

        lat = Lattice("lattice", kt, dims)
        lat.printLattice()
        initiallattice=copy.deepcopy(lat.lattice)
        #Make a copy that can be outputted

        for i in range(10000):
                runWolff(lat)
                print lat.lattice
        finallattice=copy.deepcopy(lat.lattice)
        #make a copy that can be outputted

        #output initial and final grids. 
        savemat('initial.mat',{'Initial':initiallattice})
        savemat('final.mat',{'final':finallattice})

if __name__ == "__main__":
        exit(main())
