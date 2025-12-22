# Lesson 01 - Introduction to Linux

This repository provides an overview of the **Linux Operating System**, its history, core architecture, and fundamental command-line operations used in cloud environments.


## 🎯 Lesson Objectives

* Discuss the **history and evolution** of Linux.
* Identify and explain the **core components** of the Linux architecture.
* Master **basic Linux commands** for file system navigation and management.


## 🐧 What is Linux?

Linux is a family of open-source Unix-like operating systems based on the **Linux kernel**. It is the dominant operating system for cloud infrastructure, web servers, and supercomputers.


### The Evolution of Linux

* **1969:** Unix was originally developed by Ken Thompson and Dennis Ritchie at Bell Labs.
* **1991:** Linus Torvalds, a Finnish student, began developing the Linux kernel as a free alternative to the Minix operating system.
* **Open Source:** Linux is developed under the GNU General Public License (GPL), allowing anyone to see, modify, and distribute the code.
* **Distributions (Distros):** Various versions of Linux exist to suit different needs, such as **Ubuntu, CentOS, Debian, and Red Hat Enterprise Linux (RHEL)**.


## 🏛️ Linux Architecture

The Linux system is organized into distinct layers that manage the transition from hardware to user applications.

| Layer | Function |
| --- | --- |
| **Hardware** | The physical components like CPU, RAM, and Disk. |
| **Kernel** | The core of the OS that manages hardware resources and provides services to programs. |
| **Shell** | The interface (CLI) that interprets user commands and sends them to the kernel. |
| **User Apps** | Programs like web browsers, editors, or compilers that run on top of the shell. |


## ⌨️ Fundamental Linux Commands

Linux is primarily managed through the **Command Line Interface (CLI)**. Below are the essential commands for daily operations:


### Navigation and Information

* `pwd`: Print Working Directory (shows exactly where you are).
* `ls`: List files and directories in the current location.
* `cd [path]`: Change Directory to move between folders.
* `man [command]`: Access the manual pages for a specific command.


### File and Directory Management

* `mkdir`: Create a new directory.
* `touch`: Create a new empty file.
* `cp`: Copy files or directories.
* `mv`: Move or rename files or directories.
* `rm`: Remove/delete files (use with caution).


### File Content and Editing

* `cat`: Concatenate and display the entire content of a file.
* `head` / `tail`: View the beginning or end of a file.
* `grep`: Search for specific text patterns within files.
* `nano` / `vi`: Standard text editors for modifying files directly in the terminal.


## 📂 The Linux File System

Unlike Windows, Linux uses a **hierarchical tree structure** starting from the root directory (`/`).

* Everything in Linux is treated as a **file**, including hardware devices.
* Standard directories include `/bin` (essential binaries), `/etc` (configuration files), and `/home` (user personal files).
