def contains_duplicate(nums):
    count = dict()

    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            if count[num] == 1:
                return True

    return False


def contains_duplicate_set(nums):
    count = set()

    for num in nums:
        if num not in count:
            count.add(num)
        else:
            return True

    return False
