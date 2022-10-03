from tkinter import *
from tkinter import messagebox
import password
import json

# Write : json.dump()     Read: json.load()       Update: json.update()

# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
generate_pass = ""


def get_generate_pass():
    global generate_pass
    generate_pass = password.generate_pass()
    entry_password.delete(0, END)
    entry_password.insert(0, generate_pass)


# #-----------------------------------FIND PASSWORD-----------------------------#
def find_password():
    key_find = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data_account = data[key_find]
            messagebox.showinfo(title=f"Your account {key_find}", message=f"{data[key_find]}")

    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message="No Data File Found")

# # ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get()
    email = entry_email_username.get()
    password_save = entry_password.get()
    new_data = {website: {
        "email": email,
        "password": password_save
    }}

    if len(website) == 0 or len(password_save) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
img_logo = PhotoImage(file="demonstrator.png")
canvas.create_image(100, 100, image=img_logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("HackNF", 12, "normal"))
website_label.grid(column=0, row=1)

Email_Username = Label(text="Email/Username:", font=("HackNF", 12, "normal"))
Email_Username.grid(column=0, row=2)

Password = Label(text="Password:", font=("HackNF", 12, "normal"))
Password.grid(column=0, row=3)

# Entries
entry_website = Entry(width=43)
entry_website.grid(column=1, row=1, sticky='w')
entry_website.focus()

entry_email_username = Entry(width=43)
entry_email_username.grid(column=1, row=2, columnspan=2, sticky='w')
entry_email_username.insert(0, "congtue.hust@gmail.com")

entry_password = Entry(width=40)
entry_password.grid(column=1, row=3, sticky='w')

# Buttons
button_search = Button(text="Search", width=10, command=find_password)
button_search.grid(column=2, row=1)

button_generate_password = Button(text="Generate Password", width=18, command=get_generate_pass)
button_generate_password.grid(column=2, row=3)

button_Add = Button(text="Add", width=10, command=save)
button_Add.grid(column=1, row=4, columnspan=2, sticky='w')

# Graphic
window.mainloop()
