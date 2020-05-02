from math import atan2, sqrt 
def mirrored_area(pos, dimensions, distance):
    node_mirrored=[]
    for i in range(len(pos)):
        points=[]
        for j in range(-(distance//dimensions[i])-1, (distance//dimensions[i]+2)):
            points.append(get_mirror(j, pos[i], dimensions[i]))
        node_mirrored.append(points)
    return node_mirrored

def get_mirror(mirror_no, coordinates, dimensions):
    res=coordinates
    mirror_rotation=[2*coordinates, 2*(dimensions-coordinates)]
    if(mirror_no<0):
        for i in range(mirror_no, 0):
            res-=mirror_rotation[(i+1)%2]
    else:
        for i in range(mirror_no, 0, -1):
            res+=mirror_rotation[i%2]
    return res 

def solution(dimensions, your_position, guard_position, distance):
    mirrored = [mirrored_area(your_position, dimensions, distance),mirrored_area(guard_position, dimensions, distance)]
    angles_dist = {}
    result = set()
    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                beam = atan2((your_position[1]-k), (your_position[0]-j))
                l = sqrt((your_position[0]-j)**2 + (your_position[1]-k)**2)
                if [j,k] != your_position and distance >= l:
                    if((beam in angles_dist and angles_dist[beam] > l) or beam not in angles_dist):
                        if i == 0:
                            angles_dist[beam] = l
                        else:
                            angles_dist[beam] = l
                            result.add(beam)
    return len(result) 

