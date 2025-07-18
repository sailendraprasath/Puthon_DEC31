user_numbers = input("Enter your numbers: ")
numbers = [int(ch) for ch in user_numbers]
new_numbers = numbers.copy()
print(numbers)
while any(new_numbers):
    final_result = []
    for val in new_numbers:
        srt_digit = new_numbers[0]
        if val < srt_digit:
            srt_digit = val
    for get_val in new_numbers:
        new_val = get_val - srt_digit
        final_result.append(new_val)
    for i in final_result:
        if i == 0:
            final_result.remove(i)
    if final_result == []:
        None
    else:
        print(final_result)
    new_numbers = final_result

