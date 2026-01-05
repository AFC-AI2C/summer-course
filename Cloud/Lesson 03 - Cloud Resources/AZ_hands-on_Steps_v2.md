# Azure Hands-On Demo: Personal Website Deployment

## STEP 0: Create Azure Account
- If you have not already done so, visit the following link to create an Azure account: [Azure Account Creation](https://azure.microsoft.com/en-au/pricing/purchase-options/azure-account/search?ef_id=_k_b0a9283dcce5166a078f416f65434c5a_k_&OCID=AIDcmms2uus4dd_SEM__k_b0a9283dcce5166a078f416f65434c5a_k_&msclkid=b0a9283dcce5166a078f416f65434c5a). 
- If the above link does not work, simply type "create azure account" into a search engine of your choice and click on the appropiate link.
- You can choose to accept the $200 credit for 30 days or pay as you go for the duration of the prerequisite course.  During the AI Technician Course, you will receive instructions from the CMU faculty on how to receive sufficient student credits for course completion. 

---

## **STEP 1: Create Resource Group**
**Location:** Azure Portal > Resource Groups > Create
- Resource Groups can be found by simply typing "Resource Groups" in the Azure Portal Search Bar at the top of the home screen (https://portal.azure.com/).
- The Create buttom can be found in the top left side of the Resource Groups screen next to a + sign.  

### **Basic Settings:**
- Name: `group[X]-rg` (e.g., `group1-rg`)
- Location: East US

### **Click the "Review + Create" button at the bottom of the page.**

---


## **STEP 2: Create Virtual Network**
**Location:** Azure Portal > Virtual Networks > Create

### **Basic Settings:**
- Select: Resource Group from Step 1
- Name: `group[X]-network` (e.g., `group1-network`)
- Region: East US

### **IP Addresses Tab (Top of the page under "Create Virtual Network"):**
1. In the center of the tab, replace the default 10.0.0.0/16 address space with your designated group's address space below.
- Address space: `10.1.X.0/28`
  - Group 1: `10.1.1.0/28`
  - Group 2: `10.1.2.0/28`
  - Group 3: `10.1.3.0/28`
  - Group 4: `10.1.4.0/28`
  - Group 5: `10.1.5.0/28`

2. **Add subnet:**
  - Click the "+ Add a subnet" button above the address space box.  A box should appear on the right side of your screen with the "Edit subnet" title. 
  - Name: `first-subnet`
  - Address range: Same as VNet address space above `10.1.X.0/28`
  - Leave the remaining settings (i.e., Security, Service Endpoints, etc.) as default.
  - Click the "Add" button at the bottom.

### **Click the "Review + Create" button at the bottom of the page.  Once you receive the "Validation Passed" green bar, click the "Create" button at the bottom of the page.**

---

## **STEP 3: Create Virtual Machine**
**Location:** Azure Portal > Virtual Machines > Create

### **Basics Tab:**
- Resource group: Same `group[X]-rg`  
- VM name: `student-vm-[YOUR INITIALS]`  
- Region: East US
- Availability Options: No infrastructure redundancy required
- Security Type: Standard
- Image: Ubuntu Server 22.04 LTS x64 Gen2
- Size: B1s (1 vcpu, 1 GB RAM)
- **Authentication type:** Password
- **Username:** `azureuser`
- **Password:** Create a strong password (write it down!)
- Note: You may receive recommendations for specific configurations (i.e., different region, availability zone, etc.) that help the VM deploy.  Not following these recommendations usually results in VM deployment failure.  You will need to assess whether a specific recommendation interferes or breaks other parts of a specific exercise.  For this exercise, make sure that your VM is in the same region as your network group.   

### **Networking Tab:**
- Virtual network: Select your `group[X]-network`.  If you cannot see this virtual network, then a recommendation might have placed you in a different region.  If so, then revert back to the original region or consult with your group members about changing the virtual network region. 
- Subnet: `web-subnet`
- Public IP: Create new
- **Select inbound ports:** SSH (22), HTTP (80), and HTTPS (443)
- Leave the remaining settings as their default.

### **Create VM (Click on the "Review + Create" button and then (when the validation passes) the "Create" button)**

---

## **STEP 4: SSH Into Your VM**
**Location:** Azure Portal > Virtual Machines > [your-vm]

### **Get Connection Info:**
1. Go to your VM in Azure Portal
2. Note down your VM's **Public IP address**.  The public IP address will be on the right side of the page under Networking > Public IP Address.

### **Connect via SSH:**
1. Open **Cloud Shell** (>_) in top navigation bar.  The Cloud Shell icon should be between the Copilot and Notifications icons.  Once you click on the Cloud Shell icon, a black cloud shell will appear at the bottom of your screen. 
2. Connect using username/password:

```bash
# SSH into your VM (replace with your actual Public IP)
ssh azureuser@[YOUR-VM-PUBLIC-IP]

# You might be asked "Are you sure you want to continue connecting (yes/no/[fingerprint])?"  Type yes.

# When prompted, enter the password you created during VM setup
# Note: You won't see characters as you type the password (this is normal)

```

3. **You're now inside your VM!** The prompt will change to: `azureuser@student[name]-vm:~$`
4. Optional: You can clear away previous commands and move your prompt to the top of the cloud shell by typing the 'clear' command. 

---

## **STEP 5: Install Software and Deploy Website**
**Location:** Inside your VM via SSH using the cloud shell.

### Update system and install nginx using the following commands.  
- You can issue the following commands individually or copy/paste them all at once.
- The latter method does sometimes complicate troubleshooting and might cause other issues in future labs.**
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
```

### **Test nginx installation:**
```bash
curl http://localhost
# Should see "Welcome to nginx!" page
```

### **Remove default nginx page:**
```bash
sudo rm /var/www/html/index.nginx-debian.html
```

### **Upload your starter website:**
1. Exit the VM by typing 'exit'.  You should land in your cloud shell home directory (i.e., /home/[your name]).
2. Locate the starterpack.html file on your local device.  You will need to download this file from github.
3. Upload the starterpack.html file to your VM working directory using the Manage File > Upload feature at the top of the cloud shell.
4. Use Secure Copy (scp) to transfer the startpack.html file from your cloud shell to your VM.
    - This is the general structure of the scp command you need to execute:
        scp [insert the cloud shell path to the starterpack.html file] [your_username@you_vm_ip_address:/path/to/your/VM/working/directory/]
    - Example: scp /home/john/starterpack.html azureuser@20.169.243.207:/home/azureuser
6. SSH again into your VM.  Confirm the starterpack.html file's presense in your VM's working directory using the 'ls' command. 

### **Deploy your starter website:**
```bash
# Copy the provided starterpack.html file
sudo cp starterpack.html /var/www/html/index.html

# Set proper permissions
sudo chown www-data:www-data /var/www/html/index.html
sudo chmod 644 /var/www/html/index.html
```

### **Test your website locally:**
```bash
curl http://localhost & curl http://publicip
# Should show your starterpack.html content.  You may receive a 'Could not resolve host: publicip' statement at the bottom of your curl.  That is expected. 
```

---

## **STEP 6: Network Testing (5 minutes)**
**Location:** Inside your VM via SSH

### **Check your network details:**
```bash
# Check your private IP address
ip addr show

# Note your private IP (will be something like 10.1.16.4)
```

### **Test group connectivity:**
```bash
# Test connectivity within your group (replace with classmate's IP).  A successful ping should return something like "64 bytes from 10.1.1.4: icmp_seq=7 ttl=64 time=0.047 ms".
ping -c 3 10.1.16.5

# Try to ping another group.  This should FAIL as you have not defined a route to that other group.  This is a demonstation of network isolation. 
ping -c 3 10.1.32.4
```

### **Exit SSH:**
```bash
exit
```

---

## **STEP 7: Share Network Information (5 minutes)**
**Location:** Azure Portal + Class Discussion

### **Get your VM's Public IP:**
1. Go to **Virtual machines** in Azure Portal
2. Click your VM name
3. Note down the **Public IP address**

### **Share with class:**
1. Write your **Public IP** on the board
2. Note your **Private IP** from Step 5
3. Compare private IPs within your group vs other groups

### **See [this link](https://www.geeksforgeeks.org/computer-networks/difference-between-private-and-public-ip-addresses/) for more information about public IPs vs private IPs.**

---

## **What You Learned So Far:**

### **Key Concepts:**
- **Compute:** VMs can run nginx web servers using direct file deployment. 
- **Networking:** VNets provide private network isolation between groups.   
- **Linux Skills:** File editing, permissions, and system administration. 
- **Network Understanding:** Private vs Public IP addressing. 

### **Key Demonstrations Completed:**
- **Direct VM Development:** Copying and editing files on cloud servers. 
- **Network Isolation:** /28 subnets provide group separation. 
- **Private IP Communication:** Can ping within group, but not across groups. 
