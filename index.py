import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please add a task.")

def delete_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete.")

def mark_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.itemconfig(task_index, bg ="light gray")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task that can be marked completed.")


#Main Window
root = tk.Tk()
root.title("JJ To-Do List")

#Task entry
entry_task = tk.Entry(root, width=50)
entry_task.grid(row=0, column=0, padx=5, pady=5)

#Add button
button_add = tk.Button(root, text="Add Task", width=42, command=add_task)
button_add.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

#Task List
listbox_task = tk.Listbox(root, height=15, width=50)
listbox_task.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

#Delete button
button_delete = tk.Button(root, text="Delete task", width=20, command=delete_task)
button_delete.grid(row=2, column=0, padx=5, pady=5)

#Complete button
button_mark = tk.Button(root, text="Mark as completed", width=20, command=mark_task)
button_mark.grid(row=2, column=1, padx=5, pady=5)

#Event loop
root.mainloop()