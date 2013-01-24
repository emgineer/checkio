def slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return 'INF'
    else:
        return (y2 - y1)/(x2 - x1)

def intercept(slope, x, y):
    if slope == 'INF':
        slope = 0
    return y - (slope * x)

def checkio(data):
    # coordinates
    xw1, yw1 = data[0]
    xw2, yw2 = data[1]
    xa, ya   = data[2]
    xb, yb   = data[3]

    m1 = slope(xw1, yw1, xw2, yw2)
    m2 = slope(xa, ya, xb, yb)

    b1 = intercept(m1, xw1, yw1)
    b2 = intercept(m2, xa, ya)

    #parallel if they have the same slope but different y intercepts 
    if m1 == m2:
        if b1 != b2:
            print ("LOL: Parallel\n----\n")
            return False

    print("\n----\n")
    if m1 == 'INF':
        m1 = 0
    if m2 == 'INF':
        m2 = 0

    if m1 == 0:
        x = 0
    else:
        x = ((m2 * xb) + b2 - b1)/m1

    print("x: %d\n----\n" % x)


    # determine the direction of the shot to validate it would hit the wall
    if xb <= xa and x <= xb:
        return True
    elif xb >= xa and x >= xb:
        return True
    else:
        return False



if __name__ == '__main__':
    assert checkio([[0, 0], [0, 2], [5, 1], [0, 1]]) == True,  "First"
    assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "Reverse First"
    assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True,  "Second"
    assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "Third"
    assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True,  "Fourth, shot in butt of wall :)"
    assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "Fifth, parallel"
    assert checkio([[2, 4], [2, 0], [0, 2], [2, 3]]) == True,  "Sixth, Vertical wall"