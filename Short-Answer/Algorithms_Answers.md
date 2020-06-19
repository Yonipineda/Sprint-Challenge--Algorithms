#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) 

It is taking a step of n^2 until it gets to n^3.

In the first loop, a will get to n^2, after the second loop it will be 2n^2. Since the loop is only n in length, with each increment, its executing 1 operation. 

For example: 

        1 + 1 + 1 + ... + 1  <---- n times  

        = n 

        = O(n) 


b) O(nlog(n)) 

This time-space complexity algorithm increases at a multiple of a constant. 

Frankly, this algorithm broke my mind a little. But I will attempt to justify my rationale as well as I can. 

The summing steps is a single operation. Meaning, for each loop of i, it computes the same number of operations within the inner j loop. And, for each inner loop of j, it is incrementing the sum by 1, then 2 and so on, until it is incremented by n. Essentially, log2(n) Operationd occur, such that if n = 64, j takes:  

                                    1 -> 2 -> 4 -> 8 -> 16 -> 32 -> 64

Each arrow represents j changing. This occurs n times for parent loop i, which means n
operations of log2(n) or nlogn 



c) O(n) 

To quickly summerize it, in total it returns 2n operations, which is also O(n).

That is because for each n, the function is calling itself until it reaches 0. A final value is returned, which eventually returns 0, and it follows the series of returns back from 0 to n
. 

## Exercise II

Assuming this is a absurdly robust egg, we can consider it as an object with an unknown breaking point. 

First, drop the egg from the middle floor, if it breaks we can move halfway to the bottom. If it does not break, move halfway to the top. We can iterate with this pattern until we have narrowed down its breaking point, eventually pinpointing the floor where it does not break. 

This a O(log(n)) time complexity.  

Psuedo code: 

```
def search_breaking_point(bottom, top):
    middle = n // 2
    if egg_breaks(n):
        top = n 
        search_breaking_point(bottom, top)
    else:
        if top == bottom:
            return top 
        else: 
            bottom = middle 
            search_breaking_point(bottom, top)

```


