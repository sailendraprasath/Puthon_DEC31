def longest_palindrome(s):
    max_len = 0
    result = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if substr == substr[::-1] and len(substr) > max_len:
                result = substr
                max_len = len(substr)
    return result


s = input("Enter a string: ")
print("Longest Palindromic Substring:", longest_palindrome(s))
