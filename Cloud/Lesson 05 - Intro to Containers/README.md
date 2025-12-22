# Lesson 05 - Cloud Computing: Containers and Images

This repository provides an overview of containerization technology, specifically focusing on the relationship between images and containers, and the benefits they bring to modern software deployment. 

## 🎯 Lesson Objectives

* Discuss the fundamental concepts of **containers and images**. 
* Explain the **benefits** of using containers in software development. 
* Differentiate between **containers and virtual machines**. 


## 📦 What is a Container?

A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. 

### Key Characteristics

- **Lightweight:** Containers share the machine’s OS system kernel and therefore do not require an OS per application. 
- **Standard:** Docker created the industry standard for containers, so they could be portable anywhere. 
- **Secure:** Applications are safer in containers and Docker provides the strongest default isolation capabilities in the industry. 


## 🖼️ Images vs. Containers

Understanding the lifecycle of containerization requires distinguishing between the static "blueprint" and the running "process." 

| Feature | Image | Container |
| --- | --- | --- |
| **Definition** | An executable package that includes everything needed to run an application. 
| A runtime instance of an image. 
| **State** | <br>**Immutable:** It does not change once created. 
| <br>**Mutable:** It has a writable layer and state. 
| **Analogy** | A recipe or a blueprint. 
| The actual meal being cooked. 


## ⚖️ Containers vs. Virtual Machines (VMs)

While both provide isolation, they operate at different layers of the technology stack. 

### Virtual Machines

* VMs are an abstraction of **physical hardware**, turning one server into many servers. 
* Each VM includes a **full copy of an operating system**, the application, and necessary binaries/libraries—taking up tens of GBs. 
* Can be slow to boot. 


### Containers

* Containers are an abstraction at the **app layer** that packages code and dependencies together. 
* Multiple containers can run on the same machine and **share the OS kernel** with other containers. 
* They take up less space (MBs) and start up almost instantly. 


## 🚀 Why Use Containers?

- **Consistency:** Solve the "it works on my machine" problem by ensuring the environment is identical across development, testing, and production. 
- **Efficiency:** Higher density of applications on a single host compared to VMs. 
- **Agility:** Faster deployment cycles and easier scaling. 
