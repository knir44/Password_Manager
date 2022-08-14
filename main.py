from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json



# ---------------------------- Const ------------------------------- #
FONT = ("Arial",15)
FONT_button = ("Arial",10)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_new_password():
    password_entry.delete(0, END)
    password_entry.insert(0, "")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list  = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password ="".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_data():
    website_entry.delete(0, END)
    website_entry.insert(0,"")

    password_entry.delete(0, END)
    password_entry.insert(0, "")


def save():


    password = password_entry.get()
    website = website_entry.get()
    email = user_name_entry.get()

    if len(website) < 1 or len(password) < 1:
        messagebox.showerror(title = "Invild data",message="Please dont leave fields empty!")
        return

    else:
        dict_web = {
            website:
                {
                    "email":email,
                    "password":password
                }

        }
        try:
            with open("data.json", "r") as text:
                data = json.load(text)
                data.update(dict_web)

                with open("data.json", "w") as text:
                    json.dump(data, text, indent=4)
        except:
            with open("data.json", "w") as text:
                json.dump(dict_web, text, indent=4)



    clear_data()


def find_password():
    try:
        with open("data.json", "r") as text:
            data = json.load(text)
        email = website_entry.get()


        if email in data:
            messagebox.showinfo(title= f"{email}", message=f"email: {data[email]['email']}\n password: {data[email]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No data file found")

    except:
        messagebox.showinfo(title="Error", message="No data file found")
# ---------------------------- UI SETUP ------------------------------- #
# ---------------------------- window ------------------------------- #
window = Tk()
window.config(padx=50,pady=50)
window.title("Password Manager")
# window.minsize(width=500,height=500)

# ---------------------------- canvas ------------------------------- #
canvas = Canvas(width= 200,height=200)
logo_img = PhotoImage(file ="logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row =0,column=1)


# ---------------------------- website------------------------------- #

website_label = Label(text="Website",font=FONT)
website_label.grid(row=1,column=0)
website_entry = Entry(width=35)
website_entry.grid(columnspan=2,row=1,column=1)
website_entry.focus()



# ---------------------------- user_name ------------------------------- #

user_name_label = Label(text="Email/Username: ",font = FONT)
user_name_label.grid(row=2,column=0)
user_name_entry = Entry(width=35)
user_name_entry.grid(columnspan=2,row=2,column=1)
user_name_entry.insert(0,"knir44@gmail.com")

# ---------------------------- password ------------------------------- #

password_label = Label(text="Password",font = FONT)
password_label.grid(row=3,column=0)
password_entry = Entry(width=35)
password_entry.grid(columnspan=2,row=3,column=1)


# ---------------------------- generate_password ------------------------------- #

generate_password_button = Button(text="Generate Password",font=FONT_button,command=generate_new_password)
generate_password_button.grid(row=3,column=3)

# ---------------------------- add ------------------------------- #

add_button = Button(width=28,text="Add",font=FONT_button,command=save)
add_button.grid(columnspan=2,row = 4,column=1)

# ---------------------------- Search ------------------------------- #
add_button = Button(width=14,text="Search",font=FONT_button,command=find_password)
add_button.grid(row = 1,column=3)







window.mainloop()


