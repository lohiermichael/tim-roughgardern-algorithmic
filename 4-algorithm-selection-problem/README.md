# algorithm-selection-problem

This repository will gather different algorithms for the **selection problem** in a list. It will highlight the performance of the **Divide to Conquer** paradigm in the context of this problem.

## Introduction to the problem

This problem often follows the problem of sorting list mainly because one of its solutions: **Randomized Selection** hinges on the same method as the one of **Quick Sort**.

### Input

Given:
* a list of n integers: `L = [a1, ..., an]`
* i and integer of [1, n] 

### Goal 

We want to return the value of the ith order statistic (i.e. ith smallest element of L)

***Example***: One specific case of this problem is finding the **median**:
- the (n+1)/2th element in n i odd
- the n/2th element if n is even

## Solutions

### 1. Reduction to sorting

A simple approach is to sort the array and take the ith element of the list. The complexity of this algorithm is that of the sorting algorithm.

If we take **merge_sort** as the sorting algorithm, the complexity will be in **O(nln(n))** in average.

However, as we can't sort a list any faster than in **O(nln(n))**, this complexity is an lower bound of the complexity we can achieve. See this [video](https://www.youtube.com/watch?v=aFveIyII5D4&list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V&index=39) for more explanation.

### 2. Randomized selection

This method is based on the same principal as the **quick sort** algorithm for lists. This method is then based on the **divide to conquer** paradigm.

### DIVIDE

We call randomized_selection(L, i). <br>
We choose a **random** element of the list.
We partition the other element of the list around this pivot, i.e., by scanning through the other elements of the list:
* if L[i] <= pivot it goes on the left: **L_left**
* if L[i] > pivot it goes on the right: **L_right**

***Note:* The order statistic of the pivot i_pivot in the resulting list is actually its index.**

### CONQUER

* If i (the order statistics that we look for) <= i_pivot: we call recursively `randomized_selection(L_left, i)`
* If i > i_pivot: we call recursively `randomized_selection(L_right, i_pivot-i)`

### 3. Deterministic selection

This method is also based  ob the same principal as the **quick sort** algorithm for lists, with the **divide to conquer paradigm**. The difference is the strategy we have to choose the pivot at each iteration. We use for that the method of **median of medians**.

### DIVIDE

* **Choice of the pivot**

1. We call `choose_pivot(L)`
2. We break L into sub-lists of at most 5 elements
3. We sort each small list
4. We keep the median of each small list and build a list of length n/5 of "middle elements" out of it.
5. We recursively call  `choose_pivot(C)

choose_pivot(L) will return the **pivot**
As soon as we get the pivot,  we use the same strategy as for the **randomized selection**.

* **Partition L around pivot**

    - if L[i] <= pivot it goes on the left: **L_left**
    - if L[i] > pivot it goes on the right: **L_right**

### CONQUER

* If i (the order statistics that we look for) <= i_pivot: we call recursively `randomized_selection(L_left, i)`
* If i > i_pivot: we call recursively `randomized_selection(L_right, i_pivot-i)`







