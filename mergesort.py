def merge(arr, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    left_arr = [0] * n1
    right_arr = [0] * n2

    for i in range(n1):
        left_arr[i] = arr[left + i]
    for j in range(n2):
        right_arr[j] = arr[middle + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        merge(arr, left, middle, right)

if __name__ == "__main__":
    arr = [99,121,0,101,392,4584]
    print("Original array is:", arr)

    merge_sort(arr, 0, len(arr) - 1)

    print("Sorted array is:", arr)
