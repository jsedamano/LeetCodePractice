# Given an array of integers, find the pair of adjacent elements that has the largest 
# product and return that product.
# 
# For inputArray = [3, 6, -2, -5, 7, 3], the output should be solution (inputArray) = 21.
# 7 and 3 produce the largest product.
# 
# Guaranteed constraints:
# 2 ≤ inputArray.length ≤ 10,
# -1000 ≤ inputArray[i] ≤ 1000.

def solution(inputArray):
    max_product = float("-inf")
    for i in range(len(inputArray) - 1):
        temp = inputArray[i] * inputArray[i + 1]
        if temp > max_product: # Can be replaced with max(max_product, temp)
            max_product = temp
    return max_product



# --------------------------------
# Tests
def test_solution():
    # Test case 1: Example from problem
    assert solution([3, 6, -2, -5, 7, 3]) == 21, "Example case failed"

    # Test case 2: Minimum length (exactly two elements)
    assert solution([1, 2]) == 2, "Two elements positive failed"
    assert solution([-5, -4]) == 20, "Two elements both negative failed"
    assert solution([-1000, 1000]) == -1000000, "Two elements opposite signs failed"

    # Test case 3: Maximum product at the beginning
    assert solution([9, 1, 1, 1]) == 9, "Max at start failed"

    # Test case 4: Maximum product at the end
    assert solution([1, 1, 9, 1]) == 9, "Max at end failed"

    # Test case 5: Contains zeros
    assert solution([0, 1000, 0, -1000]) == 0, "Zeros handling failed"

    # Test case 6: All negatives where best is a positive product
    assert solution([-1, -2, -3]) == 6, "All negatives failed"

    # Test case 7: Alternating signs
    # Pairs: 5*-1=-5, -1*-2=2, -2*-3=6 => max 6
    assert solution([5, -1, -2, -3]) == 6, "Alternating signs failed"

    # Test case 8: Mixed values with multiple equal maxima
    # Pairs: 2*3=6, 3*2=6, 2*3=6
    assert solution([2, 3, 2, 3]) == 6, "Multiple equal maxima failed"

    # Test case 9: Boundary values within constraints
    assert solution([1000, 1000]) == 1000000, "Upper bound values failed"
    assert solution([-1000, -999]) == 999000, "Near lower bound negatives failed"

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_solution()