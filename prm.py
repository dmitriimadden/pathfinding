#Dmitrii Karpenko
#For Introduction to Robotics
#2019


import numpy as np
import math  
import random

#*****************Files path*************************

WorldInput = "world5.txt"

PathOutput = "prm_world5.txt"

nodes="RRTAllPoints.txt"

#*******************Settings********************

NumberOfPointsInSpace = 2800

DistanceToNeighbor = [2, 5] #[From, UpTo]

#********Clear the output file before writing******
file = open(PathOutput, "w") 
file.write('') 
file.close() 
########
#********Clear the output file before writing******
file = open(nodes, "w") 
file.write('') 
file.close() 
########
def qarter():
        arr = [[(rangeX[1]/2)-1, (rangeY[1]/2)-1, (rangeZ[1]/2)-1], [(rangeX[1])-1, (rangeY[1]/2)-1, (rangeZ[1]/2)-1], [(rangeX[1]/2)-1,(rangeY[1])-1, (rangeZ[1]/2)-1], [(rangeX[1])-1,(rangeY[1])-1]]
        return arr

def findDistance(x1, y1, z1, x2, y2, z2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return dist 

def addObstacleCube(x,y, z,side):
        side = side*1.2
        for i in range(-int(side/2), int(side/2)):
                for l in range(-int(side/2), int(side/2)):
                        for c in range(-int(side/2), int(side/2)):
                                for m in range(len(arrat)):
                                        if arrat[m] == [x+i, y+l, z+c]:
                                                arrat.remove([x+i, y+l, z+c])
                                                break
                                continue

def addObstacleSphere(x,y, z,radius):
        radius= radius*1.4
        for m in range(len(arrat)):
                distCent = findDistance(arrat[m][0], arrat[m][1], arrat[m][2], x, y, z)
                if distCent<=radius:
                        arrat.remove(arrat[m])
                        break
def insideObsticleSphere(center, point):
    radius = center[3]
    distCent = findDistance(point[0], point[1], point[2], center[0], center[1], center[2])
    if distCent <= radius:
        return True
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

start = [int(lines[7].split(' ')[0]), int(lines[7].split(' ')[1]), int(lines[7].split(' ')[2])]
finish = [int(lines[8].split(' ')[0]), int(lines[8].split(' ')[1]), int(lines[8].split(' ')[2])]


f.close()           

quarter = [[rangeX[1]/2,rangeY[1]/2,rangeZ[1]/2],[rangeX[1],rangeY[1]/2,rangeZ[1]/2], [rangeX[1],rangeY[1],rangeZ[1]/2],[rangeX[1]/2,rangeY[1],rangeZ[1]/2],[rangeX[1]/2,rangeY[1]/2,rangeZ[1]], [rangeX[1],rangeY[1]/2,rangeZ[1]], [rangeX[1],rangeY[1],rangeZ[1]], [rangeX[1]/2,rangeY[1],rangeZ[1]]]

arrat = []

arrat.append(start)
arrat.append(finish)


for k in range(len(quarter)):

        while len(arrat)<(k+1)*(NumberOfPointsInSpace/4):
                randomX = random.randint(quarter[k][0]-quarter[0][0], quarter[k][0])
                randomY = random.randint(quarter[k][1]-quarter[0][1], quarter[k][1])
                randomZ = random.randint(quarter[k][2]-quarter[0][2], quarter[k][2])
                newCord = [randomX, randomY, randomZ]
                if newCord not in arrat:
                        arrat.append(newCord)
                        print(newCord)
                        



# Adding Obstacles
addObstacleCube(LoadCube1[0],LoadCube1[1],LoadCube1[2],LoadCube1[3])
addObstacleCube(LoadCube2[0],LoadCube2[1],LoadCube2[2],LoadCube2[3])
addObstacleSphere(LoadSphere1[0],LoadSphere1[1],LoadSphere1[2],LoadSphere1[3])
addObstacleSphere(LoadSphere2[0],LoadSphere2[1],LoadSphere2[2],LoadSphere2[3])

file = open(nodes, "a") 

for i in range(len(arrat)):
        newArr = []
        newArr.append(arrat[i][0])
        newArr.append(arrat[i][1])
        newArr.append(arrat[i][2])

        

        for k in range(len(arrat)):
                compareArr = []
                compareArr.append(arrat[k][0])
                compareArr.append(arrat[k][1])
                compareArr.append(arrat[k][2])
                dist = findDistance(newArr[0], newArr[1], newArr[2], compareArr[0], compareArr[1], compareArr[2])
                 
                if dist>DistanceToNeighbor[0] and dist <DistanceToNeighbor[1]:
                        arrat[i].append(compareArr)
                        print('Connect points with neighbors')
                        print(compareArr)
file.close() 



path = []

start = []
startPoint = []
startPoint.append(arrat[0][0])
startPoint.append(arrat[0][1])
startPoint.append(arrat[0][2])
start.append(startPoint)
start.append(startPoint)
start.append(0)
start.append(False)
path.append(start)

z = 0
loopcount = len(path)
w = 0
i=0
k=0

while w < loopcount:
        print(loopcount)
        if path[w][3] == False:
                nextPoint = path[w][0]
                distance = path[w][2]
                for i in range(len(arrat)):
                        if arrat[i][0] == nextPoint[0] and arrat[i][1] == nextPoint[1] and arrat[i][2] == nextPoint[2]:
                                for k in range(3, len(arrat[i])):
                                                                                
                                        for z in range(len(path)):
                                                if path[z][0][0] == arrat[i][k][0] and path[z][0][1] == arrat[i][k][1]and path[z][0][2] == arrat[i][k][2]:
                                                        if path[z][3] == True:
                                                                break
                                                        else:
                                                                dist = findDistance(arrat[i][0], arrat[i][1], arrat[i][2], arrat[i][k][0], arrat[i][k][1], arrat[i][k][2])
                                                                if (path[z][2]>distance+dist):
                                                                      path[z][2] = distance+dist
                                                                      print("new distance updated")
                                                                break     

                                                else:
                                                        continue
                                        if z == len(path)-1:
                                                point = []
                                                dist = findDistance(arrat[i][0], arrat[i][1],arrat[i][2], arrat[i][k][0], arrat[i][k][1], arrat[i][k][2])
                                                point.append(arrat[i][k])
                                                prevPoint = []
                                                prevPoint.append(arrat[i][0])
                                                prevPoint.append(arrat[i][1])
                                                prevPoint.append(arrat[i][2])
                                                point.append(prevPoint)
                                                point.append(dist+distance)
                                                point.append(False)
                                                path.append(point)
                                                loopcount +=1
                                                w=0

                                                print("Node added")

                                for m in range(len(path)):
                                        if path[m][0][0] == nextPoint[0] and path[m][0][1] == nextPoint[1]and path[m][0][2] == nextPoint[2]:
                                                path[m][3] = True
                                        
        else:
                w+=1


pponit = []
pponit.append(finish[0])
pponit.append(finish[1])
pponit.append(finish[2])

file = open(PathOutput, "a") 
check = 0
while True:
        if check > 500:
                print ("Finish point is unreachble or not connected with any point, try again to randomize the space again or increase the number of points.")
                break
        file.write(str(pponit[0])  + ' ' + str(pponit[1]) + ' ' + str(pponit[2]) + '\n') 
        print(pponit)
        if pponit == [0,0,0]:
                break
        for s in range(len(path)):
                if path[s][0]==pponit:
                        pponit = path[s][1]
                        break
        
        check +=1






#Building the path
file.close() 

print ('Path Complite!')







