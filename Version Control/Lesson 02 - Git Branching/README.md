# Git Branching

This repository covers advanced Git techniques for managing code changes through branching, merging strategies, and conflict resolution.


## 🎯 Lesson Objectives

* Utilize **branching** to manage concurrent changes to a Git repository.
* Discuss different **merge strategies** and when to use them.
* Identify and **resolve merge conflicts**.


## 🌿 Branches: The Tree Structure

Repositories are structured like trees where the "trunk" is your main line of development and "branches" represent parallel lines of work.


### Why Branch?

- **Parallel Work:** Multiple team members can work on different features simultaneously without interference.
- **Safe Experimentation:** Try new ideas in a branch without breaking the working code in the main branch.
- **Protection:** Keep the `main` branch stable and deployable at all times.


### Common Branch Types

- **Main:** The stable, production-ready code.
- **Develop:** The integration branch for features.
- **Feature/Bugfix:** Temporary branches for specific tasks.
- **Release/Hotfix:** Specialized branches for preparation and emergency fixes.


## 🤝 Merging Strategies

Once work in a branch is complete, it must be integrated back into the main line using a specific strategy.

- **Fast-forward:** Applies all commits from the source branch directly onto the destination branch.
- **No-ff (--no-ff):** Creates a "merge commit," preserving the historical existence of the feature branch.
- **Squash:** Combines all commits from a branch into one single commit before merging, keeping the history clean.
- **Rebasing:** Moves or combines a sequence of commits to a new base commit, effectively "rewriting" history for a linear timeline.


## ⚡ Resolving Merge Conflicts

Conflicts occur when Git cannot automatically determine which changes to keep (usually when two people edit the same line of the same file).

### How to Handle Conflicts:

1. **Identify:** Git will mark the conflict area in your files.
2. **Read:** Look for markers like `<<<<<<< HEAD` (your changes) and `>>>>>>> [branch]` (their changes).
3. **Resolve:** Manually edit the file to the desired final state.
4. **Finalize:** Use `git add` to mark the conflict as resolved, followed by `git commit`.


## 🛠️ Hands-On Exercises

- **Hands-On #1:** Practice making branches, performing basic merges, and resolving intentional conflicts.
- **Hands-On #2:** Use visualization tools (like `tig` or VS Code extensions) to see how different merge strategies affect the commit graph.
