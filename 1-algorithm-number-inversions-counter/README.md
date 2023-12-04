# Alrorithm for number of inversions in a list
------------------------

This exercice follows the idea of improvement of algorithm thanks to the **Divide to Conquer** paradigm. 

This paradigm as well as the solution of improvement of the **Brute Force** solution is developped in the following videos by **Tim Roughgarden**:
- [O(Nlog(N)) Algorithm for Counting Inversions (Part1)](https://www.youtube.com/watch?v=7_AJfusC6UQ&list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V&index=15&t=0s)
- [O(Nlog(N)) Algorithm for Counting Inversions (Part2)](https://www.youtube.com/watch?v=I6ygiW8xN7Y&list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V&index=16&t=0s)

## Introduciton to the problem

The problem consists of counting the number of inversed pairs in a given list.<br>

***Example:*** 
For L = [1 ,3 , 6, 2, 4, 3]
the algorithm must return **5** <br>
for the pairs: 
(3, 2) <br>
(6, 2) <br>
(6, 4) <br>
(6, 3) <br>
(4, 3) <br>

## `Brute force` approach

The `brute force` method consits of read through the list from left to right...
Checkout the notebook [](https://github.com/lohiermichael/algorithm-number-inversions-counter/blob/master/20190830-Counting_Inversions.ipynb) to take a closer look to the code.

## `Divide to conquer` approach

The `divide to conquer` method consists of a counting the number of inverisons together with merge-sorting the list.
Checkout the notebook [](https://github.com/lohiermichael/algorithm-number-inversions-counter/blob/master/20190830-Counting_Inversions.ipynb) to take a closer look to the code.
