# Analytic Continuation Explanation

The zeta function is

$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + \cdots$$

That converges only when $\text{Re}(s) > 1$.

Since we want to use the critical line, where $\text{Re}(s) = \tfrac{1}{2}$, the series will diverge.

This means we have to use the Dirichlet eta function:

$$\eta(s) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^s} = 1 - \frac{1}{2^s} + \frac{1}{3^s} - \frac{1}{4^s} + \cdots \quad \text{for } \text{Re}(s) > 0$$

Notice that the eta function is just (odd terms) − (even terms).

## Breaking down the zeta function

$$\zeta(s) = \sum_{n \text{ odd}} \frac{1}{n^s} + \sum_{n \text{ even}} \frac{1}{n^s}$$

The even terms are

$$\sum_{n \text{ even}} \frac{1}{n^s} = \frac{1}{2^s}\zeta(s)$$

so the odd terms are

$$\sum_{n \text{ odd}} \frac{1}{n^s} = \zeta(s) - \frac{1}{2^s}\zeta(s) = (1 - 2^{-s})\zeta(s)$$

Substitute the odd terms and the even terms into $\eta(s)$ = (odd) − (even):

$$\eta(s) = (1 - 2^{-s})\zeta(s) - \frac{1}{2^s}\zeta(s)$$

Simplify:

$$\eta(s) = (1 - 2^{1-s})\zeta(s)$$

And since $\eta(s)$ is the alternating sum above, this is the same as

$$\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^s} = (1 - 2^{1-s})\zeta(s)$$

## Solving for zeta

Dividing both sides by $1 - 2^{1-s}$ gives the formula the code uses:

$$\zeta(s) = \frac{\eta(s)}{1 - 2^{1-s}}$$

This works for $\text{Re}(s) > 0$, $s \neq 1$. At $s = 1$ the denominator is zero, and that is where $\zeta$ has its pole. The denominator is also zero at $s = 1 + \frac{2\pi i k}{\ln 2}$, but those points are not on the critical line, so `zetaxc.py` never lands on them.
