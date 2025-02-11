def findMedianSortedArrays(nums1, nums2):
    merged_list = sorted(nums1 + nums2)
    n = len(merged_list)
    if n % 2 == 0:
        mid1 = merged_list[n//2 -1]
        mid2 = merged_list[n//2]
        median = (mid1 + mid2) /2
    else:
        median = merged_list[n//2]
    return median
    

nums1 = [1,3]
nums2 = [2]
result = findMedianSortedArrays(nums1, nums2)
print(result)