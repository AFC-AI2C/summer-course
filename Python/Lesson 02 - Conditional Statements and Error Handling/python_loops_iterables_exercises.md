# Hands-On: Python Loops and Iterables (Advanced)

These exercises explore key differences between `for` and `while` loops, iterators, and iterable behavior in Python. You'll work with real patterns like filtering, reversing, conditional logic, and manual iteration.

---

### Exercise 1: Print Numbers with a For Loop

**Goal**: Print numbers 10 to 1 using a `for` loop.

✅ *Check*: Output should count down from 10 to 1.

---

### Exercise 2: Sum of Numbers with While Loop

**Goal**: Use a `while` loop to sum numbers from 1 to 100.

✅ *Check*: Output should be 5050.

---

### Exercise 3: Skip Multiples of 3

**Goal**: Print numbers 1 to 20, skipping multiples of 3.

✅ *Check*: 3, 6, 9, etc. should be skipped.

---

### Exercise 4: Find First Prime > 100

**Goal**: Use a `while` loop to find the first prime number greater than 100.

✅ *Check*: Should print 101.

---

### Exercise 5: Reverse a List Without Built-in Methods

**Goal**: Reverse a list using a `while` loop.

```python
original = [1, 2, 3, 4, 5]
```

✅ *Check*: Should output `[5, 4, 3, 2, 1]`.

---

### Exercise 6: Manual Iteration with Iterator

**Goal**: Use `iter()` and `next()` to manually iterate through a list.

```python
words = ["loop", "list", "range"]
```

✅ *Check*: All words should be printed in order.

---

### Exercise 7: Nested Loop with Tuple Unpacking

**Goal**: Iterate over student records with name and grades.

```python
students = [("Alice", [90, 95]), ("Bob", [85, 88])]
```

✅ *Check*: Each student should show their name and grades below.

---

### Exercise 8: Filter Even Numbers into New List

**Goal**: Use a `for` loop to create a list of even numbers from 0–20.

✅ *Check*: Should contain `[0, 2, 4, ..., 20]`.

---

### Exercise 9: While Loop with Complex Condition

**Goal**: Start at 1 and double the number until it exceeds 1000.

✅ *Check*: Should print powers of 2: 1, 2, 4, ..., up to 512.

---

### Exercise 10: For Loop with Enumerate

**Goal**: Print index and value of items in a list.

```python
colors = ["red", "green", "blue"]
```

✅ *Check*: Each color should be labeled with its index.


---

### Exercise 11: List Comprehension with Condition

**Goal**: Use a list comprehension to build a list of squares of even numbers from 1 to 20.

✅ *Check*: List should contain squares of 2, 4, 6, ..., 20.

---

### Exercise 12: Dictionary Comprehension

**Goal**: Create a dictionary where the keys are numbers 1–5 and values are their cubes.

✅ *Check*: Should print `{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}`.

---

### Exercise 13: Set Comprehension

**Goal**: Use a set comprehension to extract unique vowels from a string.

```python
text = "comprehension in python"
```

✅ *Check*: Output should be a set of vowels found in the string.

---

### Exercise 14: Generator Expression

**Goal**: Create a generator to yield the square of numbers from 1 to 10.

✅ *Check*: Each square from 1^2 to 10^2 should print.

---

### Exercise 15: Custom Generator Function

**Goal**: Write a generator that yields Fibonacci numbers up to a limit.

✅ *Check*: Should print Fibonacci numbers up to 100.
