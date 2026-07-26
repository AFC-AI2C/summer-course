# Git Branching and Merging
- [Git Branching and Merging](#git-branching-and-merging)
  - [Hands-On #1: Git Branching and Merging](#hands-on-1-git-branching-and-merging)
    - [Exercise 1: Create and Switch to a Branch](#exercise-1-create-and-switch-to-a-branch)
    - [Exercise 2: Make a Change in the Feature Branch](#exercise-2-make-a-change-in-the-feature-branch)
    - [Exercise 3: Switch Back to Main and Make a Change](#exercise-3-switch-back-to-main-and-make-a-change)
    - [Exercise 4: Merge Feature Branch into Main (Expect Conflict)](#exercise-4-merge-feature-branch-into-main-expect-conflict)
    - [Exercise 5: Squash Merge a Feature Branch](#exercise-5-squash-merge-a-feature-branch)
    - [Exercise 6: Clean Up Merged Branches](#exercise-6-clean-up-merged-branches)
  - [Hands-On #2: Merge Strategies](#hands-on-2-merge-strategies)
    - [Exercise 7: Use a Merge Strategy (`--no-ff`)](#exercise-7-use-a-merge-strategy---no-ff)
    - [Exercise 8: Fast-Forward Merge](#exercise-8-fast-forward-merge)
    - [Exercise 9: Rebase a Feature Branch](#exercise-9-rebase-a-feature-branch)
    - [Exercise 10: Squash Multiple Commits into One](#exercise-10-squash-multiple-commits-into-one)
    - [Exercise 11: Rebase vs Merge – Compare Histories](#exercise-11-rebase-vs-merge--compare-histories)

## Hands-On #1: Git Branching and Merging

These exercises guide you through creating branches, merging them, resolving conflicts, and using different merge strategies.

---

### Exercise 1: Create and Switch to a Branch

**Goal**: Create a new branch named `feature-a` and switch to it.


✅ *Check*: Use `git branch` to confirm you are now on `feature-a`.
```bash
git switch -c feature-a
git branch
```
---

### Exercise 2: Make a Change in the Feature Branch

**Goal**: Edit `notes.txt` and add a line describing feature A.


✅ *Check*: Run `git log --oneline` to view the commit history.
```bash
echo "create a mock feature" > "notes.txt"
git add .
git commit -m "create feature-a branch with a mock feature in notes.txt"
git log --oneline
```
---

### Exercise 3: Switch Back to Main and Make a Change

**Goal**: Switch to the `main` branch and make a conflicting change.


✅ *Check*: View the file with `cat notes.txt`.
```bash
git checkout main
<<<<<<< HEAD
echo "create a different mock feature" > "notes.txt"
cat notes.txt
git add .
git commit -m "update main with a different mock feature in notes.txt"
=======
echo "create a difference mock feature" > "notes.txt"
cat notes.txt
>>>>>>> 5fa716c (create feature-a branch with a mock feature in notes.txt)
```
---

### Exercise 4: Merge Feature Branch into Main (Expect Conflict)

**Goal**: Merge `feature-a` into `main` and resolve the conflict.


✅ *Check*: A merge conflict should occur. Open `notes.txt` and manually resolve:


Edit using your favorite text editor to combine or keep one version.

```bash
git merge feature-a
```
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
