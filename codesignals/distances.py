class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
def largestDistance(a):
    points = buildpoints(a)
    distance = getdistances(points)
    return max(distance)
def buildpoints(array):
    xs = []
    ys = []
    points = []
    for i in range(0,len(array)//2):
        
        xs.append(array[i * 2])
        ys.append(array[i * 2 + 1])
    for x,y in zip(xs,ys):
        points.append(Point(x,y))
    return points
def getdistances(points):
    counter = 1
    distances = []
    for a in points:
        for b in points[counter:]:
            distances.append(distance(a,b))
        
        counter = counter + 1
    return (distances)
def distance(pointa,pointb):
    return max(abs(pointa.x - pointb.x), abs(pointa.y - pointb.y))
