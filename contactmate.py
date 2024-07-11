import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}
        self.groups = {}

        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack()
        self.frame4 = tk.Frame(self.root)
        self.frame4.pack()

        self.name_label = tk.Label(self.frame1, text="Name:")
        self.name_label.pack(side=tk.LEFT)
        self.name_entry = tk.Entry(self.frame1, width=20)
        self.name_entry.pack(side=tk.LEFT)

        self.phone_label = tk.Label(self.frame1, text="Phone:")
        self.phone_label.pack(side=tk.LEFT)
        self.phone_entry = tk.Entry(self.frame1, width=20)
        self.phone_entry.pack(side=tk.LEFT)

        self.group_label = tk.Label(self.frame1, text="Group:")
        self.group_label.pack(side=tk.LEFT)
        self.group_entry = tk.Entry(self.frame1, width=20)
        self.group_entry.pack(side=tk.LEFT)

        self.reminder_label = tk.Label(self.frame1, text="Reminder:")
        self.reminder_label.pack(side=tk.LEFT)
        self.reminder_entry = tk.Entry(self.frame1, width=20)
        self.reminder_entry.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.frame2, text="Add Contact", command=self.add_contact)
        self.add_button.pack(side=tk.LEFT)
        self.delete_button = tk.Button(self.frame2, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(side=tk.LEFT)
        self.search_button = tk.Button(self.frame2, text="Search Contact", command=self.search_contact)
        self.search_button.pack(side=tk.LEFT)
        self.update_button = tk.Button(self.frame2, text="Update Contact", command=self.update_contact)
        self.update_button.pack(side=tk.LEFT)

        self.listbox = tk.Listbox(self.frame3, width=40)
        self.listbox.pack()

        self.group_listbox = tk.Listbox(self.frame4, width=20)
        self.group_listbox.pack(side=tk.LEFT)
        self.group_button = tk.Button(self.frame4, text="Create Group", command=self.create_group)
        self.group_button.pack(side=tk.LEFT)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        group = self.group_entry.get()
        reminder = self.reminder_entry.get()
        if name and phone:
            self.contacts[name] = {"phone": phone, "group": group, "reminder": reminder}
            self.listbox.insert(tk.END, name)
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.group_entry.delete(0, tk.END)
            self.reminder_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def delete_contact(self):
        selected = self.listbox.curselection()
        if selected:
            name = self.listbox.get(selected)
            del self.contacts[name]
            self.listbox.delete(selected)
        else:
            messagebox.showerror("Error", "Please select a contact to delete")

    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.contacts[name]["phone"]
            group = self.contacts[name]["group"]
            reminder = self.contacts[name]["reminder"]
            messagebox.showinfo("Contact Info", f"Phone: {phone}\nGroup: {group}\nReminder: {reminder}")
        else:
            messagebox.showerror("Error", "Contact not found")

    def update_contact(self):
        selected = self.listbox.curselection()
        if selected:

           name = self.listbox.get(selected)
           new_phone = self.phone_entry.get()
           new_group = self.group_entry.get()
           new_reminder = self.reminder_entry.get()
           if new_phone and new_group and new_reminder:
                self.contacts[name] = {"phone": new_phone, "group": new_group, "reminder": new_reminder}
                messagebox.showinfo("Success", "Contact updated successfully")
                self.phone_entry.delete(0, tk.END)
                self.group_entry.delete(0, tk.END)
                self.reminder_entry.delete(0, tk.END)
           else:
                messagebox.showerror("Error", "Please fill in all fields")
        else:
            messagebox.showerror("Error", "Please select a contact to update")

    def create_group(self):
        group_name = self.group_entry.get()
        if group_name:
            if group_name not in self.groups:
                self.groups[group_name] = []
                self.group_listbox.insert(tk.END, group_name)
                self.group_entry.delete(0, tk.END)
                messagebox.showinfo("Success", f"Group '{group_name}' created successfully")
            else:
                messagebox.showerror("Error", "Group already exists")
        else:
            messagebox.showerror("Error", "Please enter a group name")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
