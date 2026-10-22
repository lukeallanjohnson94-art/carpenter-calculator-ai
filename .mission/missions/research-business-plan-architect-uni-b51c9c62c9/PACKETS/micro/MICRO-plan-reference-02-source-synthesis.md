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

## Active Micro-Task Slice: `plan-reference`
- **Task**: Synthesise bounded primary-source reference findings and upfront questions
- **Execution Tier**: `tier1-flash-lite-read` (model=`flash_lite`, effort=`low`)

### Selected Skills (Surgical Subset — Irrelevant Skills Omitted)
- `fire-up` (`H:\My Drive\APEX\03_Harness\skills-registry\fire-up\SKILL.md`): A planned and running structure of projects, sections and sessions, with every question asked through one director, shown with a visual of the work it affects, 

### Active Playbook Rules (Top Relevant Only)
- - **[R-001]** Lead with a findings table whose columns are `Finding`, `What it means for Luke`, and `Source`. *(source: `outcome-profiles/research-brief`)*
- - **[R-002]** Prefer primary sources (official docs, papers, verified local files) and date them. *(source: `outcome-profiles/research-brief`)*
- - **[R-003]** Tie every finding to Luke's named system (e.g. `/mission`, `SCAILD`, `PRYZM`) rather than generic advice. *(source: `outcome-profiles/research-brief`)*
- - **[R-004]** Automatically chain `source-intake` -> `source-extract` (exact locators) -> `source-reconcile` (conflict/staleness flags) whenever ingesting external docs or media. *(source: `suite.json`)*
- - **[D-24F04B]** Always embed the resolved child-skill tree from suite.json directly inside the compiled stage packet. *(source: `mission:verify-upgraded-active-mission-orche-6070e339e3`)*

### Bounded File Slices (Line-Range Only)
- `H:\My Drive\APEX\05_Active\personal\INSYGHT DIGITAL\CARPENTER-CALCULATOR-AI\PACKETS\micro\ref-synthesis.md` (new or empty target)

### Verification & Up-Chain Receipt Command
1. Run verification: `python -c "import pathlib; assert pathlib.Path('PACKETS').exists()"`
2. Report upward to `manager-plan-reference`: `python "H:\My Drive\APEX\03_Harness\skills-registry\mission\scripts\mission.py" liaise --mission "H:\My Drive\APEX\05_Active\personal\INSYGHT DIGITAL\CARPENTER-CALCULATOR-AI\.mission\missions\research-business-plan-architect-uni-b51c9c62c9" --up --from-agent "worker-MICRO-plan-reference-02-source-synthesis" --node "plan-reference" --micro-id "MICRO-plan-reference-02-source-synthesis" --status COMPLETED --summary "Verified MICRO-plan-reference-02-source-synthesis"`
