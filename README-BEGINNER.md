# Supply Chain Active Defense Framework: Complete Beginner's Guide

We are building a trap to catch cybercriminals who are poisoning the software supply chain. Because the malware we are hunting (like the "Mini Shai-Hulud" worm) is incredibly dangerous and can delete everything on a computer, you must follow these instructions exactly. 

Even if you have never written a line of code or set up a server before, this guide will walk you through creating a secure environment, laying the traps, and launching your tracking dashboard.

---

## ⚠️ CRITICAL WARNING: WHAT IS "ISOLATION"?
**Do not run these files on your normal, everyday computer.** 

The malware we are tracking has a "dead-man's switch." If it realizes it has been caught, it will try to erase the hard drive. To protect yourself, we must use **Isolation**. 

Isolation means building a "fake computer" inside your real computer. We call this a **Virtual Machine (VM)**. It acts like a secure, blast-proof safe room. If the malware destroys the safe room, your actual computer (and all your personal files) remains perfectly safe.

### Phase 1: Building the Safe Room (Isolation)
Before doing anything else, you need to create your Virtual Machine.
1. **Download VirtualBox:** Go to the internet and search for "Oracle VirtualBox." Download and install it like any regular program. This is the software that builds the safe room.
2. **Download Ubuntu:** Search for "Ubuntu Desktop ISO" and download it. Ubuntu is a free operating system (like Windows or macOS) that security professionals use.
3. **Create the Machine:** Open VirtualBox, click **"New"**, name it `Hunter-Trap`, and select the Ubuntu file you just downloaded. Follow the on-screen clicks to finish setting it up.
4. **Start the Machine:** Click "Start" in VirtualBox. You are now looking at a brand-new, isolated computer screen inside a window. **Do all of the following steps inside this new Ubuntu window.**

---

## Phase 2: Getting Your Tools Ready
Now that you are inside your safe Ubuntu computer, we need to open the "Terminal." The Terminal is simply a black box where you can type commands directly to the computer. 

1. **Open the Terminal:** Press `Ctrl` + `Alt` + `T` on your keyboard at the same time. A black window will pop up.
2. **Create a Folder for Our Trap:** Type the following command and press Enter:
   ```bash
   mkdir active-defense-tracker
   
```
3. **Go Inside the Folder:** Type this and press Enter:
   ```bash
   cd active-defense-tracker
   
```
4. **Download the Files:** You will need to save the files from this GitHub repository (`deploy_honeytokens.sh`, `ebpf_monitor.py`, `report_incident.py`, and `dashboard.html`) into this exact folder. You can do this by opening the web browser inside Ubuntu, coming to this GitHub page, clicking "Download ZIP", and then extracting it to your new folder.

---

## Phase 3: Installing the Required Software
Your new Ubuntu computer needs a few basic tools to read the traps we are setting.
Type the following exact text into your Terminal and press Enter (it may ask for the password you created when setting up Ubuntu):
   ```bash
   sudo apt-get update
   sudo apt-get install bcc-tools libbcc-examples linux-headers-$(uname -r) python3-bpfcc python3-pip
   ```
*(Wait for the computer to finish downloading and installing these tools. It might take a few minutes.)*

---

## Phase 4: Setting the Traps (Honeytokens)
We are going to create fake digital keys. When the hacker's malware steals these keys and tries to use them, we will get an alert with their location.
1. **In your Terminal**, make sure you are still in the active-defense-tracker folder.
2. We need to make the trap file "runnable." Type this and press Enter:
   ```bash
   chmod +x deploy_honeytokens.sh
   ```
3. **Set the Trap:** Type this and press Enter:
   ```bash
   ./deploy_honeytokens.sh
   ```
*(You should see a message on the screen saying the traps (AWS, GitHub, and SSH lures) have been successfully injected into the system.)*

---

## Phase 5: Turning on the Kernel Alarm (eBPF Monitor)
Now we turn on the deep-system alarm. This program watches the very core of the computer (the "Kernel") to see if the malware tries to trigger its wipe command (like rm -rf).
1. **In your Terminal**, type this command and press Enter:
   ```bash
   sudo python3 ebpf_monitor.py
   
```
*The screen will tell you the monitor is active. Leave this Terminal window open. It is now actively listening for attacks.*

---

## Phase 6: Deploying the Command Dashboard (HTML)
You have set the traps and turned on the alarm. Now, you need to open your visual Command Center to watch for activity. We have designed this so you do not need to set up a complicated web server. 

### The Easiest Way (Double-Click)
1. On your Ubuntu desktop, open your **Files** app (it looks like a manila folder icon).
2. Find the `active-defense-tracker` folder you created.
3. Inside, you will see the `dashboard.html` file.
4. **Double-click** `dashboard.html`. It will automatically open in your web browser. 

### The Professional Way (Local Server)
If you want to run it like a real web server, you can do this:
1. Open a **brand new** Terminal window (`Ctrl` + `Alt` + `T`). 
2. Go back to your folder by typing: 
   ```bash
   cd active-defense-tracker
   
```
3. Type the following command to start a simple web server:
   ```bash
   python3 -m http.server 8000
   
```
4. Open the web browser inside Ubuntu (like Firefox).
5. In the address bar at the top, type exactly this and press Enter:
   `http://localhost:8000/dashboard.html`

You will now see the red and black **DEFENSE COMMAND: ACTIVE TRACKING** dashboard. It is listening, watching, and ready to automatically report the hackers the moment they trip your wires.

### Phase 1: Building the Safe Room (Isolation)
Before doing anything else, you need to create your Virtual Machine.
1. **Download VirtualBox:** Go to the internet and search for "Oracle VirtualBox." Download and install it like any regular program. This is the software that builds the safe room.
2. **Download Ubuntu:** Search for "Ubuntu Desktop ISO" and download it. Ubuntu is a free operating system (like Windows or macOS) that security professionals use.
3. **Create the Machine:** Open VirtualBox, click **"New"**, name it `Hunter-Trap`, and select the Ubuntu file you just downloaded. Follow the on-screen clicks to finish setting it up.
4. **Start the Machine:** Click "Start" in VirtualBox. You are now looking at a brand-new, isolated computer screen inside a window. **Do all of the following steps inside this new Ubuntu window.**

---

## Phase 2: Getting Your Tools Ready
Now that you are inside your safe Ubuntu computer, we need to open the "Terminal." The Terminal is simply a black box where you can type commands directly to the computer. 

1. **Open the Terminal:** Press `Ctrl` + `Alt` + `T` on your keyboard at the same time. A black window will pop up.
2. **Create a Folder for Our Trap:** Type the following command and press Enter:
   ```bash
   mkdir active-defense-tracker
   
```
3. **Go Inside the Folder:** Type this and press Enter:
   ```bash
   cd active-defense-tracker
   
```
4. **Download the Files:** You will need to save the files from this GitHub repository (`deploy_honeytokens.sh`, `ebpf_monitor.py`, `report_incident.py`, and `dashboard.html`) into this exact folder. You can do this by opening the web browser inside Ubuntu, coming to this GitHub page, clicking "Download ZIP", and then extracting it to your new folder.

---

## Phase 3: Installing the Required Software
Your new Ubuntu computer needs a few basic tools to read the traps we are setting.
Type the following exact text into your Terminal and press Enter (it may ask for the password you created when setting up Ubuntu):
```bash
sudo apt-get update
sudo apt-get install bcc-tools libbcc-examples linux-headers-$(uname -r) python3-bpfcc python3-pip
```
*(Wait for the computer to finish downloading and installing these tools. It might take a few minutes.)*

## Phase 4: Setting the Traps (Honeytokens)
We are going to create fake digital keys. When the hacker's malware steals these keys and tries to use them, we will get an alert with their location.
1. **In your Terminal**, make sure you are still in the active-defense-tracker folder.
2. We need to make the trap file "runnable." Type this and press Enter:
   ```bash
   chmod +x deploy_honeytokens.sh
   ```
3. **Set the Trap:** Type this and press Enter:
   ```bash
   ./deploy_honeytokens.sh
   ```
*(You should see a message on the screen saying the traps (AWS, GitHub, and SSH lures) have been successfully injected into the system.)*

## Phase 5: Turning on the Kernel Alarm (eBPF Monitor)
Now we turn on the deep-system alarm. This program watches the very core of the computer (the "Kernel") to see if the malware tries to trigger its wipe command (like rm -rf).
1. **In your Terminal**, type this command and press Enter:
   ```bash
   sudo python3 ebpf_monitor.py
   
```
*The screen will tell you the monitor is active. Leave this Terminal window open. It is now actively listening for attacks.*

---

## Phase 6: Deploying the Command Dashboard (HTML)
You have set the traps and turned on the alarm. Now, you need to open your visual Command Center to watch for activity. We have designed this so you do not need to set up a complicated web server. 

### The Easiest Way (Double-Click)
1. On your Ubuntu desktop, open your **Files** app (it looks like a manila folder icon).
2. Find the `active-defense-tracker` folder you created.
3. Inside, you will see the `dashboard.html` file.
4. **Double-click** `dashboard.html`. It will automatically open in your web browser. 

### The Professional Way (Local Server)
If you want to run it like a real web server, you can do this:
1. Open a **brand new** Terminal window (`Ctrl` + `Alt` + `T`). 
2. Go back to your folder by typing: 
   ```bash
   cd active-defense-tracker
   
```
3. Type the following command to start a simple web server:
   ```bash
   python3 -m http.server 8000
   
```
4. Open the web browser inside Ubuntu (like Firefox).
5. In the address bar at the top, type exactly this and press Enter:
   `http://localhost:8000/dashboard.html`

You will now see the red and black **DEFENSE COMMAND: ACTIVE TRACKING** dashboard. It is listening, watching, and ready to automatically report the hackers the moment they trip your wires.

### Phase 1: Building the Safe Room (Isolation)
Before doing anything else, you need to create your Virtual Machine.
1. **Download VirtualBox:** Go to the internet and search for "Oracle VirtualBox." Download and install it like any regular program. This is the software that builds the safe room.
2. **Download Ubuntu:** Search for "Ubuntu Desktop ISO" and download it. Ubuntu is a free operating system (like Windows or macOS) that security professionals use.
3. **Create the Machine:** Open VirtualBox, click **"New"**, name it `Hunter-Trap`, and select the Ubuntu file you just downloaded. Follow the on-screen clicks to finish setting it up.
4. **Start the Machine:** Click "Start" in VirtualBox. You are now looking at a brand-new, isolated computer screen inside a window. **Do all of the following steps inside this new Ubuntu window.**

---

## Phase 2: Getting Your Tools Ready
Now that you are inside your safe Ubuntu computer, we need to open the "Terminal." The Terminal is simply a black box where you can type commands directly to the computer. 

1. **Open the Terminal:** Press `Ctrl` + `Alt` + `T` on your keyboard at the same time. A black window will pop up.
2. **Create a Folder for Our Trap:** Type the following command and press Enter:
   ```bash
   mkdir active-defense-tracker
3. **Go Inside the Folder:** Type this and press Enter:
   ```bash
   cd active-defense-tracker
4. **Download the Files:** You will need to save the files from this GitHub repository (`deploy_honeytokens.sh`, `ebpf_monitor.py`, `report_incident.py`, and `dashboard.html`) into this exact folder. You can do this by opening the web browser inside Ubuntu, coming to this GitHub page, clicking "Download ZIP", and then extracting it to your new folder.

---

## Phase 3: Installing the Required Software
Your new Ubuntu computer needs a few basic tools to read the traps we are setting.
Type the following exact text into your Terminal and press Enter (it may ask for the password you created when setting up Ubuntu):
```bash
sudo apt-get update
sudo apt-get install bcc-tools libbcc-examples linux-headers-$(uname -r) python3-bpfcc python3-pip
(Wait for the computer to finish downloading and installing these tools. It might take a few minutes.)
## Phase 4: Setting the Traps (Honeytokens)
We are going to create fake digital keys. When the hacker's malware steals these keys and tries to use them, we will get an alert with their location.
1. **In your Terminal**, make sure you are still in the active-defense-tracker folder.
2. We need to make the trap file "runnable." Type this and press Enter:
```bash
chmod +x deploy_honeytokens.sh
3.**Set the Trap:** Type this and press Enter
```bash
./deploy_honeytokens.sh
(You should see a message on the screen saying the traps (AWS, GitHub, and SSH lures) have been successfully injected into the system.)
## Phase 5: Turning on the Kernel Alarm (eBPF Monitor)
Now we turn on the deep-system alarm. This program watches the very core of the computer (the "Kernel") to see if the malware tries to trigger its wipe command (like rm -rf).
1. **In your Terminal**, type this command and press Enter:
```bash
sudo python3 ebpf_monitor.py
*The screen will tell you the monitor is active. Leave this Terminal window open. It is now actively listening for attacks.*

---

## Phase 6: Deploying the Command Dashboard (HTML)
You have set the traps and turned on the alarm. Now, you need to open your visual Command Center to watch for activity. We have designed this so you do not need to set up a complicated web server. 

### The Easiest Way (Double-Click)
1. On your Ubuntu desktop, open your **Files** app (it looks like a manila folder icon).
2. Find the `active-defense-tracker` folder you created.
3. Inside, you will see the `dashboard.html` file.
4. **Double-click** `dashboard.html`. It will automatically open in your web browser. 

### The Professional Way (Local Server)
If you want to run it like a real web server, you can do this:
1. Open a **brand new** Terminal window (`Ctrl` + `Alt` + `T`). 
2. Go back to your folder by typing: 
   ```bash
   cd active-defense-tracker
3. Type the following command to start a simple web server:
```bash
python3 -m http.server 8000
4. Open the web browser inside Ubuntu (like Firefox).
5. In the address bar at the top, type exactly this and press Enter:
   `http://localhost:8000/dashboard.html`

You will now see the red and black **DEFENSE COMMAND: ACTIVE TRACKING** dashboard. It is listening, watching, and ready to automatically report the hackers the moment they trip your wires.






