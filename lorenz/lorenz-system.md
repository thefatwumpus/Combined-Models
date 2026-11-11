# The Lorenz System

The Lorenz attractor comes from a system of three differential equations. $x$, $y$, and $z$ represent the point moving through 3D space.

$$\frac{dx}{dt} = \sigma(y - x)$$

$$\frac{dy}{dt} = x(\rho - z) - y$$

$$\frac{dz}{dt} = xy - \beta z$$

(`lorenz.py` uses the classic values $\sigma = 10$, $\rho = 28$, $\beta = 8/3$.)

Looks intimidating, but it's just saying that there's a constant tug of war between $x$, $y$, and $z$.

- **$x$** is always chasing $y$. If $y$ is ahead of $x$, $x$ speeds up to close the gap. If $y$ falls behind, $x$ pulls back. It never quite catches up; that's the chase that keeps the system moving.
- **$y$** is caught between two forces: $x$ is pushing it forward (the chase from above creates pressure), but $z$ is dragging it back. The bigger $z$ gets, the more it resists $y$'s growth. So $y$ is always being stretched and reined in at the same time.
- **$z$** is driven upward by the activity between $x$ and $y$. Specifically, how much they're interacting. But it also has a natural tendency to decay back toward zero. So $z$ is constantly being fed by $x$ and $y$ while slowly bleeding away on its own.
- This is why the tug of war is never resolved. $x$ chases $y$, $y$ gets pulled by $z$, $z$ gets fed by $x$ and $y$. It's a game of tug of war with no winner, which is why the path never settles and never repeats.

## Why it's chaotic

This is unique because it's chaotic:

- Completely deterministic
- Sensitive to initial conditions
- Yet its path is not easily predictable

Two almost identical points can diverge quickly due to their initial conditions. This is popularly known as the **butterfly effect**.

- Every loop is slightly different.
- The path stays in a bounded region and never traces the same route twice.
- It's a cool representation of how an infinitely long curve can fit into a finite volume.

The Lorenz attractor is a strong example of the core concept in chaos theory: ***sensitive dependence on initial conditions***.
