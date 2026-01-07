# Git Branching and Merging

## Hands-On #1: Git Branching and Merging

These exercises guide you through creating branches, merging them, resolving conflicts, and using different merge strategies.

---

### Exercise 1: Create and Switch to a Branch

**Goal**: Create a new branch named `feature-a` and switch to it.


✅ *Check*: Use `git branch` to confirm you are now on `feature-a`.

---

### Exercise 2: Make a Change in the Feature Branch

**Goal**: Edit `notes.txt` and add a line describing feature A.


✅ *Check*: Run `git log --oneline` to view the commit history.

---

### Exercise 3: Switch Back to Main and Make a Change

**Goal**: Switch to the `main` branch and make a conflicting change.


✅ *Check*: View the file with `cat notes.txt`.

---

### Exercise 4: Merge Feature Branch into Main (Expect Conflict)

**Goal**: Merge `feature-a` into `main` and resolve the conflict.


✅ *Check*: A merge conflict should occur. Open `notes.txt` and manually resolve:


Edit using your favorite text editor to combine or keep one version. Then:


---

### Exercise 5: Squash Merge a Feature Branch

**Goal**: Use `--squash` to merge and squash all commits into one.


✅ *Check*: Only one commit should appear in the history after squashing.

---

### Exercise 6: Clean Up Merged Branches

**Goal**: Delete local branches that have been merged.


✅ *Check*: Run `git branch` to confirm deletion.

## Hands-On #2: Merge Strategies

### Exercise 7: Use a Merge Strategy (`--no-ff`)

**Goal**: Create a new branch and merge with `--no-ff`.


✅ *Check*: `git log` should show a merge commit.

---

### Exercise 8: Fast-Forward Merge

**Goal**: Observe a fast-forward merge when no new commits exist on main.


✅ *Check*: Run `git log --oneline` — no merge commit is created.

---

### Exercise 9: Rebase a Feature Branch

**Goal**: Rebase a feature branch onto the latest main branch.


✅ *Check*: The commit from `rebase-demo` will now appear after the `main` commit as if made later.

---

### Exercise 10: Squash Multiple Commits into One

**Goal**: Squash multiple commits into one before merging.


✅ *Check*: `git log` will show a single commit from the squash.

---

### Exercise 11: Rebase vs Merge – Compare Histories

**Goal**: Compare merge and rebase history using two branches.


✅ *Check*: Use `git log --graph --oneline --all` to visually compare linear (rebase) vs. branched (merge) history.
