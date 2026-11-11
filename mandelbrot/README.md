# Mandelbrot Set

Draws the Mandelbrot set in Minecraft, one wool block per point of the complex plane.

![Mandelbrot set in Minecraft](MandelbrotVisual.png)

## How it works

Each block is a complex number $c$. Starting from $z_0 = 0$, the script repeats $z_{n+1} = z_n^2 + c$.

- If $|z|$ ever gets bigger than 2, the point **escapes**. It is not in the set, and its wool color depends on how many steps it took to escape.
- If it hasn't escaped after `max_iter` steps, the point is treated as **inside the set** and gets black wool.

The block grid maps to the plane like this: the block at column `x`, row `z` is the complex number

```
real = (x - width/2)  * scale + center_re
imag = (z - height/2) * scale + center_im
```

`scale` is how much of the plane each block covers, so a smaller `scale` is a deeper zoom.

## Patterns

`mandelbrot.py` draws four patterns one after another. It waits for you to press Enter between them.

| # | Size | Iterations | Scale | Center | View |
|---|---|---|---|---|---|
| 1 | 200 × 200 | 30 | 0.015 | −0.75 + 0i | Full set |
| 2 | 300 × 300 | 40 | 0.010 | −0.75 + 0i | Full set, bigger |
| 3 | 400 × 400 | 50 | 0.007 | −0.75 + 0i | Full set, biggest |
| 4 | 150 × 150 | 150 | 0.001 | −0.7436 + 0.1318i | Zoom into Seahorse Valley |

The set runs from about −2 to 0.47 on the real axis, so the full views are centered at −0.75 to keep all of it in frame.

Patterns draw over each other at the same spot, so each later pattern replaces the earlier one.

## Run it

```bash
python mandelbrot.py
```

See the [main README](../README.md#setup) for the server and RCON setup. The password is in `MinecraftRCON.__init__`.

## Files

- `mandelbrot.py`: the generator
- `explanation.md`: the math, written for Algebra 2 students, including a proof that the radius-2 escape test works
- `MandelbrotVisual.png`: a screenshot of the finished render in the game
