# # The idea is to sort the array in non-descending order.
# Now, we know the largest element will be at index (n - 1).
# So, starting from index (n - 2), traverse the remaining array in reverse order.
# As soon as we encounter an element which is not equal to the largest element,
# return it as the second largest element in the array.
# If all the elements are equal to the largest element, return -1.


#Python program to find the second largest element in an array using sorting
secondLargest = 0


def getSecondLargest_sorted(arr):
    n = len(arr)
    
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Start from the second last element, as last element is the largest element
    for i in range(n-2, -1, -1):
        
        # return the first element which is not equal to the largest element
        if arr[i] != arr[n-1]:
            secondLargest = arr[i]
            return secondLargest
        
        # if no second largest element was found, return -1
        return -1
    
    
if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    # arr = [10, 5, 10]
    # arr = [10, 10, 10]
    print(getSecondLargest_sorted(arr))


## Time Complexity: O(n*log(n)),
# as sorting the array takes O(n*log(n)) time
# and traversing the array can take O(n) time in the worst case
# so total time complexity = (n*log(n) + n) = O(n*log(n))
# Auxiliary space: O(1), as no extra space is required.