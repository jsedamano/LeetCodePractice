# Given an array of positive integers, return the number of elements that 
# are strictly greater than the average of all previous elements. Skip 
# the first element.
#
# Input: responseTimes = [100, 200, 150,300]
# Output: 2
# Explanation:
# - Day 0: 100 (no previous days, skip) 
# - Day 1: 200 > average(100) = 100 → count = 1 
# - Day 2: 150 vs average(100, 200) = 150 → not greater → count = 1 
# - Day 3: 300 > average(100, 200, 150) = 150 → count = 2 Return 2.
#
# Constraints
# 0 <= responseTimes.length <= 1000
# 1 <= responseTimes[i] <= 10^9 for 0 <= i < responseTimes.length

def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) == 0:
        return 0
    sumsofar = responseTimes[0]
    count = 0
    for i in range(1, len(responseTimes)):
        if responseTimes[i] > (sumsofar / i):
            count += 1
        sumsofar += responseTimes[i]
    return count



# --------------------------------
# Tests
def test_solution():
    # Example from problem description
    assert countResponseTimeRegressions([100, 200, 150, 300]) == 2, "Test case 1 failed"
    
    # Edge case: empty list
    assert countResponseTimeRegressions([]) == 0, "Test case 2 failed"
    
    # Edge case: single element
    assert countResponseTimeRegressions([42]) == 0, "Test case 3 failed"
    
    # All elements strictly increasing
    assert countResponseTimeRegressions([1, 2, 3, 4, 5]) == 4, "Test case 4 failed"
    
    # All elements the same
    assert countResponseTimeRegressions([10, 10, 10, 10]) == 0, "Test case 5 failed"
    
    # All elements strictly decreasing
    assert countResponseTimeRegressions([5, 4, 3, 2, 1]) == 0, "Test case 6 failed"
    
    # Large numbers
    assert countResponseTimeRegressions([10**9, 10**9, 10**9]) == 0, "Test case 7 failed"
    
    # Alternating above/below average
    assert countResponseTimeRegressions([10, 20, 5, 30, 5]) == 2, "Test case 8 failed"
    
    # Only last element greater than previous average
    assert countResponseTimeRegressions([1, 1, 1, 10]) == 1, "Test case 9 failed"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_solution()