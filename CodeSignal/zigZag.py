# Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.
# 
# Given an array of integers numbers, your task is to check all the triples of 
# its consecutive elements for being a zigzag. More formally, your task is to 
# construct an array of length numbers.length - 2, where the ith element of the 
# output array equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) 
# is a zigzag, and 0 otherwise.
# 
# Example:
# For numbers = [1, 2, 1, 3, 4], the output should be solution(numbers) = [1, 1, 0].
# - (numbers[0], numbers[1], numbers[2]) = (1, 2, 1) is a zigzag, because 1 < 2 > 1
# - (numbers[1], numbers[2] , numbers[3]) = (2, 1, 3) is a zigzag, because 2 > 1 < 3
# - (numbers[2], numbers[3] , numbers[4]) = (1, 3, 4) is not a zigzag, because 1 < 3 < 4
#
# Guaranteed constraints:
# 3 ≤ numbers.length ≤ 100,
# 1 ≤ numbers[i] ≤ 10^9.

def solution(numbers):
    n = len(numbers)
    out = [0] * (n - 2)
    for i in range(n - 2):
        a, b, c = numbers[i], numbers [i + 1], numbers[i + 2]
        if (a < b > c) or (a > b < c):
            out[i] = 1
    return out



# --------------------------------
# Tests
def test_solution():
    # Test case 1: Example from problem
    assert solution([1, 2, 1, 3, 4]) == [1, 1, 0], "Test 1 failed"
    
    # Test case 2: All zigzags (alternating)
    assert solution([1, 3, 2, 4, 3]) == [1, 1, 1], "Test 2 failed"
    
    # Test case 3: No zigzags (ascending)
    assert solution([1, 2, 3, 4, 5]) == [0, 0, 0], "Test 3 failed"
    
    # Test case 4: No zigzags (descending)
    assert solution([5, 4, 3, 2, 1]) == [0, 0, 0], "Test 4 failed"
    
    # Test case 5: Minimum length (3 elements)
    assert solution([1, 2, 1]) == [1], "Test 5 failed"
    assert solution([3, 1, 2]) == [1], "Test 6 failed"
    assert solution([1, 2, 3]) == [0], "Test 7 failed"
    
    # Test case 6: Mixed patterns
    assert solution([5, 3, 8, 2, 7]) == [1, 1, 1], "Test 8 failed"
    
    # Test case 7: Equal consecutive values
    assert solution([1, 2, 2, 3]) == [0, 0], "Test 9 failed"
    
    # Test case 8: Large numbers
    assert solution([1000000000, 1, 999999999]) == [1], "Test 10 failed"
    
    # Test case 9: Peak pattern (a < b > c)
    assert solution([1, 5, 2, 6, 3]) == [1, 1, 1], "Test 11 failed"
    
    # Test case 10: Valley pattern (a > b < c)
    assert solution([5, 1, 6, 2, 7]) == [1, 1, 1], "Test 12 failed"
    
    print("All tests passed! ✓")

if __name__ == "__main__":
    test_solution()