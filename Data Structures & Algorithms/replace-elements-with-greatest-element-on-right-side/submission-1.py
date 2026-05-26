class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_from_right = -1 # Since last element -1
        
        # Iterate backwards through the array
        for i in range(len(arr) - 1, -1, -1):
            current_num = arr[i] # Store current element before overwrite it
            arr[i] = max_from_right # Replace curr element with max seen from right
            
            # Update the maximum for the next elements to the left
            if current_num > max_from_right:
                max_from_right = current_num

        return arr