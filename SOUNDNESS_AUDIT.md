# Soundness audit

## Question audited

Can a pruning condition that is safe for a single deterministic online component be transferred directly to a joint state representing a randomized mixture of two deterministic components?

## Finding

**Not in the naive form tested here.**

The two deterministic components can assign the same observed prefix to different load vectors. A continuation that appears prunable from one component's deterministic state can still be essential when the objective is the expected maximum load of the mixture.

The unsafe transfer arose from treating a deterministic item-bound/pruning condition as though it remained valid after moving to a joint two-component expected-load state.

## Exact counterexample

Scaled offline capacity:

```text
23
```

Prefix and next item:

```text
(51/10, 23/2, 83/10, 147/10), 32/5
```

Joint component loads before the next item:

```text
A = (69/2, 51/10)
B = (99/5, 99/5)
```

Offline feasibility is explicit:

```text
51/10 + 23/2 + 32/5 = 23
83/10 + 147/10 = 23
```

Best component-wise maxima after the next item:

```text
A_best = 69/2
B_best = 131/5
```

Expected maximum load under equal mixing:

```text
607/20
```

Target induced by the apparent `57/46` certificate:

```text
57/2
```

Violation:

```text
607/20 > 57/2
```

with exact gap

```text
37/20.
```

## Consequence

Any proof or program that removes this continuation under the naive transferred pruning rule can certify a false target. Therefore the candidate `57/46` output from that implementation is not a valid upper-bound certificate.

## Scope

This audit targets the **naive transfer used in the investigated implementation only**. It does not establish that every joint-state pruning strategy is unsound. A future method could reopen the line if it supplies a formally justified invariant that is preserved under the randomized mixture state.
