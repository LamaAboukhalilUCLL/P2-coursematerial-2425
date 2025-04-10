#should return the point in points with minimum distance to target_point
#points: [(x1,y1), (x2,y2), ..]
def closest(points, target_point):
    result= min(points, key= lambda point: ((target_point[0]-point[0])**2 + (target_point[1]-point[1])**2)**0.5)
    return result


    