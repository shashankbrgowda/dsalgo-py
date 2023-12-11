from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for i in range(len(nums)):
        if (target - nums[i]) in hashmap:
            return [hashmap[target - nums[i]], i]
        hashmap[nums[i]] = i
    return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    # output: [0, 1]
    res = two_sum(nums, target)
    print("res = {}".format(res))
