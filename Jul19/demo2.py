def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase

    lines = []
    for i in range(size):
        left = alphabet[size-1:i:-1]   # descending part
        center = alphabet[i]
        right = alphabet[i+1:size]     # ascending part
        row = '-'.join(left + center + right)
        lines.append(row.center(4 * size - 3, '-'))

    pattern = lines[::-1] + lines[1:]
    print('\n'.join(pattern))



n = int(input("Enter the size of the rangoli (1-26): "))
print_rangoli(n)
