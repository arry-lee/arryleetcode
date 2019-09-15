#È«ÅÅÁĞ
#2019-04-02 15:33:49


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = [0] * len(nums)
        res = []

        def dfs(path):
            if len(path) == len(nums) and path not in res:
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0

        dfs([])
        return res


        