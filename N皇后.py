#N»Êºó
#2019-08-17 04:11:58

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
    
    def _solution_to_string(self):
        solutions = []
        for solution in self.solutions:
            sol = []
            for choice in solution:
                s = '.'*choice+'Q'+'.'*(len(solution)-choice-1)
                sol.append(s)
            solutions.append(sol)
        return solutions
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.solutions = []
        self._solution = []
        self.solution_size = n
        self.choices = range(n)
        
        self.dfs(0)
        
        
        return self._solution_to_string()
        