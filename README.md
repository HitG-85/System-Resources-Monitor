# System Resource Monitor (CLI)

This project is a terminal-based application that displays real-time system resource usage.

It shows:
- CPU usage
- Memory usage
- Running processes
- CPU usage of processes

The application updates continuously in the terminal to provide a live view of system performance.

---

# Screenshots
  OUTPUT: 
<img width="1016" height="428" alt="image" src="https://github.com/user-attachments/assets/8bfd482e-19e2-46c2-9f67-09f7de322f61" />


---

# How to Run

1. Install psutil: pip install psutil
2. Run the code: python3 monitor.py

---

# Design Decisions

- Used Python for fast development and simplicity.
- Used psutil library to fetch system data.
- Implemented a continuous loop for real-time updates.
- Used text-based progress bars for better visualization.
- Sorted processes by CPU usage to show the most active ones.
- Kept the UI minimal and readable for terminal use.


