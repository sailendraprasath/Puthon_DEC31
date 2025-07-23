from collections import Counter

def longest_suffix_with_repeats(nums):
    freq = Counter(nums)
    # Start from the end and find the longest suffix where all elements have freq > 1
    for i in range(len(nums)):
        suffix = nums[i:]
        if all(freq[x] > 1 for x in suffix):
            return suffix
    return []

if __name__ == "__main__":
    input_list = [2,2,4,4,5,5,7,5,7]
    output = longest_suffix_with_repeats(input_list)
    print("Input:", input_list)
    print("Output:", output)
