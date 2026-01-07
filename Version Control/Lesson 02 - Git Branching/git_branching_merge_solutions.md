# Git Branching and Merging

## Hands-On #1: Git Branching and Merging

These exercises guide you through creating branches, merging them, resolving conflicts, and using different merge strategies.

---

### Exercise 1: Create and Switch to a Branch

**Goal**: Create a new branch named `feature-a` and switch to it.

```bash
git checkout -b feature-a
```

✅ *Check*: Use `git branch` to confirm you are now on `feature-a`.

---

### Exercise 2: Make a Change in the Feature Branch

**Goal**: Edit `notes.txt` and add a line describing feature A.

```bash
echo "This is Feature A" >> notes.txt
git add notes.txt
git commit -m "Add Feature A line to notes.txt"
```

✅ *Check*: Run `git log --oneline` to view the commit history.

---

### Exercise 3: Switch Back to Main and Make a Change

**Goal**: Switch to the `main` branch and make a conflicting change.

```bash
git checkout main
echo "This is Main Line" >> notes.txt
git add notes.txt
git commit -m "Add Main Line to notes.txt"
```

✅ *Check*: View the file with `cat notes.txt`.

---

### Exercise 4: Merge Feature Branch into Main (Expect Conflict)

**Goal**: Merge `feature-a` into `main` and resolve the conflict.

```bash
git merge feature-a
```

✅ *Check*: A merge conflict should occur. Open `notes.txt` and manually resolve:

```
<<<<<<< HEAD
This is Main Line
=======
This is Feature A
>>>>>>> feature-a
```

Edit using your favorite text editor to combine or keep one version. Then:

```bash
git add notes.txt
git commit
```

---

### Exercise 5: Squash Merge a Feature Branch

**Goal**: Use `--squash` to merge and squash all commits into one.

```bash
git checkout -b feature-c
echo "Squash this feature" > squash.txt
git add squash.txt
git commit -m "Add squash feature"

git checkout main
git merge --squash feature-c
git commit -m "Squashed feature-c changes"
```

✅ *Check*: Only one commit should appear in the history after squashing.

---

### Exercise 6: Clean Up Merged Branches

**Goal**: Delete local branches that have been merged.

```bash
git branch --merged
git branch -d feature-a
git branch -d feature-b
git branch -d feature-c
```

✅ *Check*: Run `git branch` to confirm deletion.

## Hands-On #2: Merge Strategies

### Exercise 7: Use a Merge Strategy (`--no-ff`)

**Goal**: Create a new branch and merge with `--no-ff`.

```bash
git checkout -b feature-b
echo "Another feature" >> newfile.txt
git add newfile.txt
git commit -m "Add new feature file"

git checkout main
git merge --no-ff feature-b -m "Merge feature-b with no fast-forward"
```

✅ *Check*: `git log` should show a merge commit.

---

### Exercise 8: Fast-Forward Merge

**Goal**: Observe a fast-forward merge when no new commits exist on main.

```bash
git checkout -b fast-forward-demo
echo "Fast forward example" > ff.txt
git add ff.txt
git commit -m "Add fast forward example"

git checkout main
git merge fast-forward-demo
```

✅ *Check*: Run `git log --oneline` — no merge commit is created.

---

### Exercise 9: Rebase a Feature Branch

**Goal**: Rebase a feature branch onto the latest main branch.

```bash
git checkout -b rebase-demo
echo "Line for rebase demo" > rebase.txt
git add rebase.txt
git commit -m "Initial rebase commit"

git checkout main
echo "Main branch update" > common.txt
git add common.txt
git commit -m "Update from main"

git checkout rebase-demo
git rebase main
```

✅ *Check*: The commit from `rebase-demo` will now appear after the `main` commit as if made later.

---

### Exercise 10: Squash Multiple Commits into One

**Goal**: Squash multiple commits into one before merging.

```bash
git checkout -b squash-demo
echo "Line 1" > squash.txt
git add squash.txt
git commit -m "Add line 1"

echo "Line 2" >> squash.txt
git add squash.txt
git commit -m "Add line 2"

git checkout main
git merge --squash squash-demo
git commit -m "Squashed all changes from squash-demo"
```

✅ *Check*: `git log` will show a single commit from the squash.

---

### Exercise 11: Rebase vs Merge – Compare Histories

**Goal**: Compare merge and rebase history using two branches.

```bash
# Create one branch and make commits
git checkout -b merge-vs-rebase
echo "A" > file.txt
git add file.txt
git commit -m "Commit A"

echo "B" >> file.txt
git add file.txt
git commit -m "Commit B"

# Simulate upstream changes
git checkout main
echo "Main update" > main.txt
git add main.txt
git commit -m "Update main"

# Now try merge
git checkout merge-vs-rebase
git merge main   # OR git rebase main
```

✅ *Check*: Use `git log --graph --oneline --all` to visually compare linear (rebase) vs. branched (merge) history.
