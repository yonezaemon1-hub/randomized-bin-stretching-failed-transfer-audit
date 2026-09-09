# Status

## Current classification

```text
FROZEN NEGATIVE RESULT
NO_NEW_BOUND_CLAIMED
```

This line is not counted as a successful paper result.

## Completed checks

- Exact reproduction of the classic `7/6` Yao support: PASS.
- Exact arithmetic for the failed-transfer diagnostic: PASS.
- Offline feasibility of the counterexample continuation: PASS.
- Candidate `57/46` certificate under the audited naive transfer: REJECTED.

## Why the line is frozen

The apparent improvement depended on a joint-state pruning/lifting rule whose soundness did not survive audit. Once the boundary continuation was restored, the candidate target was violated by an offline-feasible sequence.

## Reopening conditions

Reopen only if at least one of the following is obtained:

1. a new pruning invariant proved sound for joint randomized-mixture states;
2. an independent exact formulation that certifies a bound without the rejected transfer;
3. a machine-checkable certificate whose verifier does not depend on the unsafe rule;
4. new theory that changes the state representation enough to remove the counterexample mechanism.

A lower numerical output from the same unsound pruning rule is not a reopening condition.
