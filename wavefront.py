#Dmitrii Karpenko
#For Introduction to Robotics
#2019


import numpy as np
import math  

#*****************Files path*************************

WorldInput = "world5.txt"

PathOutput = "wavefront_world5.txt"

#**************************


#Clear the output file
file = open(PathOutput, "w") 
file.write('') 
file.close() 
########

def findDistanceCphere(z,y,x, k, j, i):
    dist = math.sqrt((i - x)**2 + (j - y)**2 + (k - z)**2)
    return dist 

def addObstacleSphere(x,y,z,radius):
    i = 0
    j = 0
    k = 0

    for i in range(RangeX[1]):
        for j in range(RangeY[1]):
            for k in range(RangeZ[1]):
                distance = findDistanceCphere(z,y,x, k, j, i)
                if distance<radius+1:
                    array2d[k][j][i] = 1                    
    return

def addObstacleCube(x,y,z,side):
    #side = side*1.3
    i = 0
    j = 0
    k = 0
    startx = x-side/2
    endx = x+side/2
    starty = y-side/2
    endy = y+side/2
    startz = z-side/2
    endz = z+side/2

    for i in range(RangeX[1]):
        for j in range(RangeY[1]):
            for k in range(RangeZ[1]):
                if j <= endy and j >= starty and i >= startx and i <= endx and k <= endz and k >= startz:
                    array2d[k][j][i] = 1
    return


def validation(z, y, x):
    if x<RangeX[0] or z<RangeZ[0] or y<RangeY[0] or z >= RangeZ[1] or y >= RangeY[1] or x >= RangeX[1]:
        return False
    else:
        if array2d[z][y][x] == 0:
            return True
        else:
            return False

def validation2(z, y, x):
    if RangeX[0]<0 or RangeZ[0]<0 or RangeY[0]<0 or z >= RangeZ[1] or y >= RangeY[1] or x >= RangeX[1]:
        return False
    else:
        if array2d[z][y][x] == 1:
            return False
        else:
            return True

def setRoundPoints(z, y, x):
    value = array2d[z][y][x]
    for i in range(-1, 2):
        for j in range(-1,2):
            for k in range(-1,2):
                if (validation(z+k, y + j, i+x)):
                    array2d[z+k][y+j][x+i] = value+ 1
    return

def doRound(num):
    while True:
        for i in range(RangeX[1]):
            for j in range(RangeY[1]):
                for k in range(RangeZ[1]):
                    if array2d[k][j][i] == num:
                        setRoundPoints(k, j, i)
        num += 1
        if num>((len(range(RangeX[0], RangeX[1]))*(len(range(RangeY[0], RangeY[1]))))):
            print('No path exist')
            quit()
        if array2d[startPoint[2]][startPoint[1]][startPoint[0]]>0:
            break
        
    return

def findDistance(z, y, x):
    dist = math.sqrt((goalPoint[0] - x)**2 + (goalPoint[1] - y)**2 + (goalPoint[2] - z)**2)
    return dist


def bouildPath():
    print ('Starting poing: (' + str(startPoint[0]) + ':' + str(startPoint[1]) + ':' + str(startPoint[2]) + ')' )
    print ('Ending poing: (' + str(goalPoint[0]) + ':' + str(goalPoint[1]) + ':' + str(goalPoint[2]) + ')' )

    nextPoint = [startPoint[2], startPoint[1], startPoint[0]]
    while True:
        distance1 = 999
        distance2 = 999
     
        value = array2d[nextPoint[0]][nextPoint[1]][nextPoint[2]]
        x = nextPoint[2]
        y = nextPoint[1]
        z = nextPoint[0]
        for i in range(-1, 2):
            for j in range(-1,2):
                for k in range(-1,2):
                    if (validation2(k+z, j+y, i + x)):
                        if array2d[k+z][j+y][i+x]<value:
                                distance1 = findDistance(k+z,j+y, i+x)
                                if distance1 < distance2:
                                    distance2 = distance1
                                    nextPoint = [k+z, j+y,i+x]

        print ('('+ str(nextPoint[2])  + ':' + str(nextPoint[1]) + ':' + str(nextPoint[0]) + ')' )
        file.write(str(nextPoint[2])  + ' ' + str(nextPoint[1]) + ' ' + str(nextPoint[0]) + '\n') 

        if (nextPoint[0] == goalPoint[2] and nextPoint[1] == goalPoint[1] and nextPoint[2] == goalPoint[0]):
            break


def CheckStart():
    if goalPoint[2]>= RangeZ[1] or goalPoint[1] >=RangeY[1] or goalPoint[0]>= RangeX[1]:
        print("Goal Point is out of bounds ")
        quit()
    elif startPoint[2]>= RangeZ[1] or startPoint[1] >=RangeY[1] or startPoint[0]>= RangeX[1]:
        print("Start Point is out of bounds ")
        quit()
    else:
        array2d[goalPoint[2]][goalPoint[1]][goalPoint[0]] = 2

    if (array2d[goalPoint[2]][goalPoint[1]][goalPoint[0]] == 1 ):
        print("Goal Point is inside object")
        quit()
    elif (array2d[startPoint[2]][startPoint[1]][startPoint[0]] == 1 ):
        print("Start Point is inside object")
        quit()



#Open input file...

f=open(WorldInput,"r")
lines=f.readlines()

RangeX=[int(lines[0].split(' ')[0]), int(lines[0].split(' ')[1])]
RangeY=[int(lines[1].split(' ')[0]), int(lines[1].split(' ')[1])]
RangeZ=[int(lines[2].split(' ')[0]), int(lines[2].split(' ')[1])]


LoadCube1 = [int(lines[3].split(' ')[0]), int(lines[3].split(' ')[1]), int(lines[3].split(' ')[2]), int(lines[3].split(' ')[3])]
LoadCube2 = [int(lines[4].split(' ')[0]), int(lines[4].split(' ')[1]), int(lines[4].split(' ')[2]), int(lines[4].split(' ')[3])]
LoadSphere1 = [int(lines[5].split(' ')[0]), int(lines[5].split(' ')[1]), int(lines[5].split(' ')[2]), int(lines[5].split(' ')[3])]
LoadSphere2 = [int(lines[6].split(' ')[0]), int(lines[6].split(' ')[1]), int(lines[6].split(' ')[2]), int(lines[6].split(' ')[3])]

goalPoint = [int(lines[7].split(' ')[0]), int(lines[7].split(' ')[1]), int(lines[7].split(' ')[2])]
startPoint = [int(lines[8].split(' ')[0]), int(lines[8].split(' ')[1]), int(lines[8].split(' ')[2])]


f.close()

s = (RangeZ[1],RangeY[1],RangeX[1])
array2d = np.zeros((s), dtype=int)

# Adding Obstacles
addObstacleCube(LoadCube1[0],LoadCube1[1],LoadCube1[2],LoadCube1[3])
addObstacleCube(LoadCube2[0],LoadCube2[1],LoadCube2[2],LoadCube2[3])
addObstacleSphere(LoadSphere1[0],LoadSphere1[1],LoadSphere1[2],LoadSphere1[3])
addObstacleSphere(LoadSphere2[0],LoadSphere2[1],LoadSphere2[2],LoadSphere2[3])


#Check validation of start and end poibt
CheckStart()
#DoWavefront 
doRound(2)

#Building the path
file = open(PathOutput, "a") 
bouildPath()
file.close() 
print ('Path Complite!')

