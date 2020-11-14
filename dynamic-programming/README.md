## Dynamic programming

Technique for computing recursive algorithm with highly overlapping subproblems by only solving each subproblems by only solving each problem once.

Memoization - a technique for speeding up computations by caching results of repeated calculations.

Downside of memoization is memory usage.

- Repeated calculations are slow
- Memoization speeds up computations by caching intermediate results
- Memoization trade off space for speed

To avoid wasting space we can use Bottom-up dynamic programming.

- Solve earlier subproblems so they are ready when needed later
- Throw away earlier results when no longer needed

Directed Acyclic Graph (DAG)

- Graph = vertices + edges
- Edges have direction (arrow)
- No cycles: can't come back to a vertex by following edges

Recap for bottom-up approach:

- Bottom-up dynamic programming represents recursive problems as a DAG
- The DAG respresentation can be traversed in order of dependency
- Problems can be solved in minimal time and space
