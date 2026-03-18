import time
import psutil
import os

def display_usage(cpu, mem, bars=50):
    cpu_percent = (cpu / 100.0)
    cpu_bar = '▌' * int(cpu_percent * bars) + '_' * (bars - int(cpu_percent * bars))

    mem_percent = (mem / 100.0)
    mem_bar = '▌' * int(mem_percent * bars) + '_' * (bars - int(mem_percent * bars))

    print(f"CPU usage: |{cpu_bar}| {cpu:.2f}%")
    print(f"Mem usage: |{mem_bar}| {mem:.2f}%\n")

def display_processes():
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            info = proc.info

            cpu = info.get('cpu_percent')
            if cpu is None:
                cpu = 0.0

            processes.append({
                'pid': info.get('pid'),
                'name': info.get('name') or "unknown",
                'cpu_percent': cpu
            })

        except:
            pass

   
    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)

    print("PID     NAME                CPU%")
    print("-----------------------------------")

    for p in processes[:10]:
        print(f"{p['pid']:<7} {p['name'][:18]:<18} {p['cpu_percent']:<5}")

while True:
    os.system('clear')  # clears screen

    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent

    display_usage(cpu, mem)
    display_processes()

    time.sleep(0.5)  