#!/usr/bin/env python3
# Description: eBPF script to monitor kernel-level execution of destructive commands.
# Requires root privileges to run.

from bcc import BPF
import time
import subprocess

print("[*] Compiling eBPF program... (This may take a moment)")

# eBPF program written in C
bpf_text = """
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>
#include <linux/fs.h>

BPF_PERF_OUTPUT(events);

struct data_t {
    u32 pid;
    char comm[TASK_COMM_LEN];
};

int trace_execve(struct pt_regs *ctx) {
    struct data_t data = {};
    data.pid = bpf_get_current_pid_tgid() >> 32;
    bpf_get_current_comm(&data.comm, sizeof(data.comm));
    
    // Only capture 'rm' commands to minimize noise
    if (data.comm[0] == 'r' && data.comm[1] == 'm') {
        events.perf_submit(ctx, &data, sizeof(data));
    }
    return 0;
}
"""

try:
    b = BPF(text=bpf_text)
    # Hook the execve system call
    execve_fnname = b.get_syscall_fnname("execve")
    b.attach_kprobe(event=execve_fnname, fn_name="trace_execve")
except Exception as e:
    print(f"[!] Failed to attach eBPF. Are you running as root? Error: {e}")
    exit(1)

def trigger_alert(pid, comm):
    print(f"\n[!!!] ALERT: Destructive command detected!")
    print(f"[!!!] Process ID: {pid} | Command: {comm}")
    print(f"[!!!] Triggering automated incident report...\n")
    # Call the reporting script
    subprocess.Popen(["python3", "report_incident.py", str(pid), comm])

def print_event(cpu, data, size):
    event = b["events"].event(data)
    comm = event.comm.decode('utf-8', 'replace')
    trigger_alert(event.pid, comm)

print("[*] eBPF Monitor Active. Watching for destructive commands (e.g., rm -rf)...")
print("[*] Press Ctrl+C to exit.")

b["events"].open_perf_buffer(print_event)

while True:
    try:
        b.perf_buffer_poll()
    except KeyboardInterrupt:
        print("\n[*] Exiting eBPF Monitor.")
        exit()
      
