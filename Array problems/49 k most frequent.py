def kmostfrequent(nums, k):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    frequency_items = list(frequency.items())
    frequency_items.sort(key=lambda item: item[1], reverse=True)

    most_frequent = [item for item, _ in frequency_items[:k]]

    return most_frequent

if __name__ == '__main__':
    nums = [1, 2]
    a=kmostfrequent(nums, 2)
    print(a)