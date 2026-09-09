#!/usr/bin/env python3
"""
Reproducibility experiments for:

[FAIL] A Computational Audit of Randomized Two-Bin Stretching

This script deliberately contains only small, independently checkable
experiments. It does NOT certify any new competitive-ratio upper bound.

Experiments
-----------
E1. Exact finite decision-tree reproduction of the classic 7/6 Yao support:
    S1 = (1/3, 1/3, 2/3, 2/3)
    S2 = (1/3, 1/3, 1)
    each with probability 1/2.

E2. Exact-arithmetic diagnostic witness showing why a naive joint-state
    pruning/lifting rule can be unsafe. This is a counterexample to the
    audited naive implementation, NOT to the published randomized M2 method.
"""

from fractions import Fraction as F
from functools import lru_cache
from collections import deque


def canonical_loads(a, b):
    return tuple(sorted((a, b), reverse=True))


# ---------------------------------------------------------------------
# E1: exact 7/6 reproduction
# ---------------------------------------------------------------------

seqs = [
    (F(1, 3), F(1, 3), F(2, 3), F(2, 3)),
    (F(1, 3), F(1, 3), F(1, 1)),
]
probs = [F(1, 2), F(1, 2)]


@lru_cache(None)
def solve(active):
    active = tuple(active)
    if all(pos >= len(seqs[i]) for i, pos, hi, lo in active):
        return sum(probs[i] * max(hi, lo) for i, pos, hi, lo in active)

    # The deterministic online algorithm must use the same action whenever
    # its observable history, current loads, and current item are identical.
    groups = {}
    for rec in active:
        i, pos, hi, lo = rec
        if pos < len(seqs[i]):
            key = (seqs[i][:pos], canonical_loads(hi, lo), seqs[i][pos])
            groups.setdefault(key, []).append(rec)

    key = sorted(groups.keys(), key=str)[0]
    group = groups[key]

    best = None
    for target in (0, 1):
        nxt = []
        for rec in active:
            i, pos, hi, lo = rec
            if rec in group:
                loads = list(canonical_loads(hi, lo))
                loads[target] += seqs[i][pos]
                nhi, nlo = canonical_loads(*loads)
                nxt.append((i, pos + 1, nhi, nlo))
            else:
                nxt.append(rec)
        val = solve(tuple(nxt))
        best = val if best is None else min(best, val)
    return best


initial = tuple((i, 0, F(0), F(0)) for i in range(2))
e1_value = solve(initial)

# Count all reachable meta-states and observable decision information sets.
seen = {initial}
q = deque([initial])
infos = set()
terminal_values = []

while q:
    active = q.popleft()
    if all(pos >= len(seqs[i]) for i, pos, hi, lo in active):
        terminal_values.append(
            sum(probs[i] * max(hi, lo) for i, pos, hi, lo in active)
        )
        continue

    groups = {}
    for rec in active:
        i, pos, hi, lo = rec
        if pos < len(seqs[i]):
            key = (seqs[i][:pos], canonical_loads(hi, lo), seqs[i][pos])
            groups.setdefault(key, []).append(rec)

    key = sorted(groups.keys(), key=str)[0]
    infos.add(key)
    group = groups[key]

    for target in (0, 1):
        nxt = []
        for rec in active:
            i, pos, hi, lo = rec
            if rec in group:
                loads = list(canonical_loads(hi, lo))
                loads[target] += seqs[i][pos]
                nhi, nlo = canonical_loads(*loads)
                nxt.append((i, pos + 1, nhi, nlo))
            else:
                nxt.append(rec)
        nxt = tuple(nxt)
        if nxt not in seen:
            seen.add(nxt)
            q.append(nxt)

# Offline feasibility checks for the two inputs.
assert seqs[0][0] + seqs[0][2] == 1
assert seqs[0][1] + seqs[0][3] == 1
assert seqs[1][0] + seqs[1][1] == F(2, 3)
assert seqs[1][2] == 1
assert e1_value == F(7, 6)

# ---------------------------------------------------------------------
# E2: exact-arithmetic diagnostic against the naive lift
# ---------------------------------------------------------------------

# Scaled capacity is 23 per offline bin.
prefix = [F(51, 10), F(23, 2), F(83, 10), F(147, 10)]
next_item = F(32, 5)

# Two deterministic components can place the SAME prefix differently.
# Component A:
A = (F(69, 2), F(51, 10))     # 34.5, 5.1
# Component B:
B = (F(99, 5), F(99, 5))      # 19.8, 19.8

# Explicit offline packing of all five items:
offline_bin_1 = F(51, 10) + F(23, 2) + next_item
offline_bin_2 = F(83, 10) + F(147, 10)

assert offline_bin_1 == 23
assert offline_bin_2 == 23

# Best possible placement of the next item for each component.
A_best = min(max(A[0] + next_item, A[1]),
             max(A[0], A[1] + next_item))
B_best = min(max(B[0] + next_item, B[1]),
             max(B[0], B[1] + next_item))

expected_best = (A_best + B_best) / 2
candidate_target_scaled = F(57, 2)  # 23 * (57/46)

assert expected_best == F(607, 20)
assert expected_best > candidate_target_scaled

print("=== E1: exact Yao-support reproduction ===")
print("support_1 =", seqs[0])
print("support_2 =", seqs[1])
print("probabilities = 1/2, 1/2")
print("reachable_meta_states =", len(seen))
print("observable_information_sets =", len(infos))
print("terminal_meta_states =", len(terminal_values))
print("optimal_deterministic_expected_max_load =", e1_value)
print("RESULT_E1 = PASS_REPRODUCED_7_6")
print()

print("=== E2: diagnostic witness against naive joint pruning ===")
print("prefix =", tuple(prefix))
print("next_item =", next_item)
print("component_A_loads =", A)
print("component_B_loads =", B)
print("offline_bin_1 =", offline_bin_1)
print("offline_bin_2 =", offline_bin_2)
print("A_best_after_next =", A_best)
print("B_best_after_next =", B_best)
print("best_50_50_expected_max_load =", expected_best)
print("candidate_57_46_scaled_target =", candidate_target_scaled)
print("gap =", expected_best - candidate_target_scaled)
print("RESULT_E2 = PASS_NAIVE_LIFT_DIAGNOSTIC_FAILS_TARGET")
print()
print("FINAL = NO_NEW_BOUND_CLAIMED")
