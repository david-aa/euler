nPaths = 0;
def move_point(point, limit):
    global nPaths
    if point == limit:
        #print("Finished!")
        nPaths += 1
    if point[1] < limit[1]:
        # Continue down...
        new_point = (point[0], point[1]+1)
        # print("From", point, "to", new_point)
        move_point(new_point, limit)
        # And lets go right too
        if point[0] < limit[0]:
            new_point = (point[0]+1, point[1])
            # print("From", point, "to", new_point)
            move_point(new_point, limit)
    elif point[0] < limit[0]:
        new_point = (point[0]+1, point[1])
        # print("From", point, "to", new_point)
        move_point(new_point, limit)

move_point((0, 0), (20, 20))
print("N Paths", nPaths)
