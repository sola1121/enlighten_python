def min_max(lst, start, end):
    assert len(lst) > 0
    if end - start <= 0:
        raise ValueError("outrange of start and end")
    if end - start == 1:
        min_value = min(lst[start], lst[end])
        max_value = max(lst[start], lst[end])
        return (min_value, max_value)
    min1, max1 = min_max(lst, start, (start+end)//2)
    min2, max2 = min_max(lst, (start+end)//2+1, end)
    return (min(min1, min2), max(max1, max2))

lst = [78, -6, 326, 9, 46, 451, -54, 52, 341, 415, -12, -97, -123, 65, 99]
print(min_max(lst, 0, len(lst)-1))
