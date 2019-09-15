#��ӽ�ԭ���K����
#2019-01-14 23:10:00

class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # # ���������㷨 NlogN
        # points.sort(key = lambda P:P[0]**2 + P[1]**2)
        # return points[:K]
        
        # ���ƿ��������㷨
        dist = lambda i: points[i][0]**2 + points[i][1]**2
        
        def work(i,j,K):
            if i >= j: return
            oi, oj = i, j
            """�±�ij֮������ʹ��K����С��ǰ�棬����ȫ����"""
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
        