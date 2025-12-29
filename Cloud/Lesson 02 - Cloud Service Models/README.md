# Lesson 02 - Cloud Computing - *-as-a-Service (XaaS)

This document provides a comprehensive overview of primary cloud service models, including Infrastructure (IaaS), Platform (PaaS), and Software (SaaS), along with selection criteria for various business use cases.

## 🎯 Lesson Objectives

* Discuss and differentiate between the service models of **IaaS, PaaS, and SaaS**.
* Learn to select the **appropriate service model** based on specific technical and business requirements.


## 🍕 The "Pizza as a Service" Analogy

To understand management responsibilities, consider the "New Pizza as a Service" model:

- **Traditional On-Premises:** You manage everything from the kitchen and gas to the toppings and cooking.
- **IaaS (Kitchen-as-a-Service):** The vendor provides the kitchen, gas, and oven; you manage the dough, toppings, and cooking.
- **PaaS (Walk-In-and-Bake):** The vendor provides everything up to the dough; you just manage the toppings and the final cooking.
- **SaaS (Pizza-as-a-Service):** The vendor manages the entire process; you simply consume the final product.


## 🏗️ IaaS: Infrastructure as a Service

IaaS was the first cloud model available and allows you to build services from the operating system up.

- **Core Features:** Self-service on-demand portals with incremental billing and detailed usage reporting.
- **Financials:** No upfront costs; users pay only for the resources needed.
- **Deployment Workflow:** Define the problem  Choose OS  Select Services  Provision Resources  Setup VM instances  Run Service.
- **Major Providers:** Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP).


## 💻 PaaS: Platform as a Service

PaaS provides a managed execution runtime environment, allowing developers to focus on code rather than infrastructure.

- **Key Benefits:** Multi-tenant environments offer significant savings through shared underlying functions like databases.
- **Development Flow:** Use an IDE for development and deploy directly via tools like Git (e.g., Heroku).
- **Technical Considerations:** Requires evaluation of supported languages, frameworks (e.g., Ruby on Rails, Flask, Django, Laravel), and API types (RESTful vs. SOAP).
- **Major Providers:** Google App Engine, AWS Elastic Beanstalk, and Heroku.


## 📧 SaaS: Software as a Service

SaaS provides a complete, end-to-end software solution where the provider handles everything, including system security.

- **Common Uses:** Office productivity applications, E-commerce, Project Management, and Accounting.
- **Economic Model:** Subscription-based licensing model instead of one-time purchases, leveraging economies of scale for cost reduction.
- **Advantages:** Improved security, global accessibility, and standardized compatibility across the organization.
- **Examples:** Office 365, Google Apps, Slack, and Zendesk.


## 📊 Extended Cloud Hierarchy

Beyond the primary three, other specialized "As-a-Service" models exist:

- **FaaS (Function-as-a-Service):** AWS Lambda, Cloud Functions.
- **DaaS (Database-as-a-Service):** DynamoDB, CouchDB, Oracle Data Cloud.
- **STaaS (Storage-as-a-Service):** Dropbox, OneDrive, Google Drive, AWS S3.
- **GaaS (Gaming-as-a-Service):** NVIDIA GeForce Now, Google Stadia.
