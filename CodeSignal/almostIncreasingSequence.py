# Given a sequence of integers as an array, determine whether it is possible to 
# obtain a strictly increasing sequence by removing no more than one element 
# from the array.
# 
# Note: sequence a0, a1, ... an is considered to be a strictly increasing 
# if a0 < a1 < ... < an.
# Sequence containing only one element is also considered to be strictly increasing.
# 
# For sequence = [1, 3, 2, 1], the output should be solution (sequence) = false.
# There is no one element in this array that can be removed in order to get a strictly 
# increasing sequence.
# 
# For sequence = [1, 3, 2], the output should be solution (sequence) = true.
# You can remove 3 from the array to get the strictly increasing sequence [1, 2].
# Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

def solution(sequence):
    removed = False
    prevprev = float('-inf')
    prev = sequence[0]
    for i in range(1, len(sequence)):
        cur = sequence[i]
        if prev >= cur:
            if removed:
                return False
            removed = True
            if prevprev < cur:
                prev = cur
            else:
                pass
        else:
            prevprev = prev
            prev = cur
    return True



# --------------------------------
# Tests
def test_solution():
    # Test case 1: Examples from problem
    assert solution([1, 3, 2, 1]) == False, "Example 1 failed"
    assert solution([1, 3, 2]) == True, "Example 2 failed"

    # Test case 2: Already strictly increasing
    assert solution([1, 2, 3, 4, 5]) == True, "Already increasing failed"

    # Test case 3: Single and two elements
    assert solution([5]) == True, "Single element failed"
    assert solution([1, 1]) == True, "Two equal elements should be fixable by removing one"
    assert solution([2, 1]) == True, "Two elements decreasing can be fixed by removing one"

    # Test case 4: Duplicate in the middle (remove one duplicate)
    assert solution([1, 2, 2, 3]) == True, "Duplicate middle failed"

    # Test case 5: Removal at the start
    assert solution([10, 1, 2, 3, 4]) == True, "Removal at start failed"

    # Test case 6: Removal at the end
    assert solution([1, 2, 3, 4, 3]) == True, "Removal at end failed"

    # Test case 7: Choose to remove previous vs current
    assert solution([1, 4, 2, 3]) == True, "Remove previous element scenario failed"
    assert solution([1, 2, 5, 3, 5]) == True, "Remove current element scenario failed"

    # Test case 8: Multiple decreases cannot be fixed by one removal
    assert solution([1, 2, 3, 4, 3, 2, 5]) == False, "Multiple decreases should fail"
    assert solution([1, 2, 3, 1, 2, 3]) == False, "Two dips should fail"

    # Test case 9: Classic tricky cases
    assert solution([3, 5, 67, 98, 3]) == True, "Classic case remove last failed"
    assert solution([1, 2, 5, 3, 4]) == True, "Remove a high peak failed"
    assert solution([1, 2, 3, 4, 99, 5, 6]) == True, "Remove large outlier failed"

    # Test case 10: Negative numbers and zeros
    assert solution([-1, 0, 1, 1]) == True, "Handle zero and duplicate at end failed"
    assert solution([-3, -2, -1, -2]) == True, "Remove last negative dip failed"

    print("All tests passed! ✓")

if __name__ == "__main__":
    test_solution()