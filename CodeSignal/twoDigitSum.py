# You are given a two-digit integer n. Return the sum of its digits.
# 
# For n = 29, the output should be solution(n) = 11.
# 
# Guaranteed constraints:
# 10 ≤ n ≤ 99.

def solution(n):
    sum = 0
    for dig in str(n):
        sum += int(dig)
    return sum

# One line solution
def solution2(n):
    return sum(int(dig) for dig in str(n))



# --------------------------------
# Tests
def test_solutions():
    # Test case 1: Example from problem
    assert solution(29) == 11, "Test 1 failed for solution()"
    assert solution2(29) == 11, "Test 1 failed for solution2()"
    
    # Test case 2: Minimum constraint (10)
    assert solution(10) == 1, "Test 2 failed for solution()"
    assert solution2(10) == 1, "Test 2 failed for solution2()"
    
    # Test case 3: Maximum constraint (99)
    assert solution(99) == 18, "Test 3 failed for solution()"
    assert solution2(99) == 18, "Test 3 failed for solution2()"
    
    # Test case 4: Same digits
    assert solution(55) == 10, "Test 4 failed for solution()"
    assert solution2(55) == 10, "Test 4 failed for solution2()"
    
    # Test case 5: Zero in ones place
    assert solution(20) == 2, "Test 5 failed for solution()"
    assert solution2(20) == 2, "Test 5 failed for solution2()"
    
    # Test case 6: Random number
    assert solution(47) == 11, "Test 6 failed for solution()"
    assert solution2(47) == 11, "Test 6 failed for solution2()"
    
    # Test case 7: Another random number
    assert solution(83) == 11, "Test 7 failed for solution()"
    assert solution2(83) == 11, "Test 7 failed for solution2()"
    
    print("All tests passed! ✓")

if __name__ == "__main__":
    test_solutions()