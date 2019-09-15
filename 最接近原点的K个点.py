#最接近原点的K个点
#2019-01-14 23:10:00

class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # # 基本排序算法 NlogN
        # points.sort(key = lambda P:P[0]**2 + P[1]**2)
        # return points[:K]
        
        # 类似快速排序算法
        dist = lambda i: points[i][0]**2 + points[i][1]**2
        
        def work(i,j,K):
            if i >= j: return
            oi, oj = i, j
            """下标ij之间排序使得K个最小在前面，不用全排序"""
            p = dist(random.randint(i,j))
            while i < j:
                while i < j and dist(i) < p:
                    i += 1
                while i < j and dist(j) > p:
                    j -= 1
                points[i],points[j] = points[j],points[i]
            
            if i - oi +1 >= K:
                work(oi,i,K)
            else:
                work(i+1,oj,K-(i-oi+1))
                
        work(0,len(points)-1,K)
        return points[:K]
        