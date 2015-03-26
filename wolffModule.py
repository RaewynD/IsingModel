import lattice

def runWolff(kT, dimensions):

        lat = Lattice(kT, dimensions)

        #TODO: loop over all cells and call wolffDFS
        lat.mapLattice(lat.lattice, wolffCallback, None)


# a function with the correct structure to be passed to Lattice's
# mapLattice function.
# This function invokes the wolffDFS function
def wolffCallback(lattice, position, closure):
        wolffDFS(lattice, position)

def wolffDFS(lat, start):

        if !shouldFlip(start):
                return

        #visited is a set string corresponding to
        #indecies that have already been visited
        #flipList is a running list of vertices that need to be flipped
        visited, flipList = set(), [start]
        while flipList:
                pos = flipList.pop()
                if pos not in visited:
                        neighbors = lattice.getNeighbors(pos)
                        for neighbor in neighbors:
                                if shouldFlip(pos, neighbor):
                                        flipList.append(neighbor)

                        #add current pos to visited and then flip it in lattice
                        visited.add(pos)
                        lattice.flipPositionValue(pos)

#first checks to see whether previousPosition and newPostion are of same sign
#if so uses ∆E and the probability exp(-∆E/kT) from the lattice to calculate
#whether a position should be added to the list to flip
def shouldFlip(previousPosition, newPosition):

        preVal = lattice.getValue(previousPosition)
        newVal = lattice.getValue(newPosition)

        #check to see if different sign (I'm proud of this cleverness)
        #if so return false
        if preValue*newVal < 0:
                return False

        #TODO: The actual logic

