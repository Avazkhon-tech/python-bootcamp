from tkinter import Canvas, Entry, Tk, Label, Button, PhotoImage, messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ([choice(letters) for _ in range(randint(8,10))] +
                [choice(symbols) for _ in range(randint(2,4))] +
                [choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password)
    password_new = ''.join(password)
    password_entry.insert(0, password_new)
    pyperclip.copy(password_new)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_entry_input = website_entry.get()
    username_entry_input = username_entry.get()
    password_entry_input = password_entry.get()
    new_data = {
        website_entry_input: {
            'email': username_entry_input,
            'password': password_entry_input,
        }
    }
    if len(website_entry_input) == 0 or len(username_entry_input) == 0 or len(password_entry_input) == 0:
        messagebox.showinfo(title="Warning", message="Please make sure you have not left any of the spaces empty.")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- LOOK FOR PASSWORD ------------------------------- #
def find_password():
    try:
        website = website_entry.get()
        with open("data.json", 'r') as file:
            data = json.load(file)
        code = (data[website]['password'])
        email = (data[website]['email'])
        messagebox.showinfo(title=website, message=f'Email/Username: {email}\n'
                                                   f'Password: {code}')
    except FileNotFoundError:
        messagebox.showinfo(title='warning', message='no data file found.')
    except KeyError:
        messagebox.showinfo(title=website, message=f'no info has been found for this website')


# ---------------------------- UI SETUP -------------------------------


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=img_logo)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry_info = website_entry.get()


username_entry = Entry(width=53)
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# buttons
generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()