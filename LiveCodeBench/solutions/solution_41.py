def maximumSumQueries(nums1, nums2, queries):
    n = len(nums1)
    
    answer = []
    for xi, yi in queries:
        max_sum = -1
        for j in range(n):
            if nums1[j] >= xi and nums2[j] >= yi:
                max_sum = max(max_sum, nums1[j] + nums2[j])
        answer.append(max_sum)
    
    return answer