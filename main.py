def maximize_sum_limited_flips(arr, k):
    neg_count = count_negatives(arr)
    max_sum = 0
    
    if k >= neg_count:
        # Flip all negative numbers
        for i in range(len(arr)):
            arr[i] = abs(arr[i])
        
        # Handle remaining flips if k is greater than neg_count
        if k > neg_count:
            remaining_flips = k - neg_count
            if remaining_flips % 2 != 0:
                # If there are odd remaining flips, flip the smallest element to minimize impact
                arr.sort()  # Sort to get the smallest element at the front
                arr[0] = -arr[0]  # Flip the smallest element
        
        max_sum = sum(arr)
    else:
        # Sort and flip the k most negative numbers
        arr.sort()
        for i in range(k):
            arr[i] = -arr[i]
        max_sum = sum(arr)
    
    return max_sum

def count_negatives(arr):
    count = 0
    for x in arr:
        if x < 0:
            count += 1
    return count
