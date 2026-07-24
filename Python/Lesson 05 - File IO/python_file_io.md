# Hands-On Exercises: Python `os` and `os.path` Modules

This guide introduces basic file and directory operations using Python's `os` and `pathlib.Path` modules. It mirrors Linux shell operations you may already know, using Python code to accomplish the same tasks.

---
## Hands-On #1

### Exercise 0: Environment Set-up

Clone the repository at `https://github.com/shafe123/AI2C-python-files.git`.

```bash
git clone https://github.com/shafe123/AI2C-python-files.git
```

### Exercise 1: Get Current Working Directory

**Goal**: Use Python to print the current working directory.


✅ *Check*: Run the script and confirm it prints the full path of your working directory.
```python
import os
os.getcwd()
```
---

### Exercise 2: Change Directory

**Goal**: Change into a directory named `projects`.

✅ *Check*: Ensure that you are now in the `projects` directory. Create it first if it doesn't exist.
```python
os.mkdir("projects")
os.chdir("projects")
os.getcwd()
```
---

### Exercise 3: List Directory Contents

**Goal**: List all files and directories in the current directory.

✅ *Check*: Compare the output to the `ls` command in your terminal.
```python
os.listdir()
os.system('ls')     #run from inside wsl, not powershell
```
---

### Exercise 4: Create a Directory

**Goal**: Create a directory named `data`.

✅ *Check*: Verify the directory exists using `pathlib` or by checking in your terminal.
```python
import pathlib
p = pathlib.Path.cwd() / "data"
p.mkdir(exist_ok=True)
p2 = pathlib.Path.cwd() / "data" / "file.txt"
p2.touch(exist_ok=True)
os.system("ls -R")
```
---

### Exercise 5: Create Nested Directories

**Goal**: Create nested directories `a/b/c` in one call.

✅ *Check*: Use `pathlib` to confirm creation.
```python
p3 = pathlib.Path.cwd() / "a" / "b" / "c"
p3.mkdir(parents=True, exist_ok=True)
os.system("ls -R")
```
---

### Exercise 6: Remove a File

**Goal**: Delete a file named `temp.txt`.

✅ *Check*: Use `pathlib` to validate that the file no longer exists.
```python
p0 = pathlib.Path.cwd()
p4 = p0 / "temp.txt"
p4.touch()
#or
pathlib.Path.cwd().joinpath("temp.txt").touch()
print(*pathlib.Path(".").iterdir())     #os.system("ls")
pathlib.Path.cwd().joinpath("temp.txt").unlink()
print(*pathlib.Path(".").iterdir())     #os.system("ls")    
#print(*pathlib.Path(".").glob("*"))
```
---

### Exercise 7: Remove an Empty Directory

**Goal**: Delete an empty directory named `old_data`.

✅ *Check*: If the directory is not empty, this will raise an error. Try clearing it first.
```python
pathlib.Path(".").joinpath("old_data").mkdir()
print(*pathlib.Path(".").iterdir())
pathlib.Path(".").joinpath("old_data").rmdir()
print(*pathlib.Path(".").iterdir())

pathlib.Path(".").joinpath("old_data").mkdir(exist_ok=True)
pathlib.Path(".").joinpath("old_data","contents.txt").touch()
print(*pathlib.Path("old_data").glob("*"))
#print(*pathlib.Path(".").glob("**/*"))  #print(*pathlib.Path(".").rglob("*"))
[f.unlink() for f in pathlib.Path("old_data").glob("*") if f.is_file()]
#[f.unlink() for f in pathlib.Path(".").joinpath("old_data").glob("*")]
pathlib.Path(".").joinpath("old_data").rmdir()
print(*pathlib.Path(".").iterdir())
```
---

### Exercise 8: Rename a File

**Goal**: Rename `example.txt` to `renamed_example.txt`.

✅ *Check*: Confirm the new name exists and the old one doesn't.
```python
p5 = pathlib.Path("example.txt")
p5.touch(exist_ok=True)
print(*pathlib.Path(".").glob("*"))
p5.rename(pathlib.Path("renamed_example.txt"))
print(*pathlib.Path(".").glob("*"))
```
---

### Exercise 9: Check File or Directory Type

**Goal**: Determine whether `target` is a file or directory.

✅ *Check*: Create a test file or directory and run the script to see the correct output.
```python
pathlib.Path("target").mkdir()
print(pathlib.Path("target").is_dir())
pathlib.Path("target").rmdir()
pathlib.Path("target").touch()
print(pathlib.Path("target").is_file())
pathlib.Path("target").unlink()
```
## Hands-On #2

This series of exercises helps you understand how to create, read, append, and handle files in Python using both built-in `open()` and the `pathlib` module.

---

### Exercise 10: Create and Write to a File

**Goal**: Create a file called `log.txt` and write a single line to it.

✅ *Check*: Open `log.txt` and verify the line was written.

```python
os.system("echo '24 Jul 2026 06:27:00 hello' > log.txt")
os.system("cat log.txt")
```
---

### Exercise 11: Read the File

**Goal**: Read and print the contents of `log.txt`.

✅ *Check*: Ensure the output matches the line you wrote previously.
```python
with open('log.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="")

print()
```
---

### Exercise 12: Append a Line to the File

**Goal**: Add another line to `log.txt` without removing the original content.

✅ *Check*: Re-read the file and confirm both lines are present.
```python
with open('log.txt', 'a') as f:
    f.write("24 July 2026 06:33:00 hello")

with open('log.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
---

### Exercise 13: Write Multiple Lines

**Goal**: Write multiple lines to a new file using a list.

✅ *Check*: Open `multi.txt` and confirm all three lines are present.
```python
with open('multi.txt', 'w') as f:
    lines = ["24 July 06:38:00\n","24 July 06:38:01\n","24 July 06:38:02\n"]
    f.writelines(lines)
os.system("cat multi.txt")
with open('multi.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
```
---

### Exercise 14: Read a File Line by Line

**Goal**: Read `multi.txt` and print each line one at a time.

✅ *Check*: Each line should print without extra blank lines.
```python
with open('multi.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end="")
```
---

### Exercise 15: Count Lines in a File

**Goal**: Count how many lines are in `multi.txt`.

✅ *Check*: The count should be 3 if using the previous file.
```python
with open('multi.txt', 'r') as f:
    lines = f.readlines()
    num_lines = 0
    for line in lines:
        num_lines += 1
        print(line, end="")
print(f"Number of lines: {num_lines}")
os.system("cat multi.txt | wc -l")
```
---

### Exercise 16: Read a File Safely

**Goal**: Try reading a file that may not exist and handle the error.

✅ *Check*: Make sure the program doesn't crash if the file is missing.
```python
#handle errors silently
for filename in ["multi.txt", "missing"]:
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except:
        pass

#announce errors
for filename in ["multi.txt", "missing"]:
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print("FileNotFoundError: ", e)
```
---

### Exercise 17: Use `pathlib` to Read/Write

**Goal**: Use `pathlib.Path` instead of `open()`.

✅ *Check*: The file should contain the message, and it should print to the screen.
```python
with pathlib.Path("multi.txt").open(mode='r') as f:
    print(f.read())
```

## Stretch Goals

**Goal**: Print the size and last modified time of `data.csv`.

✅ *Check*: Match file size with `ls -l` and modification time with `stat` in the terminal.
```python
my_path = pathlib.Path("data.csv")
my_path.touch()
my_path.stat()
print(pathlib.Path("data.csv").stat().st_mtime)
os.system("stat -c %.Y data.csv")        #mtime in seconds since epoch
print(pathlib.Path("data.csv").stat().st_size)
os.system("stat -c %s data.csv")        #size
#print(*pathlib.Path(".").glob("*"))
os.system("ls -l data.csv")

#os.system("stat data.csv")
#os.system("ls -l --time=modification --s data.csv")
#os.system("ls -l --time=modification --size data.csv")
#os.system("ls -l --time=mtime --s data.csv")
#os.system("ls --time=mtime --size data.csv")
```
**Goal**: Gain a deeper understanding of os and Pathlib.

Create a short listing of the overlapping features of os and Pathlib.  Why might one prefer one module over the other?


```
Operation,                  os / os.path,                           pathlib
Get Current Directory,      os.getcwd(),                            Path.cwd()
Join Paths,                 "os.path.join(a, b)",                   Path(a) / b or Path(a).joinpath(b)
Check Existence,            os.path.exists(path),                   Path(path).exists()
Create Directory,           os.mkdir(path) / os.makedirs(),         Path(path).mkdir(parents=True)
Remove File,                os.remove(path) / os.unlink(),          Path(path).unlink()
Remove Directory,           os.rmdir(path),                         Path(path).rmdir()
List Directory Contents,    os.listdir(path),                       [p for p in Path(path).iterdir()]
Find Files with Glob,       "glob.glob(""*.py"") (via glob module)","Path(""."").glob(""*.py"")"
Get File Stats (Size/Time), os.stat(path),                          Path(path).stat()
Check File/Dir Type,        os.path.isfile(path),                   Path(path).is_file()


Why Prefer pathlib over os?
pathlib (introduced in Python 3.4) is generally the modern standard for path manipulation.

Object-Oriented Design: pathlib treats paths as objects rather than simple string representations. This allows method chaining (e.g., Path.cwd().joinpath("data").mkdir()).

Operator Overloading: Joining paths with the / operator (path / "file.txt") is cleaner and less error-prone than os.path.join().

Consolidated Functionality: pathlib combines utilities scattered across os, os.path, glob, and shutil into a single intuitive API.

Read/Write Convenience: pathlib provides handy built-in methods like .read_text(), .write_text(), .read_bytes(), and .write_bytes() to quickly read or write files without explicit with open(...) blocks.




Why Prefer os over pathlib?
While pathlib is preferred for path arithmetic and standard file operations, os remains essential in specific scenarios:

Lower-Level System Calls: os provides process management (os.fork(), os.exec()), environment variable access (os.environ), and lower-level file descriptor operations (os.open(), os.read()).

Performance-Critical Code: Converting string paths to Path objects adds a slight overhead. In tight loops or performance-sensitive file operations, raw string manipulations using os.path can be faster.

Legacy Codebases: Older Python projects and legacy libraries frequently pass raw strings, making os or os.path more immediately compatible without needing str(path) conversions.
```
