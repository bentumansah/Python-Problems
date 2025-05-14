# The idea is to keep track of the largest and second largest element while traversing the array.
# Initialize largest and secondLargest with -1. Now, for any index i,
# If arr[i] > largest, update secondLargest with largest and largest with arr[i].
# Else If arr[i] < largest and arr[i] > secondLargest, update secondLargest with arr[i].


# Python program to find the second largest element in the array
# using one traversal

# function to find the second largest element in the array
def getSecondLargest_single_traversal(arr):
    n = len(arr)

    largest = -1
    secondLargest = -1

    # finding the second largest element
    for i in range(n):

        # If arr[i] > largest, update second largest with
        # largest and largest with arr[i]
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
      
        # If arr[i] < largest and arr[i] > second largest, 
        # update second largest with arr[i]
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]

    return secondLargest

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest_single_traversal(arr))
    
    
# Time Complexity: O(n),
# as we are traversing the array only once.
# Auxiliary space: O(1),
# as no extra space is required.
# The code is a Python program that finds the second largest element in an array using a single traversal.
# It initializes two variables, largest and secondLargest, to -1.
# It then iterates through the array, updating these variables based on the conditions specified.
# The function returns the second largest element found in the array.