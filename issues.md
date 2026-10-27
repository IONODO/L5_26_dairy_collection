# Static Code Analysis Issues — Dairy Milk Collection Ledger

| Issue Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- |
| **High Security (Bandit B605)** | 31 | Starting a process with a shell (`os.system`) creates a command injection vulnerability. | Replace `os.system` with a safe Python `print` statement or a non-shell execution method. |
| **High Security (Bandit B324)** | 16 | Use of weak MD5 hash for security in `farmerToken`. | Replace MD5 with a secure cryptographic hashing algorithm such as SHA-256 (`hashlib.sha256`). |
| **Medium Security (Bandit B608)** | 11 | Hardcoded SQL expressions via string formatting (`.format()`) introduce a SQL injection vector. | Use parameterized queries with `?` placeholders in SQLite. |
| **Style / Code Quality (Flake8 E711)** | 36 | Comparison to `None` using `==` operator instead of the identity operator. | Change `fat == None` to `fat is None`. |
| **Code Quality (Flake8 F401)** | 2 | Unused import `json`. | Remove the unused `json` import statement. |