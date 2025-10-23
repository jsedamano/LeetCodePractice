# You are given a string S.
# Your task is to find the first occurrence of an alphanumeric character in S
# (read from left to right) that has consecutive repetitions.
# 
# Print the first occurrence of the repeating character. If there are no 
# repeating characters, print -1.
# 
# Sample Input: ..12345678910111213141516171820212223
# Sample Output: 1
# .. is the first repeating character, but it is not alphanumeric.
# 1 is the first (from left to right) alphanumeric repeating character of the 
# string in the substring 111.
# 
# Constraints
# 0 < len(S) < 100

def solution(s):
    for char in range(len(s) - 1):
        if s[char].isalnum() and s[char] == s[char + 1]:
            return s[char]
    return "-1"

import re
def solution2(s):
    pattern = r"([A-Za-z0-9])\1"
    m = re.search(pattern, s)
    if m:
        return m.group(1)
    else:
        return "-1"

# --------------------------------
# Tests
def test_solution():
    # Test case 1: Sample from problem
    assert solution("..12345678910111213141516171820212223") == "1", "Sample test failed"
    assert solution2("..12345678910111213141516171820212223") == "1", "Sample test failed"
    
    # Test case 2: No repeating alphanumeric characters
    assert solution("abcdef") == "-1", "No repetition failed"
    assert solution2("abcdef") == "-1", "No repetition failed"
    assert solution("a.b.c.d") == "-1", "No alphanumeric repetition with symbols failed"
    assert solution2("a.b.c.d") == "-1", "No alphanumeric repetition with symbols failed"
    
    # Test case 3: First character repeats
    assert solution("aabcd") == "a", "First character repeat failed"
    assert solution2("aabcd") == "a", "First character repeat failed"
    assert solution("11abc") == "1", "First digit repeat failed"
    assert solution2("11abc") == "1", "First digit repeat failed"
    
    # Test case 4: Only non-alphanumeric repeats
    assert solution("...abc") == "-1", "Only symbols repeat failed"
    assert solution2("...abc") == "-1", "Only symbols repeat failed"
    assert solution("!!##$$abc") == "-1", "Multiple symbol repeats failed"
    assert solution2("!!##$$abc") == "-1", "Multiple symbol repeats failed"
    
    # Test case 5: Multiple repeating characters (return first)
    assert solution("a.bb.cc") == "b", "Multiple repeats return first failed"
    assert solution2("a.bb.cc") == "b", "Multiple repeats return first failed"
    assert solution("123.44.55") == "4", "Multiple digit repeats failed"
    assert solution2("123.44.55") == "4", "Multiple digit repeats failed"
    
    # Test case 6: Case sensitivity
    assert solution("aAbbc") == "b", "Case sensitivity failed"
    assert solution2("aAbbc") == "b", "Case sensitivity failed"
    
    # Test case 7: Numbers and letters mixed
    assert solution("a1b2c33d") == "3", "Mixed alphanumeric failed"
    assert solution2("a1b2c33d") == "3", "Mixed alphanumeric failed"
    
    # Test case 8: Repetition at end
    assert solution("abcdee") == "e", "Repetition at end failed"
    assert solution2("abcdee") == "e", "Repetition at end failed"
    
    # Test case 9: Three or more consecutive
    assert solution("abcccde") == "c", "Three consecutive failed"
    assert solution2("abcccde") == "c", "Three consecutive failed"
    assert solution("1222234") == "2", "Four consecutive failed"
    assert solution2("1222234") == "2", "Four consecutive failed"
    
    # Test case 10: Empty-ish and single character edge cases
    assert solution("a") == "-1", "Single character failed"
    assert solution2("a") == "-1", "Single character failed"
    assert solution("ab") == "-1", "Two different characters failed"
    assert solution2("ab") == "-1", "Two different characters failed"
    assert solution("aa") == "a", "Two same characters failed"
    assert solution2("aa") == "a", "Two same characters failed"
    
    # Test case 11: Special characters between repeats (should not match)
    assert solution("a.a") == "-1", "Non-consecutive same chars failed"
    assert solution2("a.a") == "-1", "Non-consecutive same chars failed"
    
    print("All tests passed! ✓")

if __name__ == "__main__":
    test_solution()