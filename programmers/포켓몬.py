def solution(nums):
    s = set(nums)
    return len(nums) // 2 if len(s) > len(nums) // 2 else len(s)

print(solution([3, 1, 2, 3]))