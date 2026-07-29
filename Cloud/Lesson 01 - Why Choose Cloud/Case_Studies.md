# Case Studies Worksheet: Business Upsides of Cloud Deployment

## Instructions
Research the following case studies to understand the specific business benefits of cloud deployments. For each case study, use the provided source links to find answers to the questions. Be prepared to discuss your findings with the class.

**Categories:** We'll explore three primary business drivers for cloud adoption:
1. **Speed to Market & Innovation**
2. **Operational Efficiency & Cost Reduction**
3. **Scale & Resilience**

---

## 1. Speed to Market & Innovation

**Think About It:** How does the cloud help companies innovate faster? What bottleneck does it remove?

_______________________________________________________________________________

_______________________________________________________________________________

### Case Study: Moderna (Healthcare)

**Source:** [AWS Innovators: Moderna](https://aws.amazon.com/solutions/case-studies/innovators/moderna/)

**Cloud Provider:** _______________

**Research Questions:**
1. What type of company is Moderna, and what technology do they use for drug development?

   _______________________________________________________________________________
```Moderna is a biotechnology company that has developed a pipeline based on mRNA technology to support various vaccines and therapeutic programs.

Moderna credits their partnership with AWS for allowing them to deliver their mRNA products much faster than traditional timelines, specifically noting that the technology provided the computing power necessary to support their research, development, and genomics work.```
   _______________________________________________________________________________

2. How did AWS cloud services accelerate Moderna's drug discovery process and development timeline?

   _______________________________________________________________________________
```According to the speaker, AWS Data Exchange accelerated Moderna’s processes by connecting the team to the right data vendors and simplifying the procurement of necessary datasets for their epidemiologists. By centralizing data cataloging, organization, and flow into one tool, the company reduced data ingestion time by 50 to 60 percent (0:56-1:09).

This improved pipeline allowed the team to:

Streamline the ingestion of real-world evidence used to track RSV globally (0:22-0:28).
Visualize data and create KPI metrics that help stakeholders make informed business decisions (0:46-0:50).
Provide immediate visibility to stakeholders regarding what data to expect, which increased overall project efficiency```
   _______________________________________________________________________________

3. What specific AWS capabilities did Moderna leverage for their workflows?
```Moderna leveraged the following AWS capabilities for their workflows:

Amazon Data Exchange (ADX): Used to connect with the right data vendors and securely bring third-party data directly into their systems.
Data Warehouse: Used to store ingested information, allowing for centralized cataloging and organization.

o support their workflows, Moderna leverages several AWS services, including:

Amazon Connect: Used to build their global, automated, omnichannel contact center (OC3).
Amazon Lex and AWS Lambda: Used to build an in-house, conversational AI engine ("Radeon") to detect customer intent.
Additional Services: They utilize Amazon CloudWatch and Kinesis to support their data-driven, scalable platform.```
   _______________________________________________________________________________

4. **Discussion:** Why would Moderna's intense data analysis workflows be difficult with traditional on-premise infrastructure?

   _______________________________________________________________________________

   _______________________________________________________________________________

---

### Case Study: Blue Origin (Aerospace)

**Source:** [How Blue Origin Built the First AI Agent-Designed Hardware for the Moon](https://aws.amazon.com/solutions/case-studies/blue-origin-case-study/)

**Cloud Provider:** _______________

**Research Questions:**
1. What engineering challenge was Blue Origin trying to solve for their lunar lander?

   _______________________________________________________________________________

   _______________________________________________________________________________

2. What cloud technology did they leverage to speed up their design process?

   _______________________________________________________________________________

   _______________________________________________________________________________

3. What was the impact on their design cycle timeline?
   
   * Before cloud: _______________
   * After cloud: _______________

4. **Discussion:** How does running "thousands of design variations simultaneously" differ from traditional design workflows?

   _______________________________________________________________________________

   _______________________________________________________________________________

---

## 2. Operational Efficiency & Cost Reduction

**Think About It:** How can moving to the cloud reduce costs when you're paying for cloud services? What types of costs are eliminated?

_______________________________________________________________________________

_______________________________________________________________________________

### Case Study: Capital One (Finance)

**Source:** [Capital One Cloud Journey](https://www.capitalone.com/software/blog/cloud-migration-journey/)

**Cloud Provider:** _______________

**Research Questions:**
1. What was Capital One's infrastructure situation before migrating to the cloud?

   _______________________________________________________________________________

   _______________________________________________________________________________

2. What specific pain points were they experiencing with their on-premise data centers?

   _______________________________________________________________________________

   _______________________________________________________________________________

3. What were the measurable results of their cloud migration?
   
   * Development environment setup time reduced from: _______________
   * Number of data centers closed: _______________
   * Other benefits: _______________________________________________________________________________

4. **Discussion:** Where did they reinvest the savings from closing their data centers?

   _______________________________________________________________________________

---

### Case Study: Mazda (Automotive)

**Source:** [How the automotive industry is transforming with cloud](https://blogs.oracle.com/cloud-infrastructure/customerseries-mazda)

**Cloud Provider:** _______________

**Research Questions:**
1. What business challenges was Mazda facing with their on-premises infrastructure?

   _______________________________________________________________________________
```Transactions were being processed on an on-premises server and storage infrastructure that created heavy workloads and made inventory difficult to manage across different business functions.

Demand forecasting became cumbersome, and their system lacked the scalability required to support long-term global growth initiatives while managing 250,000 repair parts and accessories.```
   _______________________________________________________________________________

   _______________________________________________________________________________

2. What specific operational issues did they need to solve? (Think about inventory, forecasting, and data analysis)

   _______________________________________________________________________________
```Inventory Management: Difficulty tracking and managing inventory efficiently across various business functions and regions.

Forecasting: Demand forecasting processes were slow, cumbersome, and limited in frequency.

Data Analysis: A need to expand analysis data to account for demand forecasting by country, region, and globally.```
   _______________________________________________________________________________

3. What results did they achieve after migrating to Oracle Cloud Infrastructure?
   
   * Cost reduction: _______________ ```Cut costs by 50%```
   * Performance increase: _______________ ```Boosted performance by 70%```
   * Total Cost of Ownership (TCO) impact: _______________ ```Led to a reduction in the five-year total cost of ownership```

4. How did the cloud change their forecasting capabilities?

   * Before: _______________ ```Ran forecasts on a monthly basis```
   * After: _______________ ```Able to run daily forecasts and adjust production up or down based on real-time demand```

5. **Discussion:** Why is "on-demand forecasting" and the ability to "move production up or down with demand" only possible with cloud infrastructure?

   _______________________________________________________________________________

   _______________________________________________________________________________

---

---

## 3. Scale & Resilience

**Think About It:** What happens when a popular website gets more traffic than expected? How does the cloud help handle unpredictable demand?

_______________________________________________________________________________

_______________________________________________________________________________

### Case Study: Netflix (Media & Entertainment)

**Source:** [Netflix on AWS](https://aws.amazon.com/solutions/case-studies/netflix/)

**Cloud Provider:** _______________

**Research Questions:**
1. What was Netflix's business evolution that required massive infrastructure changes?

   _______________________________________________________________________________
```Netflix transitioned from a DVD-by-mail service to a global streaming platform, and later expanded into live events and advertising. Moving from physical disc logistics to streaming high-definition video to tens of millions of concurrent users required moving away from traditional, fixed-capacity datacenters to an elastic cloud architecture.```
   _______________________________________________________________________________

2. What scale has Netflix achieved using cloud infrastructure?
   
   * Number of members: _______________ ```Over 280 million paid subscribers worldwide.```
   * Geographic reach: _______________ ```Available in more than 190 countries.```

3. How does Netflix handle sudden traffic spikes in the cloud? What AWS capabilities do they use?

   _______________________________________________________________________________
``` To manage massive, sudden spikes in viewer traffic (such as major content releases or live broadcasts), Netflix relies on multi-region architecture and automated scaling:

- Traffic Spike Strategy:

-- Multi-Region Redundancy: Operations are active across four AWS Regions simultaneously. If one region encounters an issue or severe overload, traffic can be dynamically shifted to another region.

-- Hybrid Auto-Scaling: Uses predictive pre-scaling to spin up compute capacity ahead of expected viewing spikes, combined with reactive auto-scaling to handle sudden surges.

- AWS Capabilities & Services Used:

-- Thousands of Auto-Scaling Groups (ASGs): Dynamically adjusts virtual machine (EC2) capacity.

-- Amazon Aurora: Relational database management providing low-latency replication across regions.

-- Amazon EKS (Elastic Kubernetes Service): Container orchestration for microservices at scale.

-- Amazon EMR (Elastic MapReduce): Large-scale batch processing and big data analytics.

-- Amazon S3: Scalable object storage for raw media assets and video files. ```
   _______________________________________________________________________________

4. What benefits does Netflix gain from using AWS for global streaming delivery?

   _______________________________________________________________________________
```Speed & Agility: Engineering teams can rapidly experiment, deploy, and scale microservices without managing physical server hardware.

Global Reach & Low Latency: AWS's global infrastructure footprint enables Netflix to serve users across the globe with high availability and reliability.

Performance & Cost Efficiency: Migrating critical databases to services like Amazon Aurora provided up to 75% performance improvements and 28% cost savings, reducing maintenance overhead.

Resilience: Multi-region active-active deployment minimizes single points of failure and prevents global service outages during peak events.```
   _______________________________________________________________________________

5. **Discussion:** Why would it be impractical for Netflix to build their own data centers to handle this global scale?

   _______________________________________________________________________________

---

### Case Study: MakeMyTrip (Travel)

**Source:** [MakeMyTrip Case Study: 22% Cost Reduction via AWS Containers](https://smeoncloud.in/makemytrip-cuts-compute-costs-by-22-with-amazon-ecs-eks/)

**Cloud Provider:** _______________

**Research Questions:**
1. What unique traffic pattern does MakeMyTrip experience, and why does it make their infrastructure challenging?

   _______________________________________________________________________________

   _______________________________________________________________________________

2. What was the problem with buying enough servers to handle "peak" capacity?

   _______________________________________________________________________________

   _______________________________________________________________________________

3. What cloud feature did they use to solve this problem?

   _______________________________________________________________________________

4. What were the measurable results?
   
   * Cost reduction: _______________
   * Availability during peak seasons: _______________

5. **Discussion:** How does "Auto Scaling" work, and why is it only possible in the cloud?

   _______________________________________________________________________________

   _______________________________________________________________________________

---

## Synthesis Questions

After completing all the case studies, answer these broader questions:

1. **Pattern Recognition:** What common themes do you see across all these case studies?

   _______________________________________________________________________________

   _______________________________________________________________________________

   _______________________________________________________________________________

2. **Business Value:** If you had to pitch cloud migration to a CEO, what would be your top three arguments based on these case studies?

   a. _______________________________________________________________________________

   b. _______________________________________________________________________________

   c. _______________________________________________________________________________

3. **Industry Differences:** Do different industries (healthcare, finance, entertainment, travel) benefit from the cloud in different ways? Explain.

   _______________________________________________________________________________

   _______________________________________________________________________________

   _______________________________________________________________________________

4. **Trade-offs:** Based on your research, can you identify any potential downsides or challenges of cloud migration that these companies had to overcome?

   _______________________________________________________________________________

   _______________________________________________________________________________

   _______________________________________________________________________________

---

## Additional Research Resources

For further exploration, browse the customer success hubs of major cloud providers:

* **AWS Case Studies:** [aws.amazon.com/solutions/case-studies](https://aws.amazon.com/solutions/case-studies)
* **Microsoft Azure Customer Stories:** [azure.microsoft.com/en-us/resources/customer-stories](https://azure.microsoft.com/en-us/resources/customer-stories)
* **Google Cloud Customers:** [cloud.google.com/customers](https://cloud.google.com/customers)
