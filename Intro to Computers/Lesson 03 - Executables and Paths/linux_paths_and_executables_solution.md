# Linux Paths and Executables – Instructor Answers

This document contains suggested answers and explanations for the exercises.

---

## Part 1 – Exploring Linux Paths

### Exercise 1 Answers

- The number of directories varies by system, but typically includes `/usr/bin`, `/bin`, `/usr/local/bin`, and user-specific directories.
- Order matters because the OS executes the first matching executable it finds.
- System tools are usually located in `/bin` and `/usr/bin`.

---

### Exercise 2 Answers

- `ls` typically resolves to `/bin/ls` or `/usr/bin/ls`.
- `echo` may resolve to `/bin/echo` or be a shell builtin.
- `python` resolves to whichever Python executable appears first on PATH.
- Executables are distributed across multiple directories.

---

### Exercise 3 Answers

- The error is usually `command not found`.
- The current directory is not searched by default, and the script’s directory is not on PATH.

---

### Exercise 4 Answers

- `./` explicitly tells the OS to look in the current directory.
- It bypasses PATH searching by providing a relative path.

---

## Part 2 – PATH Order and Precedence

### Exercise 5 Answers

- The version in the directory listed first in PATH runs.
- PATH order determines precedence when multiple executables share a name.

---

## Part 3 – Environment Variables

### Exercise 6 Answers

- Common variables include `HOME`, `USER`, `SHELL`, and `PWD`.
- Variables like `PATH`, `LD_LIBRARY_PATH`, and `PYTHONPATH` affect execution.

---

### Exercise 7 Answers

- PATH changes are session-scoped and reset when the shell exits.
- Permanent changes belong in files like `.bashrc`, `.profile`, or `.zshrc`.

---

## Part 4 – Virtual Environments and PATH

### Exercise 8 Answers

- `venv/bin` contains `python`, `pip`, and activation scripts.
- These ensure isolation from system-wide packages.

---

### Exercise 9 Answers

- The virtual environment’s `bin` directory is prepended to PATH.
- `python` resolves to the virtual environment interpreter.

---

### Exercise 10 Answers

- PATH returns to its original state.
- Confusion arises when users don’t realize which interpreter is active.

---

## Part 5 – Reflection Answers

1. Searching the current directory by default would be a security risk.
2. Malicious executables could override trusted system commands.
3. `python -m venv` uses the first `python` found on PATH to create the environment.

