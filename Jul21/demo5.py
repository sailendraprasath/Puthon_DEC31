def longest_common_suffix(strs):
    if not strs:
        return ""


    reversed_strs = [s[::-1] for s in strs]


    prefix = reversed_strs[0]
    for word in reversed_strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""


    return prefix[::-1]


strs = input("Enter words separated by space: ").split()
print("Longest Common Suffix:", longest_common_suffix(strs))
