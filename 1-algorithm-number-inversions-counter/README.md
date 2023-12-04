# Algorithm for number of inversions in a list

This exercise follows the idea of improvement of algorithm thanks to the
**Divide to Conquer** paradigm.

This paradigm as well as the solution of improvement of the **Brute Force**
solution is developed in the following videos by **Tim Roughgarden**:

- [O(Nlog(N)) Algorithm for Counting Inversions (Part1)](https://www.youtube.com/watch?v=7_AJfusC6UQ&list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V&index=15&t=0s)
- [O(Nlog(N)) Algorithm for Counting Inversions (Part2)](https://www.youtube.com/watch?v=I6ygiW8xN7Y&list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V&index=16&t=0s)

## Introduction to the problem

The problem consists of counting the number of inverted pairs in a given list.

***Example:***
For L = [1 ,3 , 6, 2, 4, 3]
the algorithm must return **5**
for the pairs:

- (3, 2)
- (6, 2)
- (6, 4)
- (6, 3)
- (4, 3)

## `Brute force` approach

The `brute force` method consists of read through the list from left to right...
Checkout the notebook [](https://github.com/lohiermichael/algorithm-number-inversions-counter/blob/master/20190830-Counting_Inversions.ipynb) to take a closer look to the code.

## `Divide to conquer` approach

The `divide to conquer` method consists of a counting the number of inversions together with merge-sorting the list.
Checkout the notebook [](https://github.com/lohiermichael/algorithm-number-inversions-counter/blob/master/20190830-Counting_Inversions.ipynb) to take a closer look to the code.
