

# CMPS 2200 Assignment 1

**Name:**_____________Maddie Bonanno____________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
.  
.  Yes, it is in O(2^n) beause 2^n+1 is 2 * 2^n
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
.  
.  No it is not in O(2^n) because there is no constant > 0 that satisfies condition f(n) <= g(n) for all values of n
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  
.  No because the power function will eventually surpass the logarithmic function, meaning it is not in O(log^2n)
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  Yes because there exists constants s.t. f(n) >= g(n) for all values of n,
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  No, as the logarithmic function will not dominate the sqrt for constants > 0 for all values of n
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  
  Yes, as this is the opposite of 1e. Sqrt(n) will asymptotically dominate the log funct, making this statement true

2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  This function determines the fibonacci number at index x. It first checks base cases of 0 and 1, alloting values for n0 and n1 (since we must use x-2 in the recursive step, the lowest value of x that we can solve for is 2; the base cases fill in our missing info). Following this, the function recursively determines the next element in the sequence by obtaining the sum of the two numbers preceding it. This allows us to determine what any fibonacci number is at desired index x. 
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  
.  The work and span of this implementation are O(n) --> there is no parallelism
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  
.  The work of this algorithm is O(n), while the span would be O(log2n)
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

. If it was parallelized in this way, the work would be O(log2n) and the span would be O(log2n)
.  
.  
.  
.  
.  
.  
.  

