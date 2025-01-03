class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
         n = len(arr)
         d %= n  # Handle cases where d > n

        # Step 1: Reverse the first d elements
         self.reverse(arr, 0, d - 1)
        
        # Step 2: Reverse the remaining n-d elements
         self.reverse(arr, d, n - 1)
        
        # Step 3: Reverse the entire array
         self.reverse(arr, 0, n - 1)

    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
