# Intro to Version Control

This repository introduces the core concepts of **Version Control Systems (VCS)**, with a specific focus on **Git**, the industry-standard tool for tracking changes in source code during software development.


## 🎯 Lesson Objectives

* Discuss basic **Git concepts**.
* Use basic Git commands to **manage a local repository**.
* Use basic Git commands to **view history and changes**.


## 🌳 What is Git?

Git is a distributed version control system created by **Linus Torvalds** in 2005. It is currently used by approximately **93% of developers** worldwide.


### Why use Git?

- **Safety:** In case of "fire" (system failure or bad code), you can revert to a previous working state.
- **Automation:** Command-line usage allows for scripting and chaining with other utilities.
- **Universal:** Most servers are terminal-only, making CLI Git skills essential for professional environments.


## ⌨️ Fundamental Git Commands

### Managing a Local Repository

| Task | Command | Description |
| --- | --- | --- |
| **Initialize** | `git init` | Create a new local Git repository.
| **Add** | `git add <file>` | Move changes from the working directory to the staging area.
| **Commit** | `git commit -m "msg"` | Save your staged snapshot to the project history.
| **Status** | `git status` | View the state of the working directory and staging area.


### Viewing History and Changes

- **`git log`**: Show the full commit history.
- **`git log --oneline`**: Display a condensed, one-line version of the history.
- **`git diff`**: Show changes that have not yet been staged.
- **`git diff --cached`**: Show changes that are staged and ready for commit.


## 🔍 Reading Diffs

Git uses "diffs" to show what has changed between files or commits:

* Lines starting with **`-` (minus)**: Represent the original state (File A).
* Lines starting with **`+` (plus)**: Represent the new state (File B).


## 💡 Pro Tip: Command Line Power

While many UIs exist for Git, the **Command Line Interface (CLI)** is preferred because:

1. Not every UI exposes all available commands.
2. It allows for advanced **automation and scripting**.
3. It is often the only interface available on remote servers.
