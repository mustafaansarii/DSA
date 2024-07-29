def mostfrequent(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_freq = 0
    most_frequent_elem = None

    for num, freq in frequency.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent_elem = num

    return most_frequent_elem

if __name__ == '__main__':
    nums = [1,2,2,2,1,1,2,2,4,4,4,4,4,4,4,4,4]
    print(mostfrequent(nums))