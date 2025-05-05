def maximize_sum_limited_flips(arr, k):
    # Step 1: Count negative numbers
    neg_count = sum(1 for x in arr if x < 0)

    if k >= neg_count:
        # Step 2: Flip all negatives
        arr = [abs(x) for x in arr]
        return sum(arr)
    else:
        # Step 3: Sort by value (ascending), flip first k elements
        arr.sort()
        for i in range(k):
            arr[i] = -arr[i]
        return sum(arr)
