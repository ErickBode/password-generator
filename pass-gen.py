import customtkinter
import tkinter
import string
import random
import pyperclip
from tkinter import *

# Functions
def copy_password():
    pyperclip.copy(password_var.get())

def slider_event(value):
    text_var_s.set(f"{int(slider.get())}")

def checkbox_event():
    pass

def button_event(password_length):
    if (check_var_sym.get() == "off" and
        check_var_num.get() == "off" and
        check_var_low.get() == "off" and
        check_var_upper.get() == "off"):
        password_var.set("Need to select at least 1 checkbox.")
    else:
        characterList = ""
        if check_var_sym.get() == "on":
            characterList += string.punctuation
        if check_var_num.get() == "on":
            characterList += string.digits
        if check_var_low.get() == "on":
            characterList += string.ascii_lowercase
        if check_var_upper.get() == "on":
            characterList += string.ascii_uppercase

        # Generate password of specified length
        password = ''.join(random.choices(characterList, k=password_length))
        password_var.set(password)  # Update password label text



# Setting up the appearance mode and color theme
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# Create the customtkinter window
app = customtkinter.CTk()
app.title('Password Generator')
app.iconbitmap(r"assets\app-icon.ico")
app.geometry("1000x700")
app.resizable(False, False)

# Create the Frame of the window
frame = customtkinter.CTkFrame(master=app, corner_radius=10)
frame.pack(pady=20, padx=20, fill="both", expand=True)


# Start of Labels Section:
# Password Length
text_var_p = tkinter.StringVar(value="Password Length: ")
label_p = customtkinter.CTkLabel(master=frame,
                                 width=1200,
                                 height=25,
                                 textvariable=text_var_p,
                                 text_color="white",
                                 font=("Arial", 20),
                                 corner_radius=8)
label_p.place(relx=0.119, rely=0.05, anchor=tkinter.CENTER)

# Include Symbols
text_var_p = tkinter.StringVar(value="Include Symbols: ")
label_p = customtkinter.CTkLabel(master=frame,
                                 width=1200,
                                 height=25,
                                 textvariable=text_var_p,
                                 text_color="white",
                                 font=("Arial", 20),
                                 corner_radius=8)
label_p.place(relx=0.114, rely=0.12, anchor=tkinter.CENTER)

# Include Numbers
text_var_p = tkinter.StringVar(value="Include Numbers: ")
label_p = customtkinter.CTkLabel(master=frame,
                                 width=1200,
                                 height=25,
                                 textvariable=text_var_p,
                                 text_color="white",
                                 font=("Arial", 20),
                                 corner_radius=8)
label_p.place(relx=0.115, rely=0.19, anchor=tkinter.CENTER)

# Include Lowercase Characters
text_var_p = tkinter.StringVar(value="Include Lowercase Characters: ")
label_p = customtkinter.CTkLabel(master=frame,
                                 width=1200,
                                 height=25,
                                 textvariable=text_var_p,
                                 text_color="white",
                                 font=("Arial", 20),
                                 corner_radius=8)
label_p.place(relx=0.178, rely=0.26, anchor=tkinter.CENTER)

# Include Uppercase Characters
text_var_p = tkinter.StringVar(value="Include Uppercase Characters: ")
label_p = customtkinter.CTkLabel(master=frame,
                                 width=1200,
                                 height=25,
                                 textvariable=text_var_p,
                                 text_color="white",
                                 font=("Arial", 20),
                                 corner_radius=8)
label_p.place(relx=0.1779, rely=0.33, anchor=tkinter.CENTER)

# Your New Password
text_var_p = tkinter.StringVar(value="Your New Password: ")
label_p = customtkinter.CTkLabel(master=frame,
                                 width=1200,
                                 height=25,
                                 textvariable=text_var_p,
                                 text_color="white",
                                 font=("Arial", 20),
                                 corner_radius=8)
label_p.place(relx=0.14, rely=0.65, anchor=tkinter.CENTER)
# End of Labels Section.

# Start of Slider Section
slider = customtkinter.CTkSlider(master=frame,
                                 from_=10,
                                 to=30,
                                 number_of_steps=19,
                                 command=slider_event)
slider.place(relx=0.47, rely=0.052, anchor=tkinter.CENTER)

text_var_s = tkinter.StringVar(value="20")
label_s = customtkinter.CTkLabel(master=frame,
                                 width=50,
                                 height=25,
                                 textvariable=text_var_s,
                                 fg_color=("dark-gray", "gray"),
                                 text_color="white",
                                 font=("Arial", 19),
                                 corner_radius=6)
label_s.place(relx=0.61, rely=0.052, anchor=tkinter.CENTER)
# End of Slider Section.

# Start of Check Box Section
check_var_sym = tkinter.StringVar(value="on")
check_var_num = tkinter.StringVar(value="on")
check_var_low = tkinter.StringVar(value="on")
check_var_upper = tkinter.StringVar(value="on")

checkbox_sym = customtkinter.CTkCheckBox(master=frame,
                                         text="( @#$% )",
                                         font=("Arial", 15),
                                         command=checkbox_event,
                                         variable=check_var_sym,
                                         onvalue="on",
                                         offvalue="off")
checkbox_sym.place(relx=0.42, rely=0.12, anchor=tkinter.CENTER)

checkbox_num = customtkinter.CTkCheckBox(master=frame,
                                         text="( 123456 )",
                                         font=("Arial", 15),
                                         command=checkbox_event,
                                         variable=check_var_num,
                                         onvalue="on",
                                         offvalue="off")
checkbox_num.place(relx=0.42, rely=0.19, anchor=tkinter.CENTER)

checkbox_low = customtkinter.CTkCheckBox(master=frame,
                                         text="( abcdefgh )",
                                         font=("Arial", 15),
                                         command=checkbox_event,
                                         variable=check_var_low,
                                         onvalue="on",
                                         offvalue="off")
checkbox_low.place(relx=0.4242, rely=0.26, anchor=tkinter.CENTER)

checkbox_upper = customtkinter.CTkCheckBox(master=frame,
                                           text="( ABCDEFGH )",
                                           font=("Arial", 15),
                                           command=checkbox_event,
                                           variable=check_var_upper,
                                           onvalue="on",
                                           offvalue="off")
checkbox_upper.place(relx=0.434, rely=0.33, anchor=tkinter.CENTER)
# End of Check Box Section.

# Start of Button Section
button = customtkinter.CTkButton(master=frame,
                                 width=175,
                                 height=32,
                                 border_width=0,
                                 corner_radius=6,
                                 text="Generate Password",
                                 font=("Arial", 18),
                                 command=lambda: button_event(int(text_var_s.get())))
button.place(relx=0.458, rely=0.58, anchor=tkinter.CENTER)
# End of Button Section

# Entry to display generated password
password_var = tkinter.StringVar()
entry_password = customtkinter.CTkEntry(master=frame,
                                        width=380,
                                        font=("Arial", 20),
                                        text_color="white",
                                        textvariable=password_var,
                                        fg_color=("dark-gray", "gray"),
                                        corner_radius=8,
                                        state="readonly")
entry_password.place(relx=0.565, rely=0.65, anchor=tkinter.CENTER)

copy_button = customtkinter.CTkButton(master=frame,
                                      width=80,
                                      height=32,
                                      border_width=0,
                                      corner_radius=6,
                                      text="Copy",
                                      font=("Arial", 18),
                                      command=copy_password)
copy_button.place(relx=0.825, rely=0.65, anchor=tkinter.CENTER)

# Run the tkinter event loop
app.mainloop()
