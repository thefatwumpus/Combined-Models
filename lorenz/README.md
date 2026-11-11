# Lorenz Attractor

Draws the Lorenz attractor, the "butterfly" that comes out of three simple differential equations, in 3D with colored wool.

![Lorenz attractor in Minecraft](LorenzAttractor.png)

## How it works

The Lorenz system is

$$\frac{dx}{dt} = \sigma(y - x) \qquad \frac{dy}{dt} = x(\rho - z) - y \qquad \frac{dz}{dt} = xy - \beta z$$

with the classic values $\sigma = 10$, $\rho = 28$, $\beta = 8/3$.

1. The script starts at $(0.1, 0.1, 0.1)$ and steps the system forward with **4th-order Runge-Kutta (RK4)**, using `dt = 0.005` for 60,000 steps.
2. It scales each point by `3.5` and uses it as a Minecraft position around `(0, 70, 0)`.
3. Every second point (`skip = 2`) becomes a wool block, so the script sends about 30,000 `setblock` commands.
4. The wool color cycles through 11 colors from red to pink as time goes on, so you can see the order in which the path was traced.

The Lorenz $x$ and $z$ coordinates are Minecraft's horizontal axes and Lorenz $y$ is height. Look down on it from above to see the two-wing butterfly.

The structure's shadow on the ground shows the same butterfly outline:

![Shadow of the Lorenz attractor on the ground](LorenzShadow.png)

## Run it

```bash
pip install numpy rcon
python lorenz.py
```

Set the server password in the `PASSWORD` variable at the bottom of the file. See the [main README](../README.md#setup) for the RCON setup.

## Files

- `lorenz.py`: the simulation and the block placement
- `what-is-a-differential-equation.md`: a plain-language intro to differential equations
- `lorenz-system.md`: what each equation means, and why the system is chaotic
- `LorenzAttractor.png`: a screenshot of the result
- `LorenzShadow.png`: the structure's shadow on the ground, which is the butterfly seen from above
