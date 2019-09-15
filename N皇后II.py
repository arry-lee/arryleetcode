#N»ÊºóII
#2019-08-17 04:15:19

class Solution:
    
    def conflict(self,k):
        for i in range(k):
            if self._solution[i] == self._solution[k] or abs(self._solution[k]-self._solution[i])== k-i:
                return True
        return False
    
    def dfs(self,k):
        if k>= self.solution_size:
            self.solutions.append(self._solution.copy())
        else:
            for choice in self.choices:
                self._solution.append(choice)
                if not self.conflict(k):
                    self.dfs(k+1)
                self._solution.pop()
    

    def totalNQueens(self, n: int) -> int:
        self.solutions = []
        self._solution = []
        self.solution_size = n
        self.choices = range(n)
        
        self.dfs(0)
        
        return len(self.solutions)
        


        