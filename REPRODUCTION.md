# Reproduction

The repository contains one exact-rational Python script and its frozen output.

## Requirements

- Python 3
- standard library only

No external solver, floating-point tolerance, random seed, or network access is required.

## Run

```bash
python reproduce_fail_bin_stretching.py
```

Expected final lines:

```text
RESULT_E1 = PASS_REPRODUCED_7_6
RESULT_E2 = PASS_NAIVE_LIFT_DIAGNOSTIC_FAILS_TARGET
FINAL = NO_NEW_BOUND_CLAIMED
```

## E1 — exact 7/6 reproduction

The script evaluates the two-sequence Yao support

```text
S1 = (1/3, 1/3, 2/3, 2/3)
S2 = (1/3, 1/3, 1)
```

with probability `1/2` on each sequence. Decisions are constrained so that a deterministic online algorithm must make the same move whenever its observable history, current canonical loads, and current item coincide.

The exact value is

```text
7/6
```

and the script also reports 18 reachable meta-states, 9 observable information sets, and 6 terminal meta-states.

## E2 — failed-lift diagnostic

The script then checks the explicit offline-feasible witness described in `SOUNDNESS_AUDIT.md` using `fractions.Fraction` throughout.

It proves exactly that

```text
best 50-50 expected maximum load = 607/20
candidate scaled target = 57/2
607/20 - 57/2 = 37/20 > 0
```

The purpose of E2 is to falsify the audited naive transfer, not to certify a new competitive ratio.

## Frozen output

`experiment_log.txt` records the expected output of the script. A clean reproduction should match its mathematical values exactly.
