def longest_unique_substring(s):
    seen = set()
    left = 0
    max_len = 0
    start_idx = 0  

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])

        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_idx = left  

    longest_substring = s[start_idx:start_idx + max_len]
    return max_len, longest_substring


user_input = input("Enter a string: ")


length, substring = longest_unique_substring(user_input)


print("Length of longest substring without repeating characters:", length)
print("Longest substring:", substring)
