# Lab 5 Reflection: Static Code Analysis

### 1. What were the most critical security vulnerabilities found by Bandit, and how did you remediate them?
Bandit identified three major security vulnerabilities:
* **Command Injection (`B605` - High Severity):** Caused by executing shell commands directly with user input using `os.system`. Remediated by replacing `os.system("echo ...")` with standard Python `print()` statements.
* **Weak Cryptographic Hash (`B324` - High Severity):** Caused by using `hashlib.md5` for token generation. Remediated by upgrading the algorithm to `hashlib.sha256`.
* **SQL Injection (`B608` - Medium Severity):** Caused by constructing SQL queries using Python string formatting (`.format()`). Remediated by transitioning to parameterized SQL queries with `?` placeholders.

### 2. How did static analysis tools like Pylint and Flake8 help improve code readability and maintainability?
Pylint and Flake8 enforced strict compliance with PEP 8 standards and clean code conventions:
* They identified unused imports (`json`), preventing unnecessary memory overhead.
* They flagged non-standard comparison operations (`fat == None` vs. `fat is None`).
* They enforced standard Python naming conventions, highlighting camelCase function names (`recordMilk`, `farmerToken`) so they could be refactored into PEP 8 compliant `snake_case`.
* They caught missing module and function docstrings, which forced the addition of clear documentation for every component.

### 3. Why is static code analysis important in a production software development lifecycle (SDLC)?
Static code analysis serves as an automated code review mechanism early in the development lifecycle (DevSecOps):
* **Early Bug Detection:** Catches syntax errors, logic flaws, and potential security threats before code reaches staging or production.
* **Cost Reduction:** Fixing a security vulnerability during the development phase is significantly cheaper than patching a post-deployment breach or outage.
* **Consistency:** Ensures that large teams follow uniform formatting, naming conventions, and architectural best practices across the codebase.

### 4. What challenges did you face when raising the Pylint score above 9.5, and how did you resolve them?
The original code started with a score of `2.00/10` due to extensive style violations and lack of structure. The key challenges included:
* **Scope Warnings:** Disambiguating the global `conn` object from function parameter names to eliminate variable shadowing (`W0621`).
* **Line Length Limit Enforcement:** Wrapping lengthy SQL creation statements and queries to remain within standard line-length boundaries.
* **Docstring Requirements:** Writing detailed docstrings for the module and every function to meet Pylint's documentation standards.

Addressing these issues systematically resulted in clean execution across all three tools and achieved a Pylint score of `10.00/10`.