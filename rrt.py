#Dmitrii Karpenko
#For Introduction to Robotics
#2019


import numpy as np
import math  
import random

#*****************Files path*************************

WorldInput = "world.txt"

PathOutput = "path.txt"

PathOutput2 = "RRTAllPoints.txt"


#*******************Settings********************

NumberOfIterations = 1400

#********Clear the output file before writing******
file = open(PathOutput, "w") 
file.write('') 
file.close() 
########
#********Clear the output file before writing******
file = open(PathOutput2, "w") 
file.write('') 
file.close() 
########

def findDistance(x1, y1, z1, x2, y2, z2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return dist 


def createRandPoint():
    randomX = random.randint(rangeX[0], rangeX[1])
    randomY = random.randint(rangeY[0], rangeY[1])
    randomZ = random.randint(rangeZ[0], rangeZ[1])
    newCord = [randomX, randomY, randomZ]
    for k in range(len(AllPoints)):
        if AllPoints[k]== newCord:
            return False

    return newCord

def findClosePoint(randPoint, AllPoints):
    dist = 999
    closePoint = []
    for n in range(len(AllPoints)):
        temp = findDistance(randPoint[0], randPoint[1], randPoint[2], AllPoints[n][0], AllPoints[n][1],AllPoints[n][2])
        if (temp < dist):
            dist = temp
            closePoint = AllPoints[n]

    return closePoint

def newPoint(closePoint, randPoint):
    newPoint = []
    newPoint.append(closePoint[0])
    newPoint.append(closePoint[1])
    newPoint.append(closePoint[2])

    vector = []

    vector.append(randPoint[0]-closePoint[0])
    vector.append(randPoint[1]-closePoint[1])
    vector.append(randPoint[2]-closePoint[2])
    
    dist = findDistance(randPoint[0], randPoint[1], randPoint[2], closePoint[0], closePoint[1], closePoint[2])

    while newPoint<randPoint  :
        newPoint[0]+=vector[0]/dist
        newPoint[1]+=vector[1]/dist
        newPoint[2]+=vector[2]/dist
        if checkObsticles(newPoint):
            return False
     

    newPoint[0]= round(newPoint[0])
    newPoint[1]= round(newPoint[1])
    newPoint[2]=round(newPoint[2])
    for k in range(len(AllPoints)):
        if  AllPoints[k] == newPoint:
            return False

    return newPoint

def insideObsticleCube(center, point):
    side = center[3]
    side=side*2
    for i in range(-int(side/2), int(side/2)):
        for l in range(-int(side/2), int(side/2)):
                for c in range(-int(side/2), int(side/2)):
                    if point == [center[0]+i, center[1]+l, center[2]+c]:
                        return True
    return False

def insideObsticleSphere(center, point):
    radius = center[3]
    distCent = findDistance(point[0], point[1], point[2], center[0], center[1], center[2])
    if distCent <= radius:
        return True
    else:
        return False

def checkObsticles(point):
    obs1 = insideObsticleCube(LoadCube1, point)
    obs2 = insideObsticleCube(LoadCube2, point)
    obs3 = insideObsticleSphere(LoadSphere1, point)
    obs4 = insideObsticleSphere(LoadSphere2, point)
    if  obs1 or  obs2 or  obs3 or  obs4:
        return True
    else:
        return False


def checkIfGoulReach(point, Goal):
    dist = findDistance(point[0], point[1], point[2], Goal[0], Goal[1], Goal[2])
    if dist<2:
        return newPoint(point, Goal)
    else:
        return False



#Open input file...

f=open(WorldInput,"r")
lines=f.readlines()

rangeX=[int(lines[0].split(' ')[0]), int(lines[0].split(' ')[1])]
rangeY=[int(lines[1].split(' ')[0]), int(lines[1].split(' ')[1])]
rangeZ=[int(lines[2].split(' ')[0]), int(lines[2].split(' ')[1])]


LoadCube1 = [int(lines[3].split(' ')[0]), int(lines[3].split(' ')[1]), int(lines[3].split(' ')[2]), int(lines[3].split(' ')[3])]
LoadCube2 = [int(lines[4].split(' ')[0]), int(lines[4].split(' ')[1]), int(lines[4].split(' ')[2]), int(lines[4].split(' ')[3])]
LoadSphere1 = [int(lines[5].split(' ')[0]), int(lines[5].split(' ')[1]), int(lines[5].split(' ')[2]), int(lines[5].split(' ')[3])]
LoadSphere2 = [int(lines[6].split(' ')[0]), int(lines[6].split(' ')[1]), int(lines[6].split(' ')[2]), int(lines[6].split(' ')[3])]

StartPoint = [int(lines[7].split(' ')[0]), int(lines[7].split(' ')[1]), int(lines[7].split(' ')[2])]
GoalPoint = [int(lines[8].split(' ')[0]), int(lines[8].split(' ')[1]), int(lines[8].split(' ')[2])]


f.close()  



AllPoints = []


AllPoints.append(StartPoint)

for i in range(NumberOfIterations):

    print(str(i)+ "  of: "+ str(NumberOfIterations))

    randPoint = createRandPoint()
    if randPoint == False:
        continue
    if checkObsticles(randPoint):
        continue
    closePoint = findClosePoint(randPoint, AllPoints)

    newPoint1 = newPoint(closePoint, randPoint)
    if newPoint1 == False:
        continue
    AllPoints.append(newPoint1)
    newPoint2=checkIfGoulReach(newPoint1, GoalPoint)
    if newPoint2 == False:
        continue
    AllPoints.append(newPoint2)


AllPoints.remove(StartPoint)
file = open(PathOutput2, "a") 

for k in range(len(AllPoints)):
    file.write(str(AllPoints[k][0])  + ' ' + str(AllPoints[k][1]) + ' ' + str(AllPoints[k][2]) + '\n') 


file.close() 
file = open(PathOutput, "a") 

dist1 = findDistance(StartPoint[0], StartPoint[1], StartPoint[2], GoalPoint[0], GoalPoint[1], GoalPoint[2])
currentPoint = StartPoint
print(currentPoint)
check = 0
file.write(str(currentPoint[0])  + ' ' + str(currentPoint[1]) + ' ' + str(currentPoint[2]) + '\n') 
while not currentPoint == GoalPoint:

    if check > 500:
        print ("Finish point is unreachble or not connected with any point, try again to randomize the space again or increase the number of iterations.")
        break


    closePoint1 = findClosePoint(currentPoint, AllPoints)
    if closePoint1 == False:
        print("Goal point is unreachable")
    try:
        tmp = findDistance(closePoint1[0], closePoint1[1], closePoint1[2], GoalPoint[0], GoalPoint[1], GoalPoint[2])
    except:
        print ("Finish point is unreachble or not connected with any point, try again to randomize the space again or increase the number of iterations.")
        break
    if tmp<dist1:

        currentPoint = closePoint1
        dist1 = tmp
        print(currentPoint)
        file.write(str(currentPoint[0])  + ' ' + str(currentPoint[1]) + ' ' + str(currentPoint[2]) + '\n') 

        continue

    else:
        AllPoints.remove(closePoint1)
        continue

    check+=1
file.write(str(currentPoint[0])  + ' ' + str(currentPoint[1]) + ' ' + str(currentPoint[2]) + '\n') 

file.close() 
print("Path build")
