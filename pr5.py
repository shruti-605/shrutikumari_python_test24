def findPeak(arr, n) :
    if (n == 1) :
      return 0
    if (arr[0] >= arr[1]) :
        return 0
    if (arr[n - 1] >= arr[n - 2]) :
        return n - 1
    for i in range(1, n - 1) :
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
            return i

arr = [ 1, 3, 20, 4, 1, 0 ]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))