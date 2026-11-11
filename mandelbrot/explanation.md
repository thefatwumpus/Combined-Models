# Clarification on the Mandelbrot Fractal for Algebra 2 Students

## Complex numbers

First, the definition of a complex number.

Its form is $a + bi$, where:

- $a$ = the real part
- $bi$ = the imaginary part
- $i$ = the square root of $-1$

Now, how can you plot imaginary points? How did I use this to map colored blocks to specific coordinates in Minecraft?

Complex numbers are like points on a coordinate plane:

- The **x-axis** is the real part ($a$).
- The **y-axis** is the imaginary part ($b$).

So $3 + 2i$ is just the point $(3, 2)$ on the complex plane.

## The Mandelbrot rule

We start with $z_0 = 0$ and repeatedly do:

$$z_{n+1} = z_n^2 + c$$

where $c$ is the complex number (the point we're testing).

### Test: c = 1

$$z_1 = 0^2 + 1 = 1$$
$$z_2 = 1^2 + 1 = 2$$
$$z_3 = 2^2 + 1 = 5$$

When it keeps getting bigger and bigger, it escapes, which means $c$ is **not** in the Mandelbrot set. In the Minecraft visual, escaped points get a colored wool block. The color depends on how many steps it took to escape.

### Test: c = -1

$$z_0 = 0$$
$$z_1 = -1$$
$$z_2 = (-1)^2 + (-1) = 0$$
$$z_3 = 0^2 + (-1) = -1$$

It keeps bouncing between 0 and -1, so it never escapes, which means $c$ is **inside** the Mandelbrot set. In the Minecraft visual these points are black wool.

## The escape test in Python

```python
if abs(z) > 2:
    return n  # Escaped!
```

What does this mean?

`abs(z)` calculates the distance from $z$ (the current value in the sequence) to the origin $(0, 0)$ using the distance formula.

Why 2 specifically? Mathematicians have proven that:

- If $|z_n|$ ever gets bigger than 2, the sequence is guaranteed to escape to infinity, so we can stop calculating for that point.
- If it stays inside the circle of radius 2 for all the steps we check, the point might still be part of the Mandelbrot set.

Of course, I wouldn't just leave you with a claim without proving it. Let's prove it.

## Why 2 works

From before, each step in the Mandelbrot formula is

$$z_{n+1} = z_n^2 + c$$

Note that $z_n = a + bi$.

Also, for any point $c$ on the plane, $|c|$ is the distance from $c$ to the origin.

So using the distance formula, $|z_n| = \sqrt{a^2 + b^2}$.

This is the distance from the origin in the complex plane.

Every point in the Mandelbrot set has $|c| \le 2$, so we can assume that. Suppose $|z_n| > 2$ at some step. Then:

1. Squaring makes the distance much bigger: $|z_n^2| = |z_n|^2$.
2. Adding $c$ can only pull it back by at most $|c| \le 2$, so
   $$|z_{n+1}| \ge |z_n|^2 - 2$$
3. Look at how far past 2 we are. Call that excess $\varepsilon_n = |z_n| - 2$. Then
   $$\varepsilon_{n+1} = |z_{n+1}| - 2 \ge |z_n|^2 - 4 = (|z_n| - 2)(|z_n| + 2) = \varepsilon_n(|z_n| + 2) > 4\varepsilon_n$$

So once a point gets past 2, the amount it is past 2 **at least quadruples every step**. It can never come back, which means it keeps getting farther and farther away and escapes to infinity.

(If $|c| > 2$, then $c$ is already outside the circle at step one and escapes too, so it isn't in the set.)
