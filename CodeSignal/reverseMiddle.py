# Given a list of words, write a function that processes each word according 
# to the following rule: If the word starts and ends with a vowel (a, e, i, 
# o, u, case-insensitive), reverse all the middle characters (everything except 
# the first and last letter). Otherwise, leave the word unchanged. Return the 
# list of processed words.
# 
# Example
# Input: ["Apple", "banana", "arena", "oso", "cielo", "test"]
# Output: ["Alppe", "banana", "aerna", "oso", "cielo", "test"]
#
# I had this as part of the SWE TikTok Coding Assessment! (10/4/2025)

def solution(words):
    vowels = "aeiouAEIOU"
    result = []
    for word in words:
        if len(word) <= 1:
            result.append(word)
        elif word[0] in vowels and word[-1] in vowels:
            middle = word[1:-1]
            inverted_middle = middle[::-1]
            new_word = word[0] + inverted_middle + word[-1]
            result.append(new_word)
        else:
            result.append(word)
    return result

# --------------------------------
# Tests
def test_solution():
    # Example list from description (note: 'arena' becomes 'anera' with full middle reverse)
    assert solution(["Apple", "banana", "arena", "oso", "cielo", "test"]) == [
        "Alppe", "banana", "anera", "oso", "cielo", "test"
    ], "Test case 1 failed"

    # Single-letter vowel word (middle is empty)
    assert solution(["a"]) == ["a"], "Test case 2 failed"

    # Two-letter, both vowels (middle empty, unchanged)
    assert solution(["ae"]) == ["ae"], "Test case 3 failed"

    # Starts vowel, ends consonant -> unchanged
    assert solution(["Abc"]) == ["Abc"], "Test case 4 failed"

    # Starts consonant, ends vowel -> unchanged
    assert solution(["brau"]) == ["brau"], "Test case 5 failed"

    # Mixed case vowels: middle reversed
    assert solution(["Idea"]) == ["Ieda"], "Test case 6 failed"

    # Multiple words in one call, mixture of cases
    assert solution(["Umbrella", "echo", "Unit", "aeiou"]) == [
        "Ullerbma",  # middle 'mbrell' -> 'llerbm' => 'U' + 'llerbm' + 'a'
        "ehco",      # middle 'ch' -> 'hc' => 'e' + 'hc' + 'o'
        "Unit",      # starts vowel, ends consonant -> unchanged
        "aoieu"      # middle 'eio' -> 'oie' => 'a' + 'oie' + 'u'
    ], "Test case 7 failed"

    # Empty string should remain unchanged and not error
    assert solution([""]) == [""], "Test case 8 failed"
    # Mixed with empty string
    assert solution(["", "ae", "b"]) == ["", "ae", "b"], "Test case 9 failed"

    print("All tests passed!")

if __name__ == "__main__":
    test_solution()