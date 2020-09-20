def binarySearch(array, target) :
    left = 0
    right = len(array) - 1
    mid = (left + right)//2

    while left < right :
        if array[mid] == target :
            return mid
        elif array[mid] > target :
            right = mid - 1
        else :
            left = mid + 1
        mid = (left + right)//2

    if array[mid] == target :
        return mid
    else :
        return -1


if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8,9,10,11,12]
    print(binarySearch(array,12))
    print(binarySearch(array,1))
    print(binarySearch(array,3))
    print(binarySearch(array,14))