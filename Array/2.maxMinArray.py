"""
Maximum and minimum of an array using minimum number of comparisons
https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
"""


def maxMin(low, high, array):
    arr_max = array[low]
    arr_min = array[low]
    print( f"Min : {arr_min}  Max : {arr_max}" )
    if low == high:
        print( f"Min : {arr_min}  Max : {arr_max}" )
        return arr_max, arr_min
    elif low + 1 == high:
        if array[low] > array[high]:
            arr_max = array[low]
            arr_min = array[high]
        else:
            arr_max = array[high]
            arr_min = array[low]
        print( f"Min : {arr_min}  Max : {arr_max}" )
        return arr_max, arr_min
    else:
        mid = (low + high) // 2
        arr_MAX1, arr_min1 = maxMin( low, mid, array )
        print( f"Min1 : {arr_min1}  Max1 : {arr_MAX1}" )
        arr_max2, arr_MIN = maxMin( mid + 1, high, array )
        print( f"Min2 : {arr_MIN}  Max2 : {arr_max2}" )
        return max( arr_MAX1, arr_max2 ), min( arr_min1, arr_MIN )


# Driver code
arr = [1000, 11, 445, 1, 330, 3000]
high = len( arr ) - 1
low = 0
arr_max1, arr_min2 = maxMin( low, high, arr )
print( 'Minimum element is ', arr_min2 )
print( 'Maximum element is ', arr_max1 )
