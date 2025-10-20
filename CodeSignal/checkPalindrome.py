# Given the string, check if it is a palindrome.
# 
# For inputstring = "aabaa", the output should be solution (inputString) = true
# For inputstring = "abac" , the output should be solution (inputString) = false
# For inputstring = "a", the output should be solution (inputString) = true
# 
# Guaranteed constraints:
# A non-empty string consisting of lowercase characters.
# 1 ≤ inputstring. length ≤ 105

def solution(inputString):
    return inputString[::1] == inputString[::-1]



# --------------------------------
# Tests
def test_solution():
    # Test case 1: Examples from problem
    assert solution("aabaa") == True, "Test 1 failed"
    assert solution("abac") == False, "Test 2 failed"
    assert solution("a") == True, "Test 3 failed"
    
    # Test case 2: Simple palindromes
    assert solution("aba") == True, "Test 4 failed"
    assert solution("abba") == True, "Test 5 failed"
    assert solution("racecar") == True, "Test 6 failed"
    
    # Test case 3: Non-palindromes
    assert solution("abc") == False, "Test 7 failed"
    assert solution("hello") == False, "Test 8 failed"
    assert solution("world") == False, "Test 9 failed"
    
    # Test case 4: Single character (always palindrome)
    assert solution("z") == True, "Test 10 failed"
    
    # Test case 5: Two characters
    assert solution("aa") == True, "Test 11 failed"
    assert solution("ab") == False, "Test 12 failed"
    
    # Test case 6: All same characters
    assert solution("aaaa") == True, "Test 13 failed"
    assert solution("zzzzzz") == True, "Test 14 failed"
    
    # Test case 7: Longer palindromes
    assert solution("abcdefedcba") == True, "Test 15 failed"
    assert solution("abcdeedcba") == True, "Test 16 failed"
    
    # Test case 8: Almost palindromes (should be False)
    assert solution("aabba") == False, "Test 17 failed"
    assert solution("abcdefgfedcbaa") == False, "Test 18 failed"
    
    # Test case 9: Palindrome with repeated patterns
    assert solution("ababababa") == True, "Test 19 failed"
    
    # Test case 10: Even and odd length palindromes
    assert solution("noon") == True, "Test 20 failed"
    assert solution("level") == True, "Test 21 failed"
    assert solution("deed") == True, "Test 22 failed"
    assert solution("civic") == True, "Test 23 failed"
    
    print("All tests passed! ✓")

if __name__ == "__main__":
    test_solution()