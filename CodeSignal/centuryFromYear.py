# Given a year, return the century it is in. The first century spans from the 
# year 1 up to and including the year 100, the second - from the year 101 up to 
# and including the year 200, etc.
# 
# For year = 1905, the output should be solution (year) = 20,
# For year = 1700, the output should be solution (year) = 17.
# 
# Guaranteed constraints:
# 1 ≤ year ≤ 2005 .

def solution(year):
    return (year - 1) // 100 + 1



# --------------------------------
# Tests
def test_solution():
    # Test case 1: Examples from problem
    assert solution(1905) == 20, "Test 1 failed"
    assert solution(1700) == 17, "Test 2 failed"
    
    # Test case 2: First year of first century
    assert solution(1) == 1, "Test 3 failed"
    
    # Test case 3: Last year of first century
    assert solution(100) == 1, "Test 4 failed"
    
    # Test case 4: First year of second century
    assert solution(101) == 2, "Test 5 failed"
    
    # Test case 5: Last year of second century
    assert solution(200) == 2, "Test 6 failed"
    
    # Test case 6: Years ending in 00 (boundary cases)
    assert solution(1000) == 10, "Test 7 failed"
    assert solution(2000) == 20, "Test 8 failed"
    
    # Test case 7: Years ending in 01 (first year of century)
    assert solution(1001) == 11, "Test 9 failed"
    assert solution(2001) == 21, "Test 10 failed"
    
    # Test case 8: Maximum constraint
    assert solution(2005) == 21, "Test 11 failed"
    
    # Test case 9: 20th century boundary
    assert solution(1900) == 19, "Test 12 failed"
    assert solution(1901) == 20, "Test 13 failed"
    assert solution(1999) == 20, "Test 14 failed"
    
    # Test case 10: 21st century
    assert solution(2004) == 21, "Test 15 failed"
    
    # Test case 11: Various centuries
    assert solution(300) == 3, "Test 16 failed"
    assert solution(500) == 5, "Test 17 failed"
    assert solution(750) == 8, "Test 18 failed"
    assert solution(1234) == 13, "Test 19 failed"
    
    print("All tests passed! ✓")

if __name__ == "__main__":
    test_solution()