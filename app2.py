import tkinter as tk
from tkinter import messagebox

def calculate_waiting_time():
    try:
        people = int(people_entry.get())
        counters = int(counters_entry.get())
        minutes = float(minutes_entry.get())

        if people < 0 or counters <= 0 or minutes <= 0:
            messagebox.showerror("Error", "Please enter valid numbers.")
            return

        waiting_time = (people * minutes) / counters

        result_label.config(
            text=f"Estimated Waiting Time: {waiting_time:.0f} minutes"
        ) 

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only.")


# Create window
window = tk.Tk()
window.title("QueueLess AI")
window.geometry("500x400")

# Title
title = tk.Label(
    window,
    text="QueueLess AI",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

subtitle = tk.Label(
    window,
    text="Estimate your waiting time",
    font=("Arial", 12)
)
subtitle.pack(pady=5)

# People
tk.Label(window, text="People ahead:").pack(pady=5)

people_entry = tk.Entry(window)
people_entry.pack()

# Counters
tk.Label(window, text="Number of counters:").pack(pady=5)

counters_entry = tk.Entry(window)
counters_entry.pack()

# Minutes
tk.Label(window, text="Average minutes per person:").pack(pady=5)

minutes_entry = tk.Entry(window)
minutes_entry.pack()

# Button
calculate_button = tk.Button(
    window,
    text="Estimate Waiting Time",
    command=calculate_waiting_time
)
calculate_button.pack(pady=20)

# Result
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=10)

# Start application
window.mainloop()