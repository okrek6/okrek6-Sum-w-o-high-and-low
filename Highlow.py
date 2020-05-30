def sum_array(arr):

    if arr == None:
        return 0
    if len(arr) == 0 or 1:
        return 0
    else:
        x = max(arr)
        y = min(arr)

        arr.remove(x)
        arr.remove(y)

        return(sum(arr))


print(sum_array([1,2,3,4,4]))