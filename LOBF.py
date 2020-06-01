import math
i = input("Enter number of data points: ")
dataPoints = []
for x in range(int(i)):
    i = input("enter data point: ")
    if("," in i):
        dataPoints.append(i)
    else:
        print("Error")
        break

dataPoints = [ j.split(",") for j in dataPoints ]
dataPoints = [[float(u) for u in lst] for lst in dataPoints]
averageX = 0
averageY = 0
standardDevX = 0
standardDevY = 0
for s in dataPoints:
    averageX += s[0]
for v in dataPoints:
    averageY += v[1]
averageX = averageX/len(dataPoints)
averageY = averageY/len(dataPoints)

for b in dataPoints:
    v1 =(b[0] - averageX) ** 2
    standardDevX += v1
for c in dataPoints:
    v2 =(b[1] - averageY) ** 2
    standardDevY += v2
standardDevX = standardDevX/len(dataPoints)
standardDevY = standardDevY/len(dataPoints)

sampleSize = len(dataPoints)
totalX = averageX * len(dataPoints)
totalY = averageY * len(dataPoints)
totalX2 = 0
totalY2 = 0
totalXY = 0

for x1 in dataPoints:
    d1 = (x1[0]) ** 2
    totalX2 += d1
for y1 in dataPoints:
    f1 = (y1[1]) ** 2
    totalY2 += f1
for q in dataPoints:
    d2 = q[0] * q[1]
    totalXY += d2
top = (sampleSize * totalXY) - ((totalX) * (totalY))
try:
    bottom = math.sqrt( ((sampleSize * totalX2) - (totalX ** 2)) * ((sampleSize * totalY2) - (totalY ** 2)) )
except:
    bottom = 0
r = 0
if(bottom == 0):
    r = 1
else:
    r = top/bottom
print(" ")
print("r = " + str(r) + " (Correlation Coefficent)")
mode = ''
def checkX():
    global r
    global mode
    if(r > 0):
        mode = 'positive'
    elif(r > 0):
        mode = 'negative'
    if(mode == 'positive' and r <= 0.25):
        print("Weak Positive Correlation")
    if(r > 0.25 and r <= 0.5):
        print("Midly Weak Positive Correlation")
    if(r > 0.5 and r <= 0.75):
        print("Midly Strong Positive Correlation")
    if(r > 0.75 and r <= 1.0):
        print("Strong Positive Correlation")
    if(mode == 'negative' and r >= -0.25):
        print("Weak Negative Correlation")
    if(r < -0.25 and  r >= -0.5):
        print("Midly Weak Negative Correlation")
    if(r < -0.5 and r >= -0.75):
        print("Midly Strong Negative Correlation")
    if(r < -0.75 and r >= -1):
        print("Strong Negative Correlation")
checkX()

#calc LOBF
slope = 0
top1 = ((sampleSize * totalXY) - (totalX * totalY))
bottom1 = ((sampleSize * totalX2) - (totalX ** 2))
try:
    slope = top1/bottom1
except:
    slope = 0
try:
    constant = ((totalX2 * totalY) - (totalX * totalXY))/((sampleSize * totalX2) - (totalX ** 2))
except:
    constant = 0
print(" ")
print("Line of Best Fit: Y = mx + b")
print("m = " + str(slope))
print("b = " + str(constant))
def check1():
    if(constant > 0):
        print("Y = " + str(slope) + "x" + " + " + str(constant))
    elif(constant < 0):
        print("Y = " + str(slope) + "x" + " - " + str(constant))
    elif(constant == 0):
        print("Y = " + str(slope) + "x" + " or " + "Y = " + str(slope) + "x" + " + " + "0")
check1()
print("")
io = []
po = []
for uj in dataPoints:
    io.append(float(uj[0]))
print("X-Range: " + str(min(io)) + " - " + str(max(io)))
for de in dataPoints:
    po.append(float(de[1]))
print("Y-Range: " + str(min(po)) + " - " + str(max(po)))
print(" ")
for m in dataPoints:
    a5 = (m[0] * slope) + constant
    a6 = m[1]
    res = a6 - a5
    print("(" + str(m[0]) + "," + str(m[1]) + ")" + " Predicted Value: " + str(a5) + " Residual: " + str(res))
print(" ")
print("type: exit, to escape")
while True:
    j = input("Enter X-Value to get predicted Y-Value: ")
    try:
        p = (float(j) * slope) + constant
        print("Your predicted Y-value is " + str(p) + " (" + str(j) + "," + str(p) + ")")
        if(float(j) >= min(io) and float(j) <= max(io)):
            print("Interpolation")
        else:
            print("Exterpolation")
        print('')
    except:
        if(j == "exit"):
            print("Exited")
            break
        else:
            print("invalid input")
            print('')
