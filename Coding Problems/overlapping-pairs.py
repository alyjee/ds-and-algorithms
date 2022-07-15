# url: https://www.educative.io/m/merge-overlapping-intervals
# Problem Statement
# You are given an array (list) of interval pairs as input where each interval has a start and end timestamp.
# The input array is sorted by starting timestamps. You are required to merge overlapping intervals and return a new output array.

# Consider the input array below. Intervals (1, 5), (3, 7), (4, 6), (6, 8) are overlapping so they should be merged to one big interval (1, 8).
# Similarly, intervals (10, 12) and (12, 15) are also overlapping and should be merged to (10, 15).

def solution(pairs):
    
    if len(pairs) <= 1:
        return pairs
    
    res = []
    i = 0
    while i < len(pairs):
        A = pairs[i]
        
        j = i + 1
        while j < len(pairs):
            B = pairs[j]
            if B[0] > A[1]:
                break
            A = (A[0], max(A[1], B[1]))
            j += 1
        
        res.append(A)
        i = j
    
    return res

pairs = [(1,5)]
print(solution(pairs))

pairs = [(1,5), (7, 13)]
print(solution(pairs))

pairs = [(1,5), (3,7), (4,6), (6,8)]
print(solution(pairs))

pairs = [(1,5), (3,7), (4,6), (6,8), (10, 10), (11, 11)]
print(solution(pairs))