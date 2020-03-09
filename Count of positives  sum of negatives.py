def count_positives_sum_negatives(arr):
    positive_count = 0
    negative_count = 0
    
    if len(arr) == 0:
        return arr
    for x in arr:
        if x > 0:
            positive_count += 1
        elif x < 0:
            negative_count +=x
    result = [positive_count, negative_count]
    return result