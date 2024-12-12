import os
import psutil
import tkinter as tk
from tkinter import ttk, messagebox

def refresh_process_list():
    """Refresh the process list in the GUI."""
    for row in tree.get_children():
        tree.delete(row)
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            tree.insert("", "end", values=(proc.info['pid'], proc.info['name']))
        except psutil.NoSuchProcess:
            continue

def kill_selected_process():
    """Kill the selected process."""
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "No process selected")
        return

    pid = tree.item(selected_item, 'values')[0]
    try:
        os.kill(int(pid), 9)
        messagebox.showinfo("Success", f"Process {pid} terminated successfully.")
        refresh_process_list()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to terminate process {pid}: {e}")

# Create main window
root = tk.Tk()
root.title("TaskTerminator")
root.geometry("600x400")

# Add a frame for the tree view and scrollbar
frame = ttk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Add a tree view to display the process list
columns = ("PID", "Name")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading("PID", text="PID")
tree.heading("Name", text="Name")
tree.column("PID", width=100, anchor="center")
tree.column("Name", width=400, anchor="w")

# Add a vertical scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)

scrollbar.pack(side="right", fill="y")
tree.pack(side="left", fill="both", expand=True)

# Add buttons for actions
button_frame = ttk.Frame(root)
button_frame.pack(fill="x", padx=10, pady=10)

refresh_button = ttk.Button(button_frame, text="Refresh", command=refresh_process_list)
refresh_button.pack(side="left", padx=5)

kill_button = ttk.Button(button_frame, text="Kill Process", command=kill_selected_process)
kill_button.pack(side="right", padx=5)

# Populate the initial process list
refresh_process_list()

# Run the main loop
root.mainloop()
