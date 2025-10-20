# Write a function that returns the sum of two numbers.
# 
# For param1 = 1 and param2 = 2, the output should be solution (param1, param2) = 3.
# 
# Guaranteed constraints:
# -1000 ≤ param1 ≤ 1000,
# -1000 ≤ param2 ≤ 1000.

def solution(param1, param2):
    return param1 + param2



# --------------------------------
# Tests
def test_solutions():
    # Test case 1: Example from problem
    assert solution(1, 2) == 3, "Test 1 failed"
    
    # Test case 2: Both positive numbers
    assert solution(100, 200) == 300, "Test 2 failed"
    
    # Test case 3: Both negative numbers
    assert solution(-50, -30) == -80, "Test 3 failed"
    
    # Test case 4: Positive and negative (positive result)
    assert solution(100, -30) == 70, "Test 4 failed"
    
    # Test case 5: Positive and negative (negative result)
    assert solution(30, -100) == -70, "Test 5 failed"
    
    # Test case 6: One zero
    assert solution(0, 42) == 42, "Test 6 failed"
    assert solution(42, 0) == 42, "Test 7 failed"
    
    # Test case 7: Both zeros
    assert solution(0, 0) == 0, "Test 8 failed"
    
    # Test case 8: Numbers that cancel out
    assert solution(100, -100) == 0, "Test 9 failed"
    
    # Test case 9: Maximum constraints
    assert solution(1000, 1000) == 2000, "Test 10 failed"
    
    # Test case 10: Minimum constraints
    assert solution(-1000, -1000) == -2000, "Test 11 failed"
    
    # Test case 11: Maximum and minimum
    assert solution(1000, -1000) == 0, "Test 12 failed"
    
    # Test case 12: Random values
    assert solution(456, 123) == 579, "Test 13 failed"
    assert solution(-456, 123) == -333, "Test 14 failed"
    
    print("All tests passed! ✓")

if __name__ == "__main__":
    test_solutions()