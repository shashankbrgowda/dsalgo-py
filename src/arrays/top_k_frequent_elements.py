from typing import List


def k_freq_eles(nums: List[int], k: int) -> List[int]:
    nums_dict = {}

    for num in nums:
        nums_dict[num] = 1 + nums_dict.get(num, 0)

    res = []
    sorted_list = sorted(nums_dict.items(), key=lambda item: item[1], reverse=True)

    for i in range(k):
        res.append(sorted_list[i][0])

    return res


if __name__ == '__main__':
    """
        Top k frquent elements in a array
        
        O/P: 1 and 2
        
        1 -> 3
        2 -> 2
    """
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    res = k_freq_eles(nums, k)
    print("res = {}".format(res))
