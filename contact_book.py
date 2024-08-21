import tkinter as tk
from tkinter import ttk, messagebox
from views import *

co0 = "#ffffff"
co1 = "#000000"
co2 = "#000080"


root = tk.Tk()
root.title("Contact Book for CodeSoft")
root.geometry("485x460")
root.configure(bg=co0)
root.resizable(False, False)

frame1 = tk.Frame(root, width=500, height=50, bg=co2)
frame1.grid(row=0, column=0, padx=0, pady=1)

frame2 = tk.Frame(root, width=500, height=150, bg=co0)
frame2.grid(row=1, column=0, padx=0, pady=1)

frame3 = tk.Frame(root, width=500, height=100, bg=co0)
frame3.grid(row=2, column=0, columnspan=2, padx=0, pady=1)


def show():
    global tree
    for widget in frame3.winfo_children():
        widget.destroy()

    listheader = ["Name", "Email", "Phone Number"]
    demo_list = view() 

    if not demo_list: 
        empty_label = tk.Label(frame3, text="No contacts to display.", font=("poppins", 12), bg="white", fg="red")
        empty_label.grid(column=0, row=0, padx=10, pady=10)
        return

    tree = ttk.Treeview(frame3, selectmode="extended", columns=listheader, show='headings')

    v_scroll = ttk.Scrollbar(frame3, orient="vertical", command=tree.yview)
    h_scroll = ttk.Scrollbar(frame3, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
    tree.grid(column=0, row=0, sticky="nsew")
    v_scroll.grid(column=1, row=0, sticky="ns")
    h_scroll.grid(column=0, row=1, sticky="ew")

    tree.heading("Name", text="Name", anchor="nw")
    tree.column("Name", width=150, anchor="nw")

    tree.heading("Email", text="Email", anchor="nw")
    tree.column("Email", width=170, anchor="nw")

    tree.heading("Phone Number", text="Phone", anchor="nw")
    tree.column("Phone Number", width=130, anchor="nw")

    for item in demo_list:
        tree.insert('', 'end', values=item)

def insert():
    name = e_name.get()
    mail = email_entry.get()
    phone = phone_entry.get()

    data = [name, mail, phone]
    if name == '' or phone == '' or mail == '':
        messagebox.showwarning('Error', 'Please fill up all the data')
    else:
        add(data)
        messagebox.showinfo('Success', 'Your information was added successfully')

        e_name.delete(0, 'end')
        email_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')

    show()


def to_update():
    try:
        tree_data = tree.focus()
   
   
        tree_directory = tree.item(tree_data)
        tree_list = tree_directory['values']

        e_name.delete(0, 'end')
        email_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')

        name = str(tree_list[0])
        email = str(tree_list[1])
        phone = str(tree_list[2])

        e_name.insert(0, name)
        email_entry.insert(0, email)
        phone_entry.insert(0, phone)

        def confirm():
            new_name = e_name.get()
            new_email = email_entry.get()
            new_phone = phone_entry.get()

            data = [new_name, new_email, new_phone]

            update(data)
            messagebox.showinfo('Success', 'Your Data Updated Successfully')
            e_name.delete(0, 'end')
            email_entry.delete(0, 'end')
            phone_entry.delete(0, 'end')

            for widget in frame3.winfo_children():
                widget.destroy()

            b_confirm.destroy()

            show()

        b_confirm = tk.Button(frame2, text="Confirm", width=8, height=1, font="poppins 10", bg="green", fg="white", command=confirm)
        b_confirm.place(x=390, y=110)

    except IndexError:
        messagebox.showerror('Error', 'Select one of the items from the table')


def to_remove():
    try:
        tree_data = tree.focus()
        if not tree_data:
            raise IndexError

        tree_directory = tree.item(tree_data)
        tree_list = tree_directory['values']
        tree_phone = str(tree_list[2])

        remove(tree_phone)
        messagebox.showinfo('Success', 'Data has been deleted successfully')

        for widget in frame3.winfo_children():
            widget.destroy()
        show()

    except IndexError:
        messagebox.showerror('Error', 'Select one of the items from the table')


def to_search():
    phone = search_entry.get()

    data = search(phone)
    
    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('', 'end', values=item)

name_label = tk.Label(frame1, text="Contact Book", height=1, font="poppins 18 bold", fg=co0, bg=co2)
name_label.place(x=160, y=5)

l_name = tk.Label(frame2, text="Name:", width=10, height=1, font="poppins 10", bg=co0)
l_name.place(x=8, y=20)
e_name = tk.Entry(frame2, width=25, justify="left", highlightthickness=1, relief="solid")
e_name.place(x=80, y=20)

email_label = tk.Label(frame2, text="Email:", width=10, height=1, font="poppins 10", bg=co0)
email_label.place(x=8, y=50)
email_entry = tk.Entry(frame2, width=25, justify="left", highlightthickness=1, relief="solid")
email_entry.place(x=80, y=50)

phone_label = tk.Label(frame2, text="Phone:", width=10, height=1, font="poppins 10", bg=co0)
phone_label.place(x=8, y=80)
phone_entry = tk.Entry(frame2, width=25, justify="left", highlightthickness=1, relief="solid")
phone_entry.place(x=80, y=80)

search_button = tk.Button(frame2, text="Search", width=7, height=1, font="poppins 10", bg=co0, fg="black", command=to_search)
search_button.place(x=250, y=20)
search_entry = tk.Entry(frame2, width=20, justify="left", highlightthickness=1, relief="solid")
search_entry.place(x=330, y=22)

view_button = tk.Button(frame2, text="View", width=12, height=1, font="poppins 10", bg=co2, fg="white", command=show)
view_button.place(x=250, y=60)

add_button = tk.Button(frame2, text="Add", width=8, height=1, font="poppins 10", bg="Green", fg="white", command=insert)
add_button.place(x=390, y=50)

update_button = tk.Button(frame2, text="Update", width=8, height=1, font="poppins 10", bg="Green", fg="white", command=to_update)
update_button.place(x=390, y=80)

delete_button = tk.Button(frame2, text="Delete", width=12, height=1, font="poppins 10", bg="Red", fg="white", command=to_remove)
delete_button.place(x=250, y=100)


show()

root.mainloop()
