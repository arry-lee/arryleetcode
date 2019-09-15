#两个数组的交集II
#2019-08-12 21:08:26


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # l = list(set(nums1)&set(nums2))
        # res = []
        # for i in l:
        #     c = min(nums1.count(i),nums2.count(i))
        #     res.extend([i]*c)
        # return res
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())

# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
    