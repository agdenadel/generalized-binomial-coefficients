from __future__ import division


class Sequence():
    def __init__(self, name, members):
        self.name = name
        self.members = members
        
    def __str__(self):
        ret = self.name
        for member in self.members:
            ret = ret + str(member)
        return ret
        
    def __len__(self):
        return len(self.members)
        
    def GetMember(self, n):
        self._checkBounds(n)
        return self.members[n - 1]
        
    def HasZeroOrNegativeValues(self):
        for member in self.members:
            if member <= 0:
                return True
        return False
        
    # issue with overflow (need arbitrary precision)
    # we could also compute this in a smarter fashion since these numbers get so huge
    def GetGeneralizedFactorial(self, n):
        product = 1
        while n - 1 >= 0:
            product *= self.GetMember(n)
            n -= 1
        return product
        
    def GetCanceledGeneralizedFactorial(self, n, k):
        product = 1
        while n - 1 > k - 1:
            product *= self.GetMember(n)
            n -= 1
        return product
        
    # issue with overflow (need arbitrary precision)
    def GetGeneralizedBinomialCoefficient(self, n, k):
        self._checkVals(n, k)
        
        # n!/(k! * (n-k)!) = n * .. * n - k + 1 / (n - k)!
        return self.GetCanceledGeneralizedFactorial(n, k) / self.GetGeneralizedFactorial(n - k)
           
    def _checkVals(self, n, k):
        if k > n:
            raise ValueError('Coefficients are not defined for k > n')
                   
    def _checkBounds(self, n):
        if n >= len(self.members):
            raise ValueError('Coefficients cannot be computed for n greater than the number of members currently available')