#����ͧ
#2019-01-12 20:17:33

class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # ̰���㷨������������ƥ��
        people.sort()
        i = 0
        j = len(people) - 1
        count = 0
        
        while i <= j:
            if people[i] + people[j] <= limit: 
                i += 1
                
            count += 1
            j -= 1 
        return count