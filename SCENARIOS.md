# Review scenarios

Open each branch as a pull request against `main` and compare what
`prana-reviewer[bot]` does with the expectation. "Expected" for planted
problems is what a careful human reviewer would say; the model may word it
differently, pick a different line inside the hunk, or miss it - record what
actually happened, that is the point of the exercise.

## Planted problems (the model should flag these)

| # | Branch | Language | Planted problem | A good review says |
|---|---|---|---|---|
| 1 | `demo/sql-injection` | Python | `search_users` builds SQL with an f-string from user input | critical · SECURITY: SQL injection; use a parameterised `LIKE ?` |
| 2 | `demo/null-check` | TypeScript | `avatarHtml` reads `user.profile.avatarUrl` though `profile` is optional | warning · BUG: crash when `profile` is undefined; use `?.` / a default |
| 3 | `demo/slow-loop` | Python | membership tests on a list inside a loop, nested scan per user | warning · PERF: O(n²); use a set / a dict of totals |
| 4 | `demo/hardcoded-secret` | JavaScript | a payments API key in source as a fallback | critical · SECURITY: secret in code; keep it in the environment only |
| 5 | `demo/go-ignored-error` | Go | `Move` discards the error from `Reserve` and adds stock anyway | critical/warning · BUG: stock created from nothing when reserve fails |
| 6 | `demo/rust-unwrap` | Rust | `port_from_env` unwraps a missing or invalid `PORT` | warning · BUG: panics; return `Result` / use `parse_port` |
| 7 | `demo/insecure-deserialization` | Python | `pickle.loads` on a cookie; `open()` on a user-supplied file name | critical · SECURITY: remote code execution; path traversal |
| 8 | `demo/missing-test` | Python | new `apply_coupon` with four branches and no tests | info/warning · TEST: add tests for the branches |

## Behaviour of the GitHub App

| # | Branch / action | What to check |
|---|---|---|
| 9 | `demo/clean-change` | Well-tested, correct code: few or no comments, nothing `critical` (false-positive check) |
| 10 | `demo/docs-only` | Only `README.md` changes: no review is posted (no supported code to review) |
| 11 | `demo/large-pr` | 12+ separate changes across 6 files: at most 8 hunks reviewed, the largest first; the summary says how many were not reviewed |
| 12 | `demo/draft-wip` | Open as a **draft**: ignored. Click "Ready for review": reviewed |
| 13 | push a second commit to PR 1 | A new review for the new head; earlier comments are not repeated |
| 14 | GitHub App → Advanced → Redeliver a delivery | Acknowledged as a duplicate, no second review |
| 15 | react 👍/👎 on a bot comment | Within 15 minutes the dashboard's "Helpful" figure changes |
| 16 | *(optional)* stop the model API, open a PR | Three retries, then one "could not review" comment; the run shows as failed on the dashboard |
