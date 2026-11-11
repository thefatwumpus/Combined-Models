# Expressing Coupled Generating Functions in Terms of Each Other

The other day I was introduced to two freshmen in multivariable calculus by my old math teacher. One of them, I'll call him Z, was working on a problem about how to get two generating functions for a pair of recursive sequences in terms of each other. At the time I didn't catch a thing, but it actually isn't too hard to break down with just Algebra 2 knowledge. And it's pretty interesting.

## Setup

Say you have

$$A(x) = \sum_{n=0}^{\infty} a_n x^n \qquad B(x) = \sum_{n=0}^{\infty} b_n x^n$$

So

$$A(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \cdots \qquad B(x) = b_0 + b_1 x + b_2 x^2 + b_3 x^3 + \cdots$$

The recurrence relation looks like:

$$a_{n+1} = p\,a_n + q\,b_n$$
$$b_{n+1} = r\,a_n + s\,b_n$$

for $n = 0, 1, 2, \ldots$

This just asks how much of the previous term contributes to the next term when the two sequences depend on each other.

- To get the next $a$, take $p$ copies of the current $a$ plus $q$ copies of the current $b$.
- To get the next $b$, take $r$ copies of the current $a$ plus $s$ copies of the current $b$.

## Shifting the index

But looking at our generating functions, we only have $a_n$ and $b_n$, not $a_{n+1}$ and $b_{n+1}$.

To fix this we have to shift everything over by 1.

$$A(x) - a_0 = a_1 x + a_2 x^2 + a_3 x^3 + \cdots$$

Divide by $x$:

$$\frac{A(x) - a_0}{x} = a_1 + a_2 x + a_3 x^2 + \cdots$$

Now the right-hand side is

$$\sum_{n=0}^{\infty} a_{n+1} x^n$$

So

$$\frac{A(x) - a_0}{x} = \sum_{n=0}^{\infty} a_{n+1} x^n$$

## Plugging into the recurrence

Plug this back into the first recurrence, after multiplying it by $x^n$ and summing over $n$:

$$\sum_{n=0}^{\infty} a_{n+1} x^n = p \sum_{n=0}^{\infty} a_n x^n + q \sum_{n=0}^{\infty} b_n x^n$$

---
