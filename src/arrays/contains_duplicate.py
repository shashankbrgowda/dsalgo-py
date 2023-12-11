def contains_duplicate(arr):
    duplicate_set = set()

    for ele in arr:
        if ele in duplicate_set:
            print("Contains duplicate")
            break
        duplicate_set.add(ele)


# Check if there are duplicates in an array
if __name__ == '__main__':
    arr = [1, 2, 3, 1]
    contains_duplicate(arr)
