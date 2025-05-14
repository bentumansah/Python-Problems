# The approach is to traverse the array twice.
# In the first traversal, find the maximum element.
# In the second traversal, find the maximum element ignoring
# the one we found in the first traversal


## Python program to find the second largest element in an array



def getSecondLargest_double_traversal(arr):
    n = len(arr)
    
    largest = -1
    secondLargest = -1
    
    #first traverse for the largest element in the array
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
        
    # Finding the second largest element in the array
    for i in range(n):
        # update second largest if the current element is greater than 
        # the second largest element and less than the largest element
        if secondLargest < arr[i] < largest:
            secondLargest = arr[i]
        
    return secondLargest
    
    
if __name__ == "__main__":
    arr = [10, 10, 10]
    # arr = [12, 35, 1, 10, 34, 1]
    # arr = [10, 5, 10]
    print(getSecondLargest_double_traversal(arr))


# Time Complexity: O(2*n) = O(n),
# as we are traversing the array two times.

# Auxiliary space: O(1),
# as no extra space is required.
