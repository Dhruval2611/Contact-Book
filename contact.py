import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.configure(bg="#003C43")

        self.contacts = {}

        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="#003C43")
        self.frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        self.label = tk.Label(self.frame, text="Contact Book", bg="#003C43", fg="#E3FEF7", font=('Times New Roman', 24, 'bold'))
        self.label.pack(pady=10, fill=tk.X)
        
        self.name_entry = self.create_entry("Name")
        self.phone_entry = self.create_entry("Phone Number")
        self.email_entry = self.create_entry("Email")
        self.address_entry = self.create_entry("Address")

        self.add_btn = tk.Button(self.frame, text="Add Contact", command=self.add_contact, bg="#135D66", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'), borderwidth=0)
        self.add_btn.pack(pady=10, fill=tk.X)

        self.search_entry = self.create_entry("Search by Name or Phone")
        self.search_btn = tk.Button(self.frame, text="Search Contact", command=self.search_contact, bg="#135D66", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'), borderwidth=0)
        self.search_btn.pack(pady=10, fill=tk.X)
        
        self.contacts_listbox = tk.Listbox(self.frame, font=('Times New Roman', 18, 'bold'), bd=0, bg="#77B0AA", fg="#003C43")
        self.contacts_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.update_btn = tk.Button(self.frame, text="Update Contact", command=self.update_contact, bg="#135D66", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'), borderwidth=0)
        self.update_btn.pack(pady=10, fill=tk.X)
        
        self.delete_btn = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact, bg="#135D66", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'), borderwidth=0)
        self.delete_btn.pack(pady=10, fill=tk.X)
    
    def create_entry(self, placeholder):
        entry = tk.Entry(self.frame, font=('Times New Roman', 18, 'bold'), bd=0, bg="#77B0AA", fg="#003C43")
        entry.pack(pady=5, fill=tk.X)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event, entry=entry, placeholder=placeholder: self.on_focus_in(event, entry, placeholder))
        entry.bind("<FocusOut>", lambda event, entry=entry, placeholder=placeholder: self.on_focus_out(event, entry, placeholder))
        return entry

    def on_focus_in(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="#003C43")

    def on_focus_out(self, event, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="#003C43")

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone and email and address:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            self.update_contact_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "All fields must be filled out.")

    def search_contact(self):
        query = self.search_entry.get()
        if query:
            results = [name for name in self.contacts if query.lower() in name.lower() or query in self.contacts[name]['phone']]
            self.update_contact_list(results)
        else:
            messagebox.showwarning("Warning", "Search field must be filled out.")

    def update_contact(self):
        try:
            selected = self.contacts_listbox.get(self.contacts_listbox.curselection())
            name = selected.split(' | ')[0]
            if name in self.contacts:
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, name)
                self.phone_entry.delete(0, tk.END)
                self.phone_entry.insert(0, self.contacts[name]['phone'])
                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(0, self.contacts[name]['email'])
                self.address_entry.delete(0, tk.END)
                self.address_entry.insert(0, self.contacts[name]['address'])
                self.add_btn.config(text="Save Contact", command=self.save_contact)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a contact to update.")

    def save_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone and email and address:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            self.update_contact_list()
            self.clear_entries()
            self.add_btn.config(text="Add Contact", command=self.add_contact)
        else:
            messagebox.showwarning("Warning", "All fields must be filled out.")

    def delete_contact(self):
        try:
            selected = self.contacts_listbox.get(self.contacts_listbox.curselection())
            name = selected.split(' | ')[0]
            if name in self.contacts:
                del self.contacts[name]
                self.update_contact_list()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a contact to delete.")

    def update_contact_list(self, contacts=None):
        self.contacts_listbox.delete(0, tk.END)
        if contacts is None:
            contacts = self.contacts.keys()
        for name in contacts:
            contact = self.contacts[name]
            self.contacts_listbox.insert(tk.END, f"{name} | {contact['phone']}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.name_entry.insert(0, "Name")
        self.phone_entry.insert(0, "Phone Number")
        self.email_entry.insert(0, "Email")
        self.address_entry.insert(0, "Address")
        self.name_entry.config(fg="#003C43")
        self.phone_entry.config(fg="#003C43")
        self.email_entry.config(fg="#003C43")
        self.address_entry.config(fg="#003C43")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
