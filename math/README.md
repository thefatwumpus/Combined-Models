# Math Notes

General Math proofs I was working on that I thought were pretty cool.

## Coupled generating functions

[`generating-functions.md`](generating-functions.md) shows how to take two sequences that depend on each other,

$$a_{n+1} = p\,a_n + q\,b_n \qquad b_{n+1} = r\,a_n + s\,b_n$$

and turn their generating functions $A(x)$ and $B(x)$ into a pair of ordinary algebra equations:

$$\begin{bmatrix} 1 - px & -qx \\ -rx & 1 - sx \end{bmatrix} \begin{bmatrix} A \\ B \end{bmatrix} = \begin{bmatrix} a_0 \\ b_0 \end{bmatrix}$$

[`handwritten-notes.jpg`](handwritten-notes.jpg) is the original handwritten version, including a couple of follow-up questions (triangular numbers and exponential generating functions).

## Optimal angle for pulling a block

[`optimal-pull-angle.md`](optimal-pull-angle.md) uses calculus to find the angle that gives a block the largest acceleration when you pull it at an angle against friction. The answer is $\theta = \tan^{-1}(\mu)$. The handwritten original is [`optimal-angle-handwritten.jpg`](optimal-angle-handwritten.jpg).
