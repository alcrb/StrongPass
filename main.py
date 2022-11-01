'''
Strong Pass is a Random Password Generator using Python
Author: Alex C
'''

import string
from random import randint, choice
from tkinter import*

#Créer une 1ère fenetre
window = Tk()

#
def generate_password():
    password_mini= 8
    password_max= 24
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range (randint(password_mini, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


#Personnaliser cette fenetre
window.title("StrongPass")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background='#1E191A')

#Créer la frame principale
frame = Frame(window, bg='#1E191A')

#Création d'image
width = 300
height = 300
image = PhotoImage(file="password_onboarding.png")
canvas= Canvas(frame, width=width, height=height, bg='#1E191A', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#Creer une sous-boite
right_frame= Frame(frame, bg='#1E191A')

# Creer un titre
label_title = Label(right_frame, text="Password", font=("Helvetica", 20), bg='#1E191A', fg='white')
label_title.pack()

# Creer un champ
password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#1E191A', fg='white')
password_entry.pack()

# Creer un bouton
generate_password_button = Button(right_frame, text="Generate", font=("Helvetica", 20), bg='#1E191A', fg='white', command=generate_password)
generate_password_button.pack(fill=X)

#On place la sous-boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

#Afficher la frame
frame.pack(expand=YES)

# Afficher le GUI
window.mainloop()