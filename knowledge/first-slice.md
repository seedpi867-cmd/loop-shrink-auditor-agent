# First Slice

The first `loop-shrink-auditor-agent` slice is deliberately narrow.

It does not try to understand full transcripts. It scans event-shaped logs and asks one question: which repeated shapes should stop consuming model judgment?

The first classifications are enough to prove the loop:

- safe repeated approvals can become scripts;
- repeated structured operations can become typed tools;
- repeated evidence checks can become fixtures;
- repeated high-risk publication or mutation stays in an approval budget;
- repeated blocked paths become deny/quarantine rules.

The next hard problem is sequence clustering. A single repeated command is easy. A recurring three-command ritual is where real shrinkage hides.
