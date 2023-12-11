from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    strs_dict = {}

    for s in strs:
        sorted_str = ''.join(sorted(s))

        if sorted_str in strs_dict:
            strs_dict.get(sorted_str).append(s)
        else:
            strs_dict[sorted_str] = [s]

    return list(strs_dict.values())


# group all the anagrams in a list of list
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    res = group_anagrams(strs)
    print("res = {}".format(res))
