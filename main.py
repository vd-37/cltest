def maximize_sum_limited_flips(arr, k):
    neg_count = count_negatives(arr)

    if k >= neg_count:
        # Flip all negative numbers (simplified loop)
        for i in range(len(arr)):
            arr[i] = abs(arr[i])
        return sum(arr)
    else:
        # Sort and flip the k most negative numbers
        arr.sort()
        for i in range(k):
            arr[i] = -arr[i]
        return sum(arr)

def count_negatives(arr):
    count = 0
    for x in arr:
        if x < 0:
            count += 1
    return count
