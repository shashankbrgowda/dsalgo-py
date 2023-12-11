def valid_anagram(s: str, t: str):
    if len(s) != len(t):
        return False

    s_dict = {}
    t_dict = {}

    for i in range(len(s)):
        s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
        t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

    if s_dict == t_dict:
        print("They're anagram")
    else:
        print("They're not anagram")


# Check If 2 strings are valid anagram
if __name__ == '__main__':
    valid_anagram("anagram", "nagaram")
    valid_anagram("rat", "bat")
