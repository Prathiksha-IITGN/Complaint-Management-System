#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk

complaints = []

def new_complaint():
    name = name_entry.get()
    email = email_entry.get()
    issue = issue_entry.get()
    complaints.append((name, email, issue))
    status_label.config(text="Complaint registered successfully")

def view_complaints():
    if len(complaints) == 0:
        status_label.config(text="No complaints registered yet")
    else:
        text = "List of complaints:\n"
        for i, c in enumerate(complaints):
            text += str(i+1) + " Name: " + c[0] + "\tEmail: " + c[1] + "\tIssue: " + c[2] + "\n"
        status_label.config(text=text)

def search_complaints():
    keyword = keyword_entry.get()
    result = []
    for c in complaints:
        if keyword in c[2]:
            result.append(c)
    if len(result) == 0:
        status_label.config(text="No complaints found")
    else:
        text = "List of complaints:\n"
        for i, c in enumerate(result):
            text += str(i+1) + " Name: " + c[0] + "\tEmail: " + c[1] + "\tIssue: " + c[2] + "\n"
        status_label.config(text=text)

# Create the main window
root = tk.Tk()
root.title("Complaint Management System")

# Create the input fields and buttons
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)
email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root)
issue_label = tk.Label(root, text="Issue:")
issue_entry = tk.Entry(root)
new_button = tk.Button(root, text="Register New Complaint", command=new_complaint)
keyword_label = tk.Label(root, text="Search keyword:")
keyword_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search Complaints", command=search_complaints)
view_button = tk.Button(root, text="View All Complaints", command=view_complaints)
status_label = tk.Label(root, text="")

# Add the input fields and buttons to the window
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1)
issue_label.grid(row=2, column=0)
issue_entry.grid(row=2, column=1)
new_button.grid(row=3, column=0, columnspan=2)
keyword_label.grid(row=4, column=0)
keyword_entry.grid(row=4, column=1)
search_button.grid(row=5, column=0, columnspan=2)
view_button.grid(row=6, column=0, columnspan=2)
status_label.grid(row=7, column=0, columnspan=2)

# Start the main loop
root.mainloop()


# In[ ]:




