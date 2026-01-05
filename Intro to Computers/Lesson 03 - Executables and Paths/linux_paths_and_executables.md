# Linux Paths and Executables – Exercises

This worksheet explores how Linux locates and executes programs using paths, executables, and environment variables.

---

## Part 1 – Exploring Linux Paths

### Exercise 1: What Is on Your PATH?

1. Display your PATH variable

**Questions:**
- How many directories are on your PATH?
- Why does the order matter?
- Which directories likely contain system tools?

---

### Exercise 2: Finding Executables

- Where is the `ls` command on your system?
- Where is `python`?
- Where is `which`?

**Questions:**
- What full path does each command resolve to?
- Are all executables located in the same directory?

---

### Exercise 3: What Happens If It’s Not on PATH?

1. Create a test directory and script.
2. Attempt to run the script by name.
3. Run your script without any directory information:  no `.` or `test_folder/script`

**Questions:**
- What error occurs?
- Why can’t the system find the script?

---

### Exercise 4: Running Local Executables

Run the script using `./`.

**Questions:**
- Why does this work?
- What does `./` explicitly mean?

---

## Part 2 – PATH Order and Precedence

### Exercise 5: PATH Search Order

Copy your test script into another folder and modify your PATH to include both folders.  Run the script again without any directory information.

**Questions:**
- Which version runs first?
- How does PATH order affect execution?

---

## Part 3 – Environment Variables

### Exercise 6: Inspecting Environment Variables

Inspect your environment variables.

**Questions:**
- Name three environment variables besides PATH.
- Which might affect program execution?

---

### Exercise 7: Temporary vs Permanent PATH Changes

Modify PATH in one terminal and compare behavior in a new terminal.

**Questions:**
- Why don’t PATH changes persist?
- Where would permanent changes be stored?

---

## Part 4 – Virtual Environments and PATH

### Exercise 8: Creating a Virtual Environment

Create a virtual environment and inspect its contents.

**Questions:**
- What executables appear in `venv/bin`?
- Why are these included?

---

### Exercise 9: Activating the Virtual Environment

Activate the environment and inspect PATH.

**Questions:**
- What changes in PATH?
- Why does `python` resolve differently?

---

### Exercise 10: Deactivation and Consequences

Deactivate the environment.

**Questions:**
- What changes back?
- Why can virtual environments cause confusion?

---

## Part 5 – Reflection

Answer in complete sentences:

1. Why doesn’t Linux search the current directory by default?
2. How can PATH ordering create security risks?
3. Why does `python -m venv` depend on PATH ordering?

