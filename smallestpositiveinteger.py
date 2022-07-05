"""
Write a function:
    def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:
        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
[1,3,6,4,1,2]
[1,2,3]
[-1,-3]
[]
"""

def solution(A):
    if A == []:
        return 1
    A.sort()
    seen_dict = {element: 1 for element in A}
    running_num = 1
    for value in A:
        if running_num != value and running_num not in seen_dict:
            return running_num
        else:
            running_num += 1
    return running_num

print(solution([1,3,6,4,1,2]))
print(solution([1,2,3]))
print(solution([-1,-3]))
print(solution([]))