# The Ulam Spiral

The Ulam spiral is a visual pattern of positive integers (natural numbers) arranged in a square spiral where the prime numbers are highlighted. The spiral starts at 1 and then wraps around. Each point on the spiral is mapped onto a Minecraft coordinate in-game.

It starts at 1 and wraps around clockwise (as seen from above), starting from the right of the center at 2:

```
7 8 9
6 1 2
5 4 3
```

## How does the program detect primes?

The logic behind prime detection is a trial division algorithm:

- It checks the number's divisibility by 2 and 3 first.
- Then it checks numbers of the form 6k ± 1 only. Every prime above 3 has this form.
- The key fact: if $n = a \cdot b$, then at least one of $a$ or $b$ must be $\le \sqrt{n}$.
- So if $n$ has any factor at all, one of them will be $\le \sqrt{n}$.

### Example: is 91 prime?

- 91 is not divisible by 2 or 3.
- It is of 6k ± 1 form: $15 \cdot 6 + 1 = 91$.
- Check divisors up to $\sqrt{91} \approx 9.5$, so try 2, 3, 5, 7.
- $91 / 7 = 13$.

So 91 is not prime.

(Being of the form 6k ± 1 doesn't make a number prime, only a candidate. 91 shows that.)

### Example: is 97 prime?

- 97 is not divisible by 2 or 3.
- It is of 6k ± 1 form: $16 \cdot 6 + 1 = 97$.
- $\sqrt{97} \approx 9.8$, so try 2, 3, 5, 7.
- None divides 97.

So 97 is prime.
