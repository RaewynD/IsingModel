import os, sys, math, random, io, numpy, copy
from scipy.io import savemat

n=100 #Input dimensions
m=100
tmax=200 #input number of time steps
kT=4.0 #input temperature. 


#Calcualte the change in energy due to flipping one point on the grid. Flip the sign of DeltaE to get anti-ferromagnetic case. 
def delta_energy(array,i,j):
        deltaE = 2*array[i][j]*(array[i][(j+1) % (m)]+array[i][(j-1) % (m)]+array[(i+1)%n][j]+array[(i-1)%n][j])
        return deltaE

def main ():
    #Create a random grid of -1 and 1
    startingArray=numpy.random.choice([1,-1],[n,m])

    #Set that grid to be the array that will cycle through the loop
    currentArray=startingArray

    #Print that array to check it looks good. Commented out for now. 
    #print(currentArray)

    #This would be the file to export to get a movie. Deepcopy is SLOOWW, so I don't do this when I don't have to. that's why the relevant sections are commendted out. 
    #fullData=[]
    #fullData.append(copy.deepcopy(currentArray))

    #store an array that will be the magnetisms at each time.
    magnetism=[numpy.sum(currentArray)]

    #begin time loop
    for t in range(0,tmax):

        #begin row loop
        for i in range(0,n):

            #begin column loop
            for j in range(0,m):

                #calculate change in energy
                deltaE=delta_energy(currentArray,i,j)

                #calculate probability of flip
                prob=math.exp(-deltaE/kT)

                #execute test and flip. 
                if random.random() < prob:
                    currentArray[i][j]=-1*currentArray[i][j]
                    
        #print(currentArray)

        #Add current magnetism to that list. 
        currentMagnetism=numpy.sum(currentArray)
        magnetism.append(currentMagnetism)
        #fullData.append(copy.deepcopy(currentArray))
    #print(currentArray)

    #get magnetism
    print(magnetism)
    
    #savemat('temp.mat',{'fulldata':fullData})

main()
