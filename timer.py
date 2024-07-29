import time
import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")

        self.time_left_var = tk.StringVar()
        self.time_left_var.set("00:00:00")

        self.label = tk.Label(root, text="Enter time in H:M:S", font=("Helvetica", 16))
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.time_display = tk.Label(root, textvariable=self.time_left_var, font=("Helvetica", 48))
        self.time_display.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack()

        self.is_paused = False
        self.total_seconds = 0
        self.remaining_seconds = 0

    def start_timer(self):
        time_str = self.entry.get()
        try:
            h, m, s = map(int, time_str.split(":"))
            self.total_seconds = h * 3600 + m * 60 + s
            self.remaining_seconds = self.total_seconds
            self.countdown()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter time in H:M:S format")

    def countdown(self):
        if self.remaining_seconds > 0 and not self.is_paused:
            self.remaining_seconds -= 1
            h, remainder = divmod(self.remaining_seconds, 3600)
            m, s = divmod(remainder, 60)
            self.time_left_var.set(f"{h:02}:{m:02}:{s:02}")
            self.root.after(1000, self.countdown)
        elif self.remaining_seconds == 0:
            messagebox.showinfo("Time's up", "Time's up!")
            self.reset_timer()

    def pause_timer(self):
        self.is_paused = not self.is_paused
        if not self.is_paused:
            self.countdown()

    def reset_timer(self):
        self.remaining_seconds = self.total_seconds
        h, remainder = divmod(self.remaining_seconds, 3600)
        m, s = divmod(remainder, 60)
        self.time_left_var.set(f"{h:02}:{m:02}:{s:02}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
