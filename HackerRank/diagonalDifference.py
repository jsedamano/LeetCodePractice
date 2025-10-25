# Given a square matrix, calculate the absolute difference between the 
# sums of its diagonals.
# 
# For example, the square matrix arr is shown below:
# 1 2 3
# 4 5 6
# 9 8 9
#
# The left-to-right diagonal = 1 + 5 + 9 = 15
# The right-to-left diagonal = 3 + 5 + 9 = 17
# Their absolute difference is |15-17| = 2.

def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    n = len(arr)
    for i in range(n):
        left_to_right += arr[i][i]
        right_to_left += arr[i][n - 1 - i]
    return abs(left_to_right - right_to_left)



# --------------------------------
# Tests
def test_solution():
    # Example from problem description
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]
    ]
    assert diagonalDifference(arr) == 2, "Test case 1 failed"

    # 1x1 matrix should return 0
    assert diagonalDifference([[5]]) == 0, "Test case 2 failed"

    # 2x2 matrix where diagonals sum equal
    assert diagonalDifference([[1, 2], [3, 4]]) == 0, "Test case 3 failed"

    # Left diagonal larger
    arr2 = [
        [11, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # left: 11 + 5 + 9 = 25, right: 3 + 5 + 7 = 15 -> diff = 10
    assert diagonalDifference(arr2) == 10, "Test case 4 failed"

    # 4x4 matrix
    arr3 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    # left: 1+6+11+16 = 34, right: 4+7+10+13 = 34 -> diff = 0
    assert diagonalDifference(arr3) == 0, "Test case 5 failed"

    print("All tests passed!")

if __name__ == "__main__":
    test_solution()