import math


def elevatorDistance(array):
    """

Imagine you start on the 5th floor of a building, then travel down to the 2nd floor, then back up to the 8th floor.
 You have travelled a total of 3 + 6 = 9 floors of distance.

Given an array representing a series of floors you must reach by elevator, return an integer representing the total
distance travelled for visiting each floor in the array in order.

Array will always contain at least 2 floors. Random tests will contain 2-20 elements in array, and floor values between 0 and 30.

    """
    res = 0
    for i in range(len(array) - 1):
        res += abs(array[i + 1] - array[i])
    return res

if __name__ == "__main__":
    print(elevatorDistance([5, 2, 8]))
    assert elevatorDistance([5, 2, 8]) == 9
    assert elevatorDistance([1, 2, 3]) == 2
    assert elevatorDistance([7, 1, 7, 1]) == 18
    assert elevatorDistance([3, 3]) == 0

    print("ALL test passed!")
