'''
Batteries Charging

Task
------
Partition a list of items into two lists such that the difference between
the sums of each is the least possible (as near equilibrium as possible)

Notes
------
The code determines what half of the total sum of all items is and then attempts
to add items one by one to reach as close to that half way point as possible.
This process brute forces as many combinations of items on the left or right as
possible and stores the minimum differences in a list. Once it finishes
iterating through all the combinations, the list of differences is sorted
leaving the smallest at the bottom. That value is then returned as the answer.

I am sure there is a better method but this is deceptively difficult to find a
pattern of behavior within different combinations of inputs.
'''

from math import ceil

def checkio( stones ):
    '''
    minimal possible weight difference between stone piles
    '''

    # show me what I am working with, sorted so that we can control SOME of the
    # behavior
    stones.sort(reverse=True)
    print ( stones )

    # handle simple cases
    if len( stones ) == 0:
        return 0
    if len( stones ) == 1:
        return stones[0]
    if len( stones ) == 2:
        return abs(stones[0] - stones[1])

    # find the value equal to half the sum of all stones. Use the ceiling since
    # we are doing all of our math on only the left side so we want to get as
    # close as possible
    half = ceil( sum( stones ) / float( 2 ) )
    print ("Half: %d" % half)

    # init some containers
    differences = []
    used_items  = []

    # the largest item will be the leftmost item
    largest = stones.pop(0)
    while len( stones ) > 0:
        # begin fresh
        left  = [largest]
        right = list(used_items)

        # lets see the state of things (but only because the lists are so small)
        print(stones,right)

        # iterate through the remaining stones and add up stones to get as close
        # as possible to half of the total sum of all items. The left will hold
        # all items whose sum is less than the half, the right gets the rest
        for stone in stones:
            if sum(left) + stone <= half:
                left.append(stone)
            else:
                right.append(stone)

            # visualize the sides and the current difference between them.
            # (I would never do this for large arrays)
            print ("[ %s|%d ]---( %d )---[ %d|%s ]" % (\
                ','.join(str(x) for x in left), \
                sum(left), \
                abs( sum( left ) - sum( right ) ), \
                sum(right), \
                ','.join(str(y) for y in right)\
            ))

        # record the difference of the two sums
        diff = abs( sum( left ) - sum( right ) )
        print("Current Difference: %d\n" % diff)
        differences.append( diff )

        # if the left only has the one value it means it was not able to
        # be added to any other item to get less than the half. In this case,
        # move this item to the list of used items and get a new item to use as
        # the largest.
        if len( left ) > 1:
            used_items.append(stones.pop(0))
        else:
            used_items.append(largest)
            largest = stones.pop(0)

    # sort our list of differences and grab the first item to return as the min
    differences.sort()
    min_diff = differences[0]
    print("Minimum Difference was found to be: %d\n" % min_diff)
    return min_diff


if __name__ == '__main__':
    assert checkio([10,10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5,5,6,5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    assert checkio([9,9,7,6,5]) == 0, "Seven"
    print ('All is ok')