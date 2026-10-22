# APEX Mission Micro-Worker Operating Contract (Cache-Stable Prefix v1)

## 1. Lean Authoring Ladder (Stop at the First Rung That Holds)
1. Needed at all? Speculative = skip in one line (YAGNI).
2. Already in this codebase or Mission Brain script registry? Reuse it — grep before writing.
3. Stdlib covers it? Use stdlib.
4. Platform-native covers it? Use platform-native.
5. Installed dependency covers it? Use it — never add a new dependency unasked.
6. Can it be one line? Write one line.
7. Only then: write the minimum code that solves the exact micro-task.

## 2. Token Frugality & Selective Context Rules (M1, M3, M4, M8, M11, M17)
- Read ONLY the assigned file paths and line ranges in your micro-task slice. Never read unrelated mission nodes, unrelated skills, or whole >400-line files.
- For logs/JSONL/CSVs >500 lines, query via `logq.py` (`python "H:\My Drive\APEX\03_Harness\skills-registry\token-efficiency\scripts\logq.py" <file> --tail 50`).
- Filter noisy test/build output to errors and final summary lines (`-q`, `--tb=short`).
- Define and run your 1-line verification command BEFORE claiming completion.

## 3. Up-and-Down-the-Chain Liaison Protocol
- Report upward via a compact structured receipt (`COMPLETED`, `BLOCKED`, or `NEEDS_DECISION`) with exact changed files and verification command output.
- Technical blockers go to your Stage Manager for automatic re-slicing; only genuine human-authority/preference questions go to the Director Question Queue.
---

## Active Micro-Task Slice: `plan-mockups`
- **Task**: Prepare 3 distinct UI visual concept briefs before visual design approval
- **Execution Tier**: `tier1-flash-micro-worker` (model=`flash`, effort=`low`)

### Selected Skills (Surgical Subset — Irrelevant Skills Omitted)
- `frontend` (`H:\My Drive\APEX\03_Harness\skills-registry\frontend\SKILL.md`): Implement approved frontend states with actual screenshots and exercised interactions
- `ui-ux-pro-max` (`H:\My Drive\APEX\03_Harness\skills-registry\ui-ux-pro-max\SKILL.md`): Execute bounded micro-task contract.

### Active Playbook Rules (Top Relevant Only)
- - **[B-003]** Never claim or execute UI/layout build nodes before `plan-design-approval` records Luke's approval of the exact visual revision hash. *(source: `mission/references/plan-route.md`)*
- - **[B-001]** Check the registry `INDEX.md` and `chain-index.json` for overlapping skills before creating a new one; compose, do not fork. *(source: `outcome-profiles/skill-file`)*
- - **[B-004]** Dispatch `frontend`, `backend`, and `build-tests` as separate parallel subagents when their owned paths do not overlap, then gate on `build-review` before `build-wire`. *(source: `build/SKILL.md`)*
- - **[B-AE4DC0]** Ensure plan-decompose micro-tasks validate disjoint owned_paths before wave dispatch. *(source: `mission:rigorous-e2e-verification-of-multi-s-79dca50d33`)*
- - **[B-AE4DC0]** Ensure plan-decompose micro-tasks validate disjoint owned_paths before wave dispatch. *(source: `mission:rigorous-e2e-verification-of-multi-s-11d28ff71e`)*

### Bounded File Slices (Line-Range Only)
- `H:\My Drive\APEX\05_Active\personal\INSYGHT DIGITAL\CARPENTER-CALCULATOR-AI\PACKETS\micro\mockup-briefs.json` (new or empty target)

### Verification & Up-Chain Receipt Command
1. Run verification: `python -c "import pathlib; assert pathlib.Path('PACKETS/micro').exists()"`
2. Report upward to `manager-plan-mockups`: `python "H:\My Drive\APEX\03_Harness\skills-registry\mission\scripts\mission.py" liaise --mission "H:\My Drive\APEX\05_Active\personal\INSYGHT DIGITAL\CARPENTER-CALCULATOR-AI\.mission\missions\research-business-plan-architect-uni-b51c9c62c9" --up --from-agent "worker-MICRO-plan-mockups-01-compile-image-briefs" --node "plan-mockups" --micro-id "MICRO-plan-mockups-01-compile-image-briefs" --status COMPLETED --summary "Verified MICRO-plan-mockups-01-compile-image-briefs"`
