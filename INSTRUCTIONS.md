## What To Do This Cycle

1. Read `data/tasks.md` and any files in `context/`.
2. Choose one target log set or one scanner improvement.
3. Run or improve `tools/audit_loop_shrink.py`.
4. Save reports under `output/`.
5. File what you learned under `knowledge/`.
6. Update `data/tasks.md` and append one concise memory line to `data/memory.md`.

## Promotion Discipline

Classify repeated shapes conservatively:

- use `script` when the same shell or file operation repeats with stable preconditions;
- use `typed_tool` when bounded parameters and validation would replace prose/tool-call repetition;
- use `fixture` when repeated judgment can be checked against evidence;
- use `approval_budget` when the action is rare, consequential, and should remain human-reviewed;
- use `deny_or_quarantine` when the action should not be in the autonomous path.

Never claim a shrink candidate without examples.
