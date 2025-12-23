# Git – Working With Others

This repository focuses on collaborative workflows in Git, covering how to interact with remote repositories, synchronize changes, and contribute to projects using forks and pull requests.


## 🎯 Lesson Objectives

- **Push changes** from a local repository to a remote repository.
- **Pull changes** from a remote repository to a local repository.

* Discuss the concepts of **origins, forks, and upstreams**.


## 🌐 Remotes and Origins

A "remote" is a version of your project hosted on the internet or another network.

- **Cloning:** When you clone a repository, Git automatically sets up a remote named **"origin"** that points back to the source URL.
- **Management:** You can view your remotes using `git remote -v` or see detailed information with `git remote show origin`.
- **Multiple Remotes:** You can maintain multiple remotes to track different versions of a project (e.g., your own fork and the original source).


## 🔄 Synchronizing Data

Collaborating requires moving commits between your local machine and the remote server.

- **Git Push:** Uploads your local branch commits to the remote repository.
- **Git Fetch:** Downloads new data from a remote repository but does not merge it into your local work.
- **Git Pull:** A combination of `fetch` and `merge`; it downloads data and immediately tries to integrate it into your current local branch.


## 🍴 Forking and Upstreams

For open-source or shared projects, you often use a "fork-and-pull" workflow.

- **Fork:** A personal copy of someone else's project hosted on your account. This allows you to make changes without affecting the original repository.
- **Upstream:** The original repository from which you forked. You typically track the "upstream" to keep your fork updated with the latest changes.


## 📥 Pull Requests (Merge Requests)

A Pull Request (PR) is a way to notify team members that you have completed a feature and want them to review and merge your code.

- **Process:** If you have forked a repository, the original developers must "pull" from your repository to integrate your changes.
- **Collaboration:** PRs provide a platform for discussion, code review, and quality checks before code is finalized.


## 🛠️ Hands-On Exercises

- **Inspect Remotes:** Practice using `git remote` to see tracking URLs.
- **Syncing:** Perform `push` and `pull` operations with a partner or remote server.
- **Collaboration:** Fork a remote repository and submit a pull request to contribute changes.
