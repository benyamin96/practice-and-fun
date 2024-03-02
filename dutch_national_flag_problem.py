def duch_flag_problem(arr, pivot=1):

    start = 0
    end = len(arr) - 1

    i = 0

    while i <= end:
        if arr[i] < pivot:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1
    return arr


numbers = [0, 0, 0, 1, 2, 2, 1, 0, 1]
print(duch_flag_problem(numbers))
