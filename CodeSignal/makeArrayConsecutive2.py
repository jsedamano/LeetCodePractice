# Ratiorg got statues of different sizes as a present from CodeMaster for 
# his birthday, each statue having an nonnegative integer size. Since he 
# likes to make things perfect, he wants to arrange them from smallest to 
# largest so that each statue will be bigger than the previous one exactly 
# by 1. He may need some additional statues to be able to accomplish that. 
# Help him figure out the minimum number of additional statues needed.
#
# For statues = [6, 2, 3, 8] , the output should be solution (statues) = 3.
# Ratiorg needs statues of sizes 4, 5 and 7.
#
# Guaranteed constraints:
# 1 ≤ statues.length ≤ 10,
# 0 ≤ statues[i] ≤ 20.

def solution(statues):
    statues = sorted(statues)
    count = 0
    for i in range(len(statues) - 1):
        count += (statues[i + 1] - statues[i]) - 1
    return count



# --------------------------------
# Tests
def test_solution():
    # Example from problem description
    assert solution([6, 2, 3, 8]) == 3, "Test case 1 failed"
    
    # Edge case: consecutive numbers (no statues needed)
    assert solution([1, 2, 3, 4]) == 0, "Test case 2 failed"
    
    # Edge case: single statue
    assert solution([5]) == 0, "Test case 3 failed"
    
    # Edge case: two statues with gap
    assert solution([1, 5]) == 3, "Test case 4 failed"
    
    # Edge case: two consecutive statues
    assert solution([3, 4]) == 0, "Test case 5 failed"
    
    # Unsorted input
    assert solution([10, 5, 7]) == 3, "Test case 6 failed"
    
    # Large gaps
    assert solution([0, 20]) == 19, "Test case 7 failed"
    
    # Multiple gaps
    assert solution([1, 4, 7, 10]) == 6, "Test case 8 failed"
    
    # Random order with multiple gaps
    assert solution([15, 10, 12]) == 3, "Test case 9 failed"  # sorted: [10, 11, 12, 13, 14, 15]
    
    # Edge case: includes zero
    assert solution([0, 2, 4]) == 2, "Test case 10 failed"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_solution()