def sort_points(points,ref):
    rx,ry=ref
    def distance(p):
        x,y=p
        return(x-rx)**2+(y-ry)**2
    points.sort(key=distance)
    return points
points=[(0,1),(0,3),(1,2)]
ref=(0,0)
print(sort_points(points,ref))
