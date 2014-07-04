'''
Median

-- Task -----------------------------------------------------------------------------
A median is a numerical value separating the upper half of a list of numbers from
the lower half. In a list where there are an odd number of entities, the median is
the number found in the middle of the list. If the list contains an even number of
entities, then there is no single middle value, instead the median becomes the
average of the two numbers found in the middle. For this mission, you are given a
non-empty list of natural numbers (X). With it, you must separate the upper half of
the numbers from the lower half and find the median.

Input: A list of integers.
Output: The median, a float.
'''
def checkio(data):
    data.sort()

    length = len(data)
    mid    = int( length / 2 )

    if length % 2 == 0:
        return float( data[mid - 1] + data[mid] ) / 2
    else:
        return data[ mid ]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")