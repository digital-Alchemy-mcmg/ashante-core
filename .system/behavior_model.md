# AI WORKER RULES
1. CLAIM: Pick highest priority PENDING task from docs/queue.csv.
2. FETCH: Pull spec and draft code.
3. VERIFY: Run verification.
4. WRITE: Update docs/queue.csv.
5. COMMIT: If PASS, commit to main.
6. NO HALLUCINATIONS: If status is unknown, it is NOT_RUN.
