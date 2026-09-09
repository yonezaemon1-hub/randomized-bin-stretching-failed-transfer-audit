# FAIL — Randomized Two-Bin Stretching: Failed Transfer Audit

**Ryutaro Yonezu — Independent Researcher**

Status: **FROZEN NEGATIVE RESULT / NO NEW BOUND CLAIMED**

This repository records a failed research direction in randomized online bin stretching with two bins. It is intentionally published as a negative-result and soundness-audit artifact.

The repository does **not** claim a new competitive-ratio upper bound.

## What was reproduced

A small exact decision-tree calculation reproduces the classic `7/6` Yao lower-bound support using

```text
S1 = (1/3, 1/3, 2/3, 2/3)
S2 = (1/3, 1/3, 1)
probabilities = 1/2, 1/2
```

The exact computation gives

```text
optimal deterministic expected maximum load = 7/6
RESULT_E1 = PASS_REPRODUCED_7_6
```

The finite decision tree contains 18 reachable meta-states, 9 observable information sets, and 6 terminal meta-states.

## What failed

A naive joint-state lifting/pruning idea appeared to support a candidate value

```text
57/46 ≈ 1.2391304348
```

for a two-algorithm randomized mixture. The transfer was rejected after a soundness audit.

The failure is specific and reproducible: a pruning rule valid for a deterministic component was transferred naively to a joint expected-load state. An exact counterexample shows that the discarded boundary continuation can remain offline-feasible and can force the 50-50 expected maximum load above the candidate target.

The diagnostic witness uses scaled offline capacity `23` and

```text
prefix = (51/10, 23/2, 83/10, 147/10)
next item = 32/5
component A loads = (69/2, 51/10)
component B loads = (99/5, 99/5)
```

All five items admit an offline packing into two bins of load exactly `23` each. After the next item,

```text
A best maximum load = 69/2
B best maximum load = 131/5
50-50 expected maximum load = 607/20
candidate 57/46 target at scale 23 = 57/2
gap = 37/20 > 0
```

Hence the audited naive lift does not certify `57/46`.

## Critical scope boundary

This is a counterexample to the **audited naive joint-state pruning/lifting rule**.

It is **not** a counterexample to the published randomized two-bin method or to the open problem itself.

## Final verdict

```text
RESULT_E1 = PASS_REPRODUCED_7_6
RESULT_E2 = PASS_NAIVE_LIFT_DIAGNOSTIC_FAILS_TARGET
FINAL = NO_NEW_BOUND_CLAIMED
```

The research line is frozen unless a new sound transfer principle, pruning invariant, or independently verified certificate is found.

## Files

- `reproduce_fail_bin_stretching.py` — exact-rational reproduction and diagnostic witness.
- `experiment_log.txt` — frozen output from the reproduction script.
- `FAILED_RESULT.md` — concise negative-result statement.
- `SOUNDNESS_AUDIT.md` — why the transfer was rejected.
- `REPRODUCTION.md` — reproduction instructions.
- `STATUS.md` — freeze status and reopening conditions.
- `CITATION.cff` — citation metadata for this negative-result repository.
- `.zenodo.json` — optional Zenodo software/research-package metadata.
- `LICENSE` — MIT license for code and repository utilities.

## Research-integrity policy

Failed computations are retained when they materially constrain future work. A numerically attractive candidate is not treated as a result unless its transfer, pruning, and certification steps are sound.
