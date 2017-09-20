from __future__ import division
from random import randint
import os.path
import urllib
import gzip

from sequence import Sequence 

            
def has_empty_values(values):
    if len(values) == 0:
        return True
    for value in values:
        if value == '':
            return True
    return False
            
def parse_file(file):
    sequences = []
    with gzip.open(file, 'r') as file:
        empty_sequences = 0
        for line in file:
            if line[0] == '#':
                continue
            bits = line.strip().strip(',').split(',')
            name = bits[0]
            members = bits[1:]
            if has_empty_values(members):
                empty_sequences += 1
                continue
            members = map(int, members)
            sequence = Sequence(name, members)
            sequences.append(sequence)
    print "There were " + str(empty_sequences) + " empty_sequences"
    return sequences

# issue with overflow (need arbitrary precision)
def check_specific_values(sequence, n, k):
    return sequence.GetGeneralizedBinomialCoefficient(n,k).is_integer()

def check_random_values(sequence, num_values):
    for i in range(num_values):
        n = randint(1, 20)
        k = randint(1, n)
        if not check_specific_values(sequence, n, k):
            return False
    return True
    
def check_first_values(sequence):
    pairs = [(2,1),
             (3,1),
             (3,2),
             (4,1),
             (4,2),
             (4,3),
             (5,1),
             (5,2),
             (5,3),
             (5,4),
             (6,1),
             (6,2),
             (6,3),
             (6,4),
             (6,5),
             (7,1),
             (7,2),
             (7,3),
             (7,4),
             (7,5),
             (7,6)]
    for pair in pairs:
        n = pair[0]
        k = pair[1]
        if not check_specific_values(sequence, n, k):
            return False
    return True
    
def main():
    stripped_file = "stripped.gz"
    stripped_file_url = "http://oeis.org/" + stripped_file
    if not os.path.isfile(stripped_file):
        urllib.urlretrieve (stripped_file_url, "stripped.gz")
    sequences = parse_file(stripped_file)
    print "Parsed " + str(len(sequences)) + " sequences"
    
    int_count = 0
    candidates = []
    for sequence in sequences:
        try:
            #print "Generalized n choose k of sequence " + sequence.name + ": " + str(sequence.GetGeneralizedBinomialCoefficient(n,k))
            num_values = 20
            if not sequence.HasZeroOrNegativeValues():
                if check_first_values(sequence):
                    int_count += 1
                    candidates.append(sequence)
        except (ZeroDivisionError, ValueError):
            pass
            
    print 'There are ' + str(int_count) + ' integer generalized binomial coefficients out of ' + str(len(sequences)) + ' total sequences'
    print 'The percentage is ' + str(int_count / len(sequences))
    
    with  open('candidates.txt', 'w') as output:
        for candidate in candidates:
            output.write(candidate.name + "\n")
    
        
        
    
if __name__ == "__main__":
    main()