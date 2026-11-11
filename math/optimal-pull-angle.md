# Optimizing the Angle of an Applied Force

**Problem.** A block of mass $m$ sits on a flat surface with kinetic friction coefficient $\mu$. You pull it with a constant force $F_{app}$ at an angle $\theta$ above the horizontal. Which angle gives the largest acceleration?

The original handwritten version is [`optimal-angle-handwritten.jpg`](optimal-angle-handwritten.jpg).

## Setting up the acceleration

Newton's second law in the horizontal direction:

$$F_x = ma_x \qquad\Rightarrow\qquad a_x = \frac{F_x}{m}$$

Split the applied force into components:

$$F_{app,x} = F_{app}\cos\theta \qquad F_{app,y} = F_{app}\sin\theta$$

Vertically, the pull holds up part of the block's weight, so the normal force is

$$F_N = F_g - F_{app,y} = mg - F_{app}\sin\theta$$

Friction is

$$F_f = \mu F_N = \mu\,(mg - F_{app}\sin\theta)$$

So the horizontal acceleration is

$$a_x = \frac{F_{app}\cos\theta - \mu\,(mg - F_{app}\sin\theta)}{m}$$

## Maximizing it

Only $\theta$ changes. $F_{app}$, $m$, $g$ and $\mu$ are constants, so to maximize $a_x$ we take the derivative of the numerator with respect to $\theta$ and set it equal to 0.

Remember:

$$\frac{d}{d\theta}(\sin\theta) = \cos\theta \qquad \frac{d}{d\theta}(\cos\theta) = -\sin\theta$$

$$\frac{d}{d\theta}\Big(F_{app}\cos\theta - \mu\,(mg - F_{app}\sin\theta)\Big) = -F_{app}\sin\theta + \mu F_{app}\cos\theta = 0$$

Divide by $F_{app}$:

$$\mu\cos\theta - \sin\theta = 0$$

$$\mu = \frac{\sin\theta}{\cos\theta} = \tan\theta$$

$$\boxed{\theta = \tan^{-1}(\mu)}$$

The best angle depends only on the friction coefficient. It doesn't depend on the mass or on how hard you pull.

## Extra checks

*(These were not in the handwritten page.)*

- **It's a maximum.** The second derivative of the numerator is $-F_{app}\cos\theta - \mu F_{app}\sin\theta$, which is negative for $0^\circ < \theta < 90^\circ$.
- **The best acceleration.** At $\theta = \tan^{-1}(\mu)$ we have $\cos\theta = 1/\sqrt{1+\mu^2}$ and $\sin\theta = \mu/\sqrt{1+\mu^2}$, so
  $$a_{max} = \frac{F_{app}\sqrt{1+\mu^2} - \mu m g}{m}$$
  This is only an acceleration if the pull is strong enough to move the block, which means $F_{app}\sqrt{1+\mu^2} > \mu m g$.
- **The block must stay on the ground.** The model needs $F_N \ge 0$, so $F_{app}\sin\theta \le mg$. If you pull hard enough to lift the block, the friction formula no longer applies.
- **Numerical check.** For $F_{app} = 10$ N, $m = 5$ kg, $\mu = 0.3$, a brute-force search over angles finds the best angle at $16.70^\circ$, and $\tan^{-1}(0.3) = 16.70^\circ$. It also matches for $\mu = 0.1$ ($5.71^\circ$), $0.5$ ($26.57^\circ$) and $1.0$ ($45^\circ$).
