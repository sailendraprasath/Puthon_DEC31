def is_valid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():  
            stack.append(char)
        elif char in bracket_map:  
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            return False  

    return not stack  

# Example usage:
s = input("Enter the string of brackets: ")
print("Valid" if is_valid(s) else "Invalid")
