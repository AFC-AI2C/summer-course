# ☁️ Cloud Computing & Deployment Scenarios

This handout covers six real-world scenarios regarding cloud infrastructure, deployment models, and cost analysis.

---

## 📚 Table of Contents
1. [Scenario 1: Deploying a LAMP Stack](#scenario-1-deploying-a-lamp-stack-for-wordpress)
2. [Scenario 2: High Performance Computing (HPC)](#scenario-2-research-lab-simulation--compute-scaling)
3. [Scenario 3: Ruby on Rails PaaS](#scenario-3-deploying-a-ruby-on-rails-application)
4. [Scenario 4: Python ML Tool Deployment](#scenario-4-deploying-a-python-machine-learning-tool)
5. [Scenario 5: Office Software Migration](#scenario-5-transitioning-to-cloud-office-solutions)
6. [Scenario 6: Gaming as a Service (GaaS)](#scenario-6-gaming-as-a-service-gaas-vs-hardware)

---

## Scenario 1: Deploying a LAMP Stack for WordPress

**Situation:** You are deploying a LAMP stack (Linux, Apache, MySQL, PHP) to run a WordPress site. You anticipate approximately **1,000 users** during the initial launch phase.

### 1. Is IaaS (Infrastructure as a Service) your only option?
**No.** While IaaS provides granular control, other models exist:

* **PaaS (Platform as a Service):** (e.g., AWS Elastic Beanstalk) Good for speed, but you lose server config control.
* **SaaS (Software as a Service):** (e.g., WordPress.com) Zero maintenance, but no backend code access.
* **Shared Hosting:** (e.g., Bluehost) Cheap, but suffers from the "Noisy Neighbor" effect.

> **Verdict:** If you are deploying the LAMP stack yourself, you need the fine-grained access that IaaS provides. Otherwise, you can use one of the other service models to offload some of that work to the service provider at the cost of flexiblity.



### 2. If using IaaS, how many servers do you need?
For **1,000 users**, a **Single Server (Monolithic Architecture)** is recommended.

* **Architecture:** Apache + MySQL on one Virtual Machine (VM).
* **Why?**
    * **Latency:** Zero network lag between app and database.
    * **Cost:** One larger server is cheaper to manage than two small ones.
    * **Performance:** 1,000 users is a light load for modern VPS hardware.

**Scalability Note:** If you grow to 10,000+ users, you should **Decouple** the services:
* *Server A:* Web Server (Apache)
* *Server B:* Database (MySQL)



### 3. What OS are you planning to use?
**Recommendation:** 🐧 **Ubuntu 24.04 LTS**

* **Documentation:** Industry standard for LAMP tutorials.
* **Stability:** LTS (Long Term Support) ensures 5 years of security updates.
* **Package Manager:** `apt` is user-friendly for installing dependencies.

---

## Scenario 2: Research Lab Simulation & Compute Scaling

**Situation:** Your team needs to run a simulation generating 4TB of data, requiring **2,000 hours** of total compute time.

### 1. With 6 VMs, how long will it take to finish in-house?
**Time required:** 📅 **~14 Days**

* **Math:** $2,000 \text{ hours} / 6 \text{ VMs} = 333.33 \text{ hours}$
* $333.33 / 24 \text{ hours} \approx 13.89 \text{ days}$

*(Note: Assumes perfect parallelism where tasks are split evenly).*



### 2. You need it done in 5 days. How many VMs do you need?
**VMs required:** 💻 **17 VMs**

* **Target:** $5 \text{ days} \times 24 \text{ hours} = 120 \text{ hours max duration}$.
* **Math:** $2,000 \text{ total hours} / 120 \text{ target hours} = 16.66 \text{ VMs}$.
* **Rounding:** You cannot provision 0.6 of a computer, so you must round up to **17**.

---

## Scenario 3: Deploying a Ruby on Rails Application

**Situation:** You are developing a Ruby on Rails app and want to test it for free before moving to production.

### 1. What PaaS service has a "free" tier?
**Recommendation:** **Koyeb** or **Render**

* **Koyeb:** Currently offers a robust "forever free" tier with 512MB RAM and Docker support.
* **Render:** Very popular, but the free web service "sleeps" (spins down) after inactivity, causing slow load times on the next visit.

### 2. Cost for "Real" Production Mode?
To run 24/7 without "sleeping" and with a persistent database, budget **$5.00 – $15.00 per month**.

| Provider | Est. Cost | Notes |
| :--- | :--- | :--- |
| **Railway** | **~$5.00** | Flexible "Hobby" plan. Best for cost efficiency. |
| **Heroku** | **~$10.00** | $5 Eco Dyno + $5 Mini Postgres. Industry standard workflow. |
| **Render** | **~$14.00** | $7 Web Service + $7 Database. |

---

## Scenario 4: Deploying a Python Machine Learning Tool

**Situation:** You have a standalone Python ML tool and want to make it a web app to collect validation data from users.

### 1. What web framework would you choose?
**Recommendation:** **Streamlit** 🎈

* **Why Streamlit?** It turns Python scripts into web apps instantly. No HTML/CSS knowledge required. Perfect for data/ML validation.
* **Alternative:** **FastAPI** if you need a high-performance backend to connect to a custom frontend.

### 2. What PaaS system will support this?
**Recommendation:** **Streamlit Community Cloud**

* **Why?** Connects directly to GitHub and renders the app immediately.
* **Alternative:** **Render** if you need a persistent PostgreSQL database to store the collected user data.

### 3. Pricing Model?
**Strategy:** **Freemium / Low-Cost Fixed**

* **Validation Phase:** $0–$7/mo (Free compute + Small paid DB for data persistence).
* **Production:** $15–$25/mo (Standard compute instance + Scaled storage).

---

## Scenario 5: Transitioning to Cloud Office Solutions

**Situation:** Startup with 30 employees. Choosing between buying standalone Office licenses ($150 each) or a SaaS subscription.

### 1. Available SaaS Solutions
* **Microsoft 365:** The standard. Includes desktop Word/Excel/PowerPoint.
* **Google Workspace:** Cloud-native (Docs/Sheets). Great for collaboration, but strictly browser-based.

### 2. Pros and Cons of SaaS
* ✅ **Pros:** Lower upfront cash outlay, always up-to-date software, easier to scale up/down.
* ❌ **Cons:** Higher long-term cost (usually more expensive after ~3 years), dependent on internet connection.

### 3. Cost Analysis (Microsoft 365)
For 30 employees, you likely need **Business Standard** ($12.50/user/mo) to keep the Desktop apps your team is used to.

* **Monthly Cost:** $12.50 \times 30 = \mathbf{\$375/month}$
* **Yearly Cost:** $\mathbf{\$4,500/year}$

---

## Scenario 6: Gaming as a Service (GaaS) vs. Hardware

**Situation:** Analyzing the cost of cloud gaming (e.g., GeForce Now) vs. buying a high-end GPU.

### 1. How GaaS Works
Instead of your PC doing the work, a server farm processes the game and streams video to you.
* **Key Tech:** Input $\rightarrow$ Internet $\rightarrow$ Server GPU $\rightarrow$ Video Stream $\rightarrow$ Your Screen.



### 2. The "Break Even" Point
Comparing **NVIDIA GeForce Now Ultimate** ($20/mo) vs. buying an **RTX 4080** (~$1,000).

* **Math:** $\$1,000 \text{ (GPU)} / \$20 \text{ (Sub)} = 50 \text{ months}$.
* **Result:** It takes **4.2 years** of subscription payments to equal the cost of just the graphics card.

> **Crucial Context:** If you do *not* already own a desktop tower, buying a full PC costs ~$1,800+. In that case, the break-even point extends to **7.5 years**, making Cloud Gaming a massive bargain for non-PC owners.
