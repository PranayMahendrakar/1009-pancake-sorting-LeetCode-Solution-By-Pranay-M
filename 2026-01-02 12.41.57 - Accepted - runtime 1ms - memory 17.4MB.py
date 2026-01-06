class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        
        for target in range(n, 0, -1):
            # Find position of target
            idx = arr.index(target)
            
            if idx == target - 1:
                # Already in place
                continue
            
            # Flip target to front if not already there
            if idx > 0:
                result.append(idx + 1)
                arr[:idx + 1] = arr[:idx + 1][::-1]
            
            # Flip target to its correct position
            result.append(target)
            arr[:target] = arr[:target][::-1]
        
        return result