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
   
