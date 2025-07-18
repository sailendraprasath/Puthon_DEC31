def compute_ways(expression):
    # If the input is just a number (including negative), return it directly
    if expression.lstrip("-").isdigit():
        return [int(expression)]

    results = []

    i = 0
    while i < len(expression):
        ch = expression[i]

        # Support for //
        if ch == '/' and i + 1 < len(expression) and expression[i+1] == '/':
            op = '//'
            left_expr = expression[:i]
            right_expr = expression[i+2:]
            i += 1  # Skip extra '/'
        elif ch in "+-*/":
            op = ch
            left_expr = expression[:i]
            right_expr = expression[i+1:]
        else:
            i += 1
            continue

        # Recursively solve left and right parts
        left = compute_ways(left_expr)
        right = compute_ways(right_expr)

        for l in left:
            for r in right:
                if op == '+':
                    results.append(l + r)
                elif op == '-':
                    results.append(l - r)
                elif op == '*':
                    results.append(l * r)
                elif op == '/':
                    if r != 0:
                        results.append(l / r)
                elif op == '//':
                    if r != 0:
                        results.append(l // r)

        i += 1

    return results


# === Driver Code ===
expression = input("Enter expression (e.g., 2*3-4*5): ").replace(" ", "")
results = compute_ways(expression)
print("Possible results:", results)
