import tkinter as tk
from tkinter.constants import CENTER
from tkinter.font import Font
import pass_gen_v2 as PG
import pyperclip

# Main window
window = tk.Tk()
window.resizable(0,0)
window.geometry("400x200")
window.configure(bg="#5D5F60")#BBBBBD
window.attributes('-alpha', 0.95)
window.title("Password Ganaretor")

# Text

label2 = tk.Label(window, text="Length",font=Font(family='Helvetica', size=26, weight='bold'),bg="#5D5F60",fg="#FF9F0B")
label2.place(x=15, y=80)

pass_gen_text = tk.StringVar()
pass_gen_text.set("Generated Password")

label3 =tk.Label(window, textvariable=pass_gen_text, bg="#7F7F80",fg="#FF9F0B", width=28, height=2,font=Font(family='Helvetica', size=26, weight='bold'))
label3.grid(column=0, row=0, columnspan=3)

label_blanc = tk.Label(window, height=6)

# User input field
lenth = tk.Spinbox(window, from_=4, to=100,bg="#5D5F60",fg="#FF9F0B" ,font=Font(family='Helvetica', size=56, weight='bold'), width=4, justify=CENTER)
lenth.place(x=15, y=115)

# Buttons
def pass_print():
    gentd_pass = PG.password_generator(int(lenth.get()))
    pass_gen_text.set(gentd_pass)
    

def pass_copy():
    pyperclip.copy(pass_gen_text.get())


gen_button = tk.Button(window, text="Gen", width=14, height=2,fg="#FF9F0B", command=lambda: pass_print(),font=Font(family='Helvetica', size=22, weight='bold'))
gen_button.place(x=205, y=80)

copy_button = tk.Button(window, text="Copy", width=14, height=2,fg="#FF9F0B", command=lambda: pass_copy(),font=Font(family='Helvetica', size=22, weight='bold'))
copy_button.place(x=205, y=140)


# Main loop
window.mainloop()