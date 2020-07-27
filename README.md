# Project Euler

This folder contains solutions to problems from Hacker Rank's Project Euler competition. Hacker Rank problems are usually a generalization of the corresponding problem on Project Euler with more strict time and memory constraints, therefore a bit more difficult. Solutions to actual Project Euler problem can be obtained by runnning the program with right input or, not as often, by modifying the given solution (when needed these modifications are trivial). 

Bellow are problem statements as well as general descriptions of solutions. 

-------------------------------------------------------------------------------------------------------------------------

## Project Euler #1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.

First line denotes number of test cases. Next T lines contain integers N. 

1 <= T <= 10^5
1 <= N <= 10^9

For each test case print the sum of multiples of 3 or 5 below N. 

## Solution 

It is possible to solve this problem in O(1) if we note that we are looking for sums of two arithmetic progressions with d = 3 and d = 5, since there is a formula for such sum. Note that both of these sums contain a sum for arithmetic progression with d = 15, so this one will be counted twice. This is why we need to subract a sum of this progression from the sum of these two. 

------------------------------------------------------------------------------------------------------------------------------


