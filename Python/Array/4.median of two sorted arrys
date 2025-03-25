'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_arry = nums1 + nums2
        merged_arry.sort()
        if len(merged_arry)%2 != 0:
            return merged_arry[len(merged_arry)//2]
        else:
            return float(merged_arry[len(merged_arry)//2] + merged_arry[len(merged_arry)//2 - 1]) / 2
'''



'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_arry = nums1 + nums2
        merged_arry.sort()

        n = len(merged_arry)
        if n%2 != 0:
            return merged_arry[n//2]
        else:
            return float(merged_arry[n//2] + merged_arry[n//2 - 1]) / 2
'''



class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A  # Always binary search the smaller array

        m, n = len(A), len(B)
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            maxLeftA = float('-inf') if i == 0 else A[i - 1]
            minRightA = float('inf') if i == m else A[i]
            maxLeftB = float('-inf') if j == 0 else B[j - 1]
            minRightB = float('inf') if j == n else B[j]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2.0
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                high = i - 1
            else:
                low = i + 1

