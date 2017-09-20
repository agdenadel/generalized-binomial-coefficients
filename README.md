# generalized-binomial-coefficients

## Generalized binomial coefficients

The binomial coefficients can be computed using the formula

n choose k = n!/(k!(n-k)!) where n and k are positive integers.

Upon initial examination, it is not necessarily clear that this should necessarily produce an integer. The binomial coefficients are in fact always integers when k <= m.

With this in mind, it is reasonable to define generalized binomial coefficients for sequences of nonzero integers other than the natural numbers. if C = (c_1, c_2, c_3, ...) is a sequence of nonzero integers then we define the C-factorial by 

(n!)_C = c_m * c_m-1* ... * c_1 when n is not 0 and (0!)_C = 1.

We can use this generalization of the factorial to define generalized binomial coefficients associated with a sequence C, called the C-nomial coefficients. There is no guarentee for an arbitrary sequence that the C-nomial coefficients will be integers. 

Which sequences have integer C-nomial coefficients? What do these C-nomial  coefficients count? Are C-nomial coefficients of any combinatorial significance?

A Lemma from Knuth and Wilf states: For any sequence, C, of nonzero integers the C-nomial coefficients are all integers if gcd(C_i, C_j) = C_gcd(i,j) for all i,j > 0.

This property for a sequence, that is, if gcd(C_i, C_j) = C_gcd(i,J) is called strong divisibility.

Several families of functions have been proven to have integer C-nomial coefficients.

## OEIS

The OEIS is the [Online Encyclopedia of Integer Sequences](oeis.org). It contains hundreds of thousands of integer sequences. We can investigate these sequences to determine which of them may have integer C-nomial coefficients.