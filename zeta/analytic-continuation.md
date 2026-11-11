# So what makes analytic continuation a continuation and not a new function entirely?

It has to do with the fact that they are analytic functions.

An analytic function is a well-behaved (continuous, single-valued, and infinitely differentiable) function that can be represented by a **convergent power series** near any point in its domain.

For the zeta and eta functions, in their overlap region (where both definitions converge, $\text{Re}(s) > 1$), they agree.

Analytic functions are determined by local data. If you know all the derivatives at one point, you know the entire function in that connected region. So the eta-based formula can't be a different function: it has to be the zeta function extended to a bigger region.

## Power series

A power series is an infinite sum that acts as an "infinite polynomial" used to represent functions, taking the form

$$\sum_{n=0}^{\infty} c_n (x - a)^n = c_0 + c_1(x - a) + c_2(x - a)^2 + \cdots$$

where $c_n$ are coefficients, $x$ is a variable, and $a$ is a constant center.

## Convergent vs. divergent

Convergent series have terms that sum to a finite, specific number as more terms are added, whereas divergent series have sums that approach infinity, negative infinity, or oscillate without settling on a single value.

## What does single-valued mean?

For every input in the domain, the function returns one unique output value in the range.
