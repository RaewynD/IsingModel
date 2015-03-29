import os, sys, math, random, io, numpy, copy
from scipy.io import savemat

n=100 #Input dimensions
m=100
tmax=200 #input number of time steps
kT=4.0 #input temperature. 


#Calcualte the change in energy due to flipping one point on the grid. Flip the sign of DeltaE to get anti-ferromagnetic case. 
def delta_energy(array,i,j):
        deltaE = 2*array[i][j]*(array[i][(j+1) % (m)]+array[i][(j-1) % (m)]+array[(i+1)%n][j]+array[(i-1)%n][j]+array[(i-1)%n][(j-1)%m]+array[(i+1)%n][(j+1)%m])
        return deltaE


def main ():
    #Create a random grid of -1 and 1
    startingArray=numpy.random.choice([1,-1],[n,m])

     #Set that grid to be the array that will cycle through the loop
    currentArray=startingArray

    #print it to check, commented out for now.
    #print(currentArray)

    #Create an array that will be all of the data.
    fullData=[]

    #Add the starting time step to that array. I tired lots of things, and deepcopy, though slow, seemed to be the only oen that worked. 
    fullData.append(copy.deepcopy(currentArray))

    #Create the array that will be the list of magnetisms and put the first one in there. 
    magnetism=[numpy.sum(currentArray)]

    #Start the outer loop. 
    for t in range(0,tmax):

        #interate over rows. 
        for i in range(0,n):

            #interate over columns
            for j in range(0,m):

                #calculate change in energy
                deltaE=delta_energy(currentArray,i,j)

                #calculate probability of a flip
                prob=math.exp(-deltaE/kT)

                #generate a random number and flip the poin in the array if that number is less than the probability. This catches the cases where DeltaE<0 because probl will always be greater than 1 in those cases
                if random.random() < prob:
                    currentArray[i][j]=-1*currentArray[i][j]
        #add current magnetism to the list            
        currentMagnetism=numpy.sum(currentArray)
        magnetism.append(currentMagnetism)

        #add current array to full data
        
        fullData.append(copy.deepcopy(currentArray))
    #print(currentArray)

    #print the magnetism. It's faster to copy-paste to mathematica than generate a new file.
    print(magnetism)

    #store the full data in a matlab file. Mathematica likes these files fo rmulti-dimensional arrays. 
    savemat('temp.mat',{'fulldata':fullData})


main()
