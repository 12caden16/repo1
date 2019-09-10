import math

print("Vector Addition Calculator")
print(" ")

numVector=0
vectorMag=0
vectorX=0
vectorY=0
vectorDeg=0
totalMag=0
totalX=0
totalY=0
totalDeg=0
totalHyp=0

numVector=int(input("Enter the number of vectors: "))

for num in range(0,numVector):
   print(" ")
   vectorMag=float(input("Enter magnitude of vector: "))
   vectorDeg=float(input("Enter degree of vector from positive x-axis(45, 180, 275, etc.): "))
   if vectorDeg<90 or vectorDeg>0:

        vectorX=vectorMag*(math.cos(math.radians(vectorDeg)))
        vectorY=vectorMag*(math.sin(math.radians(vectorDeg)))

        totalX=totalX+vectorX
        totalY=totalY+vectorY

   elif vectorDeg > 90 and vectorDeg<180:

        vectorX=vectorMag*(math.cos(math.radians(vectorDeg)))
        vectorY=vectorMag*(math.sin(math.radians(vectorDeg)))*(-1)

        totalX=totalX+vectorX
        totalY=totalY+vectorY

   elif vectorDeg > 180 and vectorDeg<270:

        vectorX=vectorMag*(math.cos(math.radians(vectorDeg)))*(-1)
        vectorY=vectorMag*(math.sin(math.radians(vectorDeg)))*(-1)

        totalX=totalX+vectorX
        totalY=totalY+vectorY

   elif vectorDeg > 270 and vectorDeg<360:

        vectorX=vectorMag*(math.cos(math.radians(vectorDeg)))*(-1)
        vectorY=vectorMag*(math.sin(math.radians(vectorDeg)))

        totalX=totalX+vectorX
        totalY=totalY+vectorY

   elif vectorDeg > 360:
        print("User ERROR")
   else:
        vectorDeg=vectorDeg

        if vectorDeg == 0:
            vectorX=0
            vectorY=vectorMag
        elif vectorDeg==90:
            vectorX=vectorMag
            vectorY=0
        elif vectorDeg==180:
            vectorX=0
            vectorY=vectorMag*(-1)
        elif vectorDeg==270:
            vectorY=0
            vectorX=vectorMag*(-1)
        elif vectorDeg==360:
            vectorX=0
            vectorY=vectorMag
        else:
            print("User ERROR")

            totalX=totalX+vectorX
            totalY=totalY+vectorY
else:

    totalDeg=math.degrees(math.atan(totalY/totalX))

    if totalY>0 and totalX<0:
        totalDeg=180+totalDeg
    elif totalY<0 and totalX<0:
        totalDeg=180+totalDeg
    elif totalY<0 and totalX>0:
        totalDeg=360+totalDeg
    else:
        totalDeg=totalDeg

    totalMag=math.sqrt((totalX**2)+(totalY**2))

    print(" ")
    print("The resultant Vector has a magnitude of",totalMag,"and a direction of",totalDeg,"Degrees")