from typing import List


def solution(nums: List[int]) -> List[int]:
    left = [1]
    temp = 1

    for i in range(1, len(nums)):
        temp *= nums[i - 1]
        left.append(temp)

    n = len(nums)
    right = [0 for _ in range(n)]
    right[n - 1] = 1
    temp = 1
    for i in range(n - 2, -1, -1):
        temp *= nums[i + 1]
        right[i] = temp

    res = []
    for i in range(len(nums)):
        res.append(left[i] * right[i])

    return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    res = solution(nums)
    print("res = {}".format(res))
