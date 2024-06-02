import tkinter as tk
import time

# Function to update the time
def time_update():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, time_update)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
clock_label.pack(anchor='center')

# Start the clock
time_update()

# Run the application
root.mainloop()
