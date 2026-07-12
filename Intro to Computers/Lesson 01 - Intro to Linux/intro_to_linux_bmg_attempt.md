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
    - [Exercise 7: SSH - Remote Access](#exercise-7-ssh---remote-access)
    - [Exercise 8: Redirection Operators](#exercise-8-redirection-operators)
  - [Stretch Goals:](#stretch-goals)

## Hands-On #1

Welcome! These exercises are designed to help you get comfortable with basic Linux file system commands.

### Exercise 0: Clone the starting repository

1. Open WSL
2. Run the following command to clone the initial file structure
    ```bash
    cd~
    git clone https://github.com/shafe123/AI2C-IntroToLinux.git
    ```
3. Verify the folder was cloned
```bash
ls
```   
4. Change directory into the newly cloned folder
```bash
cd ~/AI2C-IntroToLinux/
```   

### Exercise 1: Navigation

1. List all files and directories in the current folder.
```bash
ls
```

2. Change directory into `notes`, then list the files.
```bash
cd ./notes
ls
```   

3. Go back to the parent directory.
```bash
cd ..
```
   
### Exercise 2: File Viewing

1. View the contents of `file1.txt`.
```bash
cat file1.txt
```   

2. Use `less` or `more` to view `file2.txt`.
```bash
less file2.txt
more file2.txt
```

### Exercise 3: File Management

1. Copy `file2.txt` into the `docs` directory.
```bash
cp file2.txt ./docs/
```   

2. Move `file1.txt` into the `notes` directory and rename it as file3.
```bash
mv file1.txt ./notes/file3.txt
```   
   
3. Create a new file named `newfile.txt`.
```bash
touch newfile.txt
```   
   
4. Delete `newfile.txt`.
```bash
rm newfile.txt
```   
   

### Exercise 4: Permissions and Execution

1. View permissions of `scripts/hello.sh`.
```bash
ls -l scripts/hello.sh

stat scripts/hello.sh
```   
   
2. Make `hello.sh` executable and run it.
```bash
stat scripts/hello.sh
chmod u+x scripts/hello.sh
ls -l scripts/hello.sh

chmod 0744 scripts/hello.sh
ls -l scripts/hello.sh
```      

## Hands-On #2

These exercises are designed to help you practice using tools like `grep`, `wc`, `ssh`, and redirection operators (`>`, `>>`, `<`, `|`).

---

### Exercise 5: GREP - Search Text

1. Search for the word "Linux" in `file1.txt`.
```bash
cp ./notes/file3.txt file1.txt
grep Linux file1.txt
```   

2. Search for lines **not** containing "Linux".
```bash
grep -v Linux file1.txt
```      

3. Search recursively in all `.txt` files under the current directory.
```bash
grep -r Linux .

grep -r Linux
```

4. Find lines starting with the word "Note".
```bash
grep -r ^Note .

grep -r ^Note
```     

---

### Exercise 6: WC - Word/Line/Character Count

1. Count the number of lines in `file2.txt`.
```bash
wc file2.txt
```   

2. Count the number of words and characters in `docs/doc1.txt`.
```bash
wc docs/doc1.txt
```   
   
3. Get a summary for all `.txt` files.
```bash
wc *.txt

wc */*.txt
```   
   
---

### Exercise 7: SSH - Remote Access

1. Connect to the server that your instructor provided with the correct credentials.
```bash
ssh user2@46.225.20.198
yes
```   
  

2. Run a remote command (e.g., list home directory files).
```bash
ls ~
```   
  

3. Copy a local file to the remote server.
```bash
echo https://www.cartalk.com/content/lame-jokes-2 > LameJokesFromCarTalk
scp LameJokesFromCarTalk user2@46.225.20.
198:/srv/class_share
```   


4. Leave a message for your peers!
```bash
ssh user2@46.225.20.198
echo Non Impediti Ratione Cogitationis > Motto_of_Tom.txt && echo Unencumbered by the thought process. >> Motto_of_Tom.txt
```   
   
---

### Exercise 8: Redirection Operators

1. Redirect the output of `ls` into a file.
```bash
ls > ls_output.txt
```      

2. Append output to an existing file using echo.
```bash
echo my output >> ls_output.txt
```      

3. Use input redirection to provide data to a command.
```bash
wc < file1.txt
wc file1.txt

echo file1.txt > data_for_my_command.txt
cat $(< data_for_my_command.txt)

ls | grep $(< data_for_my_command.txt)

echo .txt > more_data_for_a_command.txt
ls | grep $(< more_data_for_a_command.txt)
```      

4. Chain commands with a pipe: count the number of files containing "Note".
```bash
grep -Rl Note | wc
```      

5. Combine multiple operators: search a file and save results.
```bash
grep -R Linux | grep -v Linux.git > results_about_Linux.txt
```     

---

## Stretch Goals:

**Goal**:  Try to determine how many text files there are in the original repository.

**Goal**:  Which file in the repository `https://github.com/shafe123/AI2C-LinuxLarge.git` has a hidden message? (hint: you can do this just with grep)

