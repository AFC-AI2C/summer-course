# Lesson 03 - Executables and Paths

This repository covers the fundamental mechanics of how operating systems locate and run programs, focusing on the relationship between binary files, the environment, and the system path.


## 🎯 Lesson Objectives

* Understand what an **executable file** is.
* Explain how the operating system uses the **PATH environment variable** to find programs.
* Learn to manage and modify your **system environment**.


## 🏃 What is an Executable?

An executable is a file that contains a set of instructions that a computer can execute directly.


### Types of Executables

* **Compiled Binaries:** Programs written in languages like C++ or Go that are converted into machine code (e.g., `.exe` in Windows, or extensionless files in Linux).
* **Scripts:** Human-readable text files that require an interpreter to run, such as Python (`.py`) or Bash (`.sh`).


## 🗺️ The PATH Environment Variable

The `PATH` is an environment variable that tells the operating system which directories to search for executable files in response to a command.


### How it Works:

1. When you type a command (like `ls` or `python`), the system doesn't know where it is located initially.
2. The system looks through each directory listed in the `PATH` variable, from left to right.
3. The first instance of the executable found is the one that gets executed.
4. If it isn't found in any of those folders, you receive a "command not found" error.


## 💻 Essential Path Commands

Managing your environment requires knowing how to view and locate your tools.

| Task | Linux/macOS Command | Windows (PowerShell) Command |
| --- | --- | --- |
| **View PATH** | `echo $PATH` | `$env:PATH` |
| **Locate Program** | `which [program]` | `where.exe [program]` |
| **Run local file** | `./[filename]` | `.\[filename]` |

> **Note:** To run a program in your current folder that isn't in your PATH, you must explicitly tell the system to look in the current directory using `./`.


## 🛠️ Modifying the Environment

Sometimes you need to add new software to your PATH so it can be run from any terminal window.

* **Temporary Change (Current Session):** `export PATH=$PATH:/new/directory`.
* **Permanent Change:** Add the export command to your shell configuration file (like `.bashrc` or `.zshrc`).


## 🧩 Shared Libraries

Many executables rely on **shared libraries**—code that is shared across multiple programs to save space and memory.

* **Linux:** Uses `.so` (Shared Object) files.
* **Windows:** Uses `.dll` (Dynamic Link Library) files.
