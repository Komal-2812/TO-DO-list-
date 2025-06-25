import tkinter as tk
from tkinter import messagebox

FILENAME = "todo.txt"

# Load tasks from file with utf-8 encoding
def load_tasks():
    try:
        with open(FILENAME, "r", encoding='utf-8') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

# Save tasks to file with utf-8 encoding
def save_tasks():
    try:
        tasks = task_listbox.get(0, tk.END)
        if tasks:
            with open(FILENAME, "w", encoding='utf-8') as f:
                for task in tasks:
                    f.write(task + "\n")
        else:
            # Clear the file if no tasks
            open(FILENAME, "w", encoding='utf-8').close()
    except Exception as e:
        messagebox.showerror("Error", f"Could not save tasks:\n{e}")

# Add task
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, "📝 " + task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("⚠️ Warning", "Please enter a task.")

# Remove selected task
def remove_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
    else:
        messagebox.showwarning("⚠️ Warning", "Please select a task to remove.")

# Exit and save
def exit_app():
    save_tasks()
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("🗒️ To-Do List App")
root.state('zoomed')

# Top Frame
top_frame = tk.Frame(root)
top_frame.pack(pady=10, padx=10, fill='x')

task_entry = tk.Entry(top_frame, font=('Arial', 16))
task_entry.pack(fill='x', expand=True, padx=10)

# Middle Frame
middle_frame = tk.Frame(root)
middle_frame.pack(padx=10, pady=10, expand=True, fill='both')

task_listbox = tk.Listbox(middle_frame, font=('Arial', 16), selectbackground="lightblue")
task_listbox.pack(side='left', fill='both', expand=True)

scrollbar = tk.Scrollbar(middle_frame)
scrollbar.pack(side='right', fill='y')
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Bottom Frame
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

add_btn = tk.Button(bottom_frame, text="➕ Add Task", font=('Arial', 14), width=20, command=add_task)
add_btn.pack(side='left', padx=10)

remove_btn = tk.Button(bottom_frame, text="❌ Remove Task", font=('Arial', 14), width=20, command=remove_task)
remove_btn.pack(side='left', padx=10)

exit_btn = tk.Button(bottom_frame, text="🚪 Exit", font=('Arial', 14), width=20, command=exit_app)
exit_btn.pack(side='left', padx=10)

# Load existing tasks at startup
for task in load_tasks():
    task_listbox.insert(tk.END, task)

# Save tasks when window closes
root.protocol("WM_DELETE_WINDOW", exit_app)

# Start GUI loop
root.mainloop()
