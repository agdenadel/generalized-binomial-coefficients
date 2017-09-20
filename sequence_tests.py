import unittest
from sequence import Sequence


def GetIntegers():
    return Sequence('integers', range(1,51))


class SequenceTests(unittest.TestCase):
    
    def test_len(self):
        sequence = GetIntegers()
        self.assertEqual(len(sequence), 50)
        
    def test_GetMember(self):
        sequence = GetIntegers()
        self.assertEqual(sequence.GetMember(5), 5)
        
    def test_HasZeroOrNegativeValues(self):
        sequence = GetIntegers()
        self.assertEqual(sequence.HasZeroOrNegativeValues(), False)
        
    def test_GetGeneralizedFactorial(self):
        sequence = GetIntegers()
        self.assertEqual(sequence.GetGeneralizedFactorial(5), 120)
    
    def test_GetCanceledGeneralizedFactorial(self):
        sequence = GetIntegers()
        self.assertEqual(sequence.GetCanceledGeneralizedFactorial(5, 3), 5*4)
    
    def test_GetGeneralizedBinomialCoefficient(self):
        sequence = GetIntegers()
        self.assertEqual(sequence.GetGeneralizedBinomialCoefficient(5,3),10)

        
        
if __name__ == '__main__':
    unittest.main()
