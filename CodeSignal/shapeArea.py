# Below we will define an n -interesting polygon. Your task is to find the area 
# of a polygon for a given n.
#
# A 1-interesting polygon is just a square with a side of length 1. An n-interesting 
# polygon is obtained by taking the n-1-interesting polygon and appending 1-interesting 
# polygons to its rim, side by side.
#
# For n = 2, the output should be solution (n) = 5;
# For n = 3, the output should be solution (n) = 13.
#
# Guaranteed constraints:
# 1 ≤ n ≤ 10**4

def solution(n):
    return n * n + (n - 1) * (n - 1)



# --------------------------------
# Tests
def test_solution():
    # Base case: 1-interesting polygon (just a square)
    assert solution(1) == 1, "Test case 1 failed"
    
    # Example from problem description
    assert solution(2) == 5, "Test case 2 failed"
    
    # Example from problem description
    assert solution(3) == 13, "Test case 3 failed"
    
    # Testing pattern continuation
    assert solution(4) == 25, "Test case 4 failed"
    
    assert solution(5) == 41, "Test case 5 failed"
    
    assert solution(6) == 61, "Test case 6 failed"
    
    # Larger values
    assert solution(10) == 181, "Test case 7 failed"
    
    assert solution(100) == 19801, "Test case 8 failed"
    
    # Edge case: maximum constraint
    assert solution(10000) == 199980001, "Test case 9 failed"
    
    # Verify the formula: n² + (n-1)²
    # For n=7: 7² + 6² = 49 + 36 = 85
    assert solution(7) == 85, "Test case 10 failed"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_solution()