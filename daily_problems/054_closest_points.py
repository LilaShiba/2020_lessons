'''
This problem was asked by Google.

Given a set of points (x, y) on a 2D cartesian plane, 
find the two closest points. For example, given 
the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], 
return [(-1, -1), (1, 1)]

'''
import math
arr = [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]
def closest_points(arr):
    points = sorted(arr, key=lambda x:x [0]**2 + x[1]**2)
    return points

def points_distance(point1, point2):
    # euclidean plane
    return round(math.sqrt( (point2[0] - point1[1])**2 + (point2[1] - point1[1])**2),2)

def brute_force(points):
    points_length = len(points)
    if points_length < 2:
        return False
    best_dist = float('inf')
    best_pair = ()

    for x in range(points_length):
        for y in range(x+1, points_length-1):
            new_dist = points_distance(points[x], points[y])
            if new_dist < best_dist:
                best_dist, best_pair = new_dist, (points[x], points[y])
    return best_dist, best_pair

def cp(points):
    points_length = len(points)
    pX = sorted(points, key=lambda x:x[0])
    pY = sorted(points, key=lambda x:x[1])

    if points_length <= 3:
        return brute_force(points)
    
    xL = [x for x in pX[:points_length//2]]
    xR = [x for x in pX[points_length//2+1:]]
    mid = pX[points_length//2]
    mid = mid[0]

    yL = [y for y in pY if y[0] < mid]
    yR = [y for y in pY if y[0] > mid]

    dl, pairL = cp(xL, yL)
    dr, pairR = cp(xR, yR)
    d = min(pariL, pairR)

    yS = [y for y in pY if mid-y[0] < d]
    yS_count = len(yS)-1
    



    

print(cp(arr))

