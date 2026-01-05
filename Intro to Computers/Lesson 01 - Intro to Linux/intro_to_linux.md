# Intro to Linux
- [Intro to Linux](#intro-to-linux)
  - [Hands-On #1](#hands-on-1)
    - [Exercise 0: Clone the starting repository](#exercise-0-clone-the-starting-repository)
    - [Exercise 1: Navigation](#exercise-1-navigation)
    - [Exercise 2: File Viewing](#exercise-2-file-viewing)
    - [Exercise 3: File Management](#exercise-3-file-management)
    - [Exercise 4: Permissions and Execution](#exercise-4-permissions-and-execution)
  - [Hands-On #2](#hands-on-2)
    - [Exercise 5: GREP - Search Text](#exercise-5-grep---search-text)
    - [Exercise 6: WC - Word/Line/Character Count](#exercise-6-wc---wordlinecharacter-count)
    - [Exercise 7: SSH - Remote Access (Assumes you have SSH access to a server)](#exercise-7-ssh---remote-access-assumes-you-have-ssh-access-to-a-server)
    - [Exercise 8: Redirection Operators](#exercise-8-redirection-operators)
  - [Stretch Goals:](#stretch-goals)

## Hands-On #1

Welcome! These exercises are designed to help you get comfortable with basic Linux file system commands.

### Exercise 0: Clone the starting repository

1. Open WSL
2. Run the following command to clone the initial file structure
    ```bash
    git clone https://github.com/shafe123/AI2C-IntroToLinux.git
    ```
3. Verify the folder was cloned
   
4. Change directory into the newly cloned folder
   

### Exercise 1: Navigation

1. List all files and directories in the current folder.
   

2. Change directory into `notes`, then list the files.
   

3. Go back to the parent directory.
   

### Exercise 2: File Viewing

1. View the contents of `file1.txt`.
   

2. Use `less` or `more` to view `file2.txt`.

### Exercise 3: File Management

1. Copy `file2.txt` into the `docs` directory.
   

2. Move `file1.txt` into the `notes` directory and rename it as file3.
   

3. Create a new file named `newfile.txt`.
   

4. Delete `newfile.txt`.
   

### Exercise 4: Permissions and Execution

1. View permissions of `scripts/hello.sh`.
   

2. Make `hello.sh` executable and run it.
   

## Hands-On #2

These exercises are designed to help you practice using tools like `grep`, `wc`, `ssh`, and redirection operators (`>`, `>>`, `<`, `|`).

---

### Exercise 5: GREP - Search Text

1. Search for the word "Linux" in `file1.txt`.
   

2. Search for lines **not** containing "Linux".
   

3. Search recursively in all `.txt` files under the current directory.
   

4. Find lines starting with the word "Note".
   

---

### Exercise 6: WC - Word/Line/Character Count

1. Count the number of lines in `file2.txt`.
   

2. Count the number of words and characters in `docs/doc1.txt`.
   

3. Get a summary for all `.txt` files.
   
---

### Exercise 7: SSH - Remote Access (Assumes you have SSH access to a server)



1. Connect to a remote server.
   

2. Run a remote command (e.g., list home directory files).
   

3. Copy a local file to the remote server.
   

---

### Exercise 8: Redirection Operators

1. Redirect the output of `ls` into a file.
   

2. Append output to an existing file.
   

3. Use input redirection to provide data to a command.
   

4. Chain commands with a pipe: count the number of files containing "Note".
   

5. Combine multiple operators: search a file and save results.
   

---

## Stretch Goals:

**Goal**:  Try to determine how many text files there are in the original repository.

**Goal**:  Which file in the repository `https://github.com/shafe123/AI2C-LinuxLarge.git` has a hidden message? (hint: you can do this just with grep)

