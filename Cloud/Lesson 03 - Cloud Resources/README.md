# Lesson 03 - Cloud Resources (The Basics)

This document outlines the fundamental components of cloud computing, often referred to as "Cloud Resources," and the shared responsibility model between providers and users. 

## 🌐 What is a Cloud Resource?

A cloud resource is a fundamental, on-demand IT asset accessed over the internet. It functions similarly to a public utility where you connect to a "grid" (the provider's network) and pay only for the capacity you use. 

### Key Characteristics

- **On-Demand:** Resources can be acquired instantly without human intervention. 
- **Pay-as-you-go:** Usage is treated as an operating expense rather than a large upfront capital cost. 
- **Elastic:** Capacity scales up or down easily to meet fluctuating demand. 


## 🏛️ The Three Pillars of Cloud

Cloud infrastructure is built upon three core pillars that work together like a biological system. 

| Pillar | Analogy | Description |
| --- | --- | --- |
| **Compute** | The "Brain" 
| Provides the CPU and RAM needed to run applications and workloads. 
| **Storage** | The "Memory" 
| Persistent space for saving and retrieving digital information and files. 
| **Networking** | The "Nervous System" 
| The fabric that connects resources and manages traffic to the internet. 


### Common Resource Types

- **Object Storage:** Highly scalable and cost-effective for unstructured data (videos, images) using unique identifiers instead of folders. 
- **Managed Databases:** Fully managed services where the provider handles backups and maintenance. 
- **Virtual Private Cloud (VPC):** A logically isolated private network segment for secure resource deployment. 
- **Content Delivery Network (CDN):** Distributed servers that cache content closer to users to reduce latency. 


## 🛡️ Shared Responsibility Model

Security in the cloud is a partnership between the provider and the customer. 

- **Provider’s Responsibility:** Security **of** the cloud, including physical data centers, hardware, and underlying services. 
- **Customer’s Responsibility:** Security **in** the cloud, including securing data, managing user access, and correct resource configuration. 


## 🏗️ Real-World Example: Building a Basic Setup

To create a functional cloud environment, a business might combine these components: 

1. **Compute:** A Virtual Machine to run the application. 
2. **Storage:** **Azure Files** to provide managed network drives for shared access. 
3. **Networking:** A **VPC** to wrap these assets in a secure, private network. 
