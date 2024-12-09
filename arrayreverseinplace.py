class Solution:

    def reverseArray(self, arr):
        # Get the size of the input list
        n = len(arr)

        # Loop through the first half of the list
        for i in range(n // 2):
            # Swap the current element with the corresponding element from the end of the list
            # Temporary variable to hold the current element
            t = arr[i]
            # Replace the current element with the element from the end
            arr[i] = arr[n - i - 1]
            # Replace the element from the end with the current element
            arr[n - i - 1] = t

