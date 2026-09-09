# Failed result statement

## Candidate that was investigated

A naive randomized two-component lift produced an apparent candidate competitive ratio

```text
57/46 ≈ 1.2391304348
```

for online bin stretching with two bins.

## Verdict

The candidate was **rejected**.

```text
NO_NEW_BOUND_CLAIMED
```

The reason is not numerical instability, insufficient search depth, or a failed optimizer. The reason is a **soundness failure in the transfer/pruning argument** used by the audited naive implementation.

## Exact diagnostic

Using scaled offline bin capacity `23`, consider

```text
prefix = (51/10, 23/2, 83/10, 147/10)
next item = 32/5
```

Two deterministic components can place the same prefix differently:

```text
A = (69/2, 51/10)
B = (99/5, 99/5)
```

The complete five-item sequence is offline feasible because

```text
51/10 + 23/2 + 32/5 = 23
83/10 + 147/10 = 23
```

The best possible next placement gives

```text
A_best = 69/2
B_best = 131/5
```

so a 50-50 mixture has expected maximum load

```text
(69/2 + 131/5)/2 = 607/20 = 30.35.
```

The candidate target at this scale is

```text
23 * 57/46 = 57/2 = 28.5.
```

Thus

```text
607/20 - 57/2 = 37/20 > 0.
```

The continuation that invalidates the target is offline feasible. Therefore the naive joint-state pruning/lifting rule is unsafe for the intended certificate.

## What this does not show

This negative result does **not** refute the published randomized two-bin method, does not settle the randomized two-bin stretching factor, and does not prove that `57/46` is impossible by some different sound method.

It shows only that the audited naive transfer does not certify it.
