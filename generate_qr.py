import customtkinter
import qrcode
from tkinter import *
from PIL import Image, ImageTk

def change_apparence(mot):
   customtkinter.set_appearance_mode(mot)

app = customtkinter.CTk()
app.grid_columnconfigure(0, weight=1)
menu_bar = Menu(app)

app.title("Générateur de QR code")
app.geometry("400x380")
app.config(menu=menu_bar)

apparence = Menu(menu_bar, tearoff=0)
apparence.add_command(label="system", command=lambda: change_apparence("system"))
apparence.add_command(label="dark", command=lambda: change_apparence("dark"))
apparence.add_command(label="light", command=lambda: change_apparence("light"))

menu_bar.add_cascade(label="Apparences", menu=apparence)
menu_bar.add_command(label="Exit", command=app.quit)

label = customtkinter.CTkLabel(app, text="Générateur de code QR", font=("Arial", 20), fg_color="transparent")
label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

entry = customtkinter.CTkEntry(app, placeholder_text="Entrez votre lien")
entry.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

def voir_lien():
    lien = entry.get()
    if lien:
        img = qrcode.make(lien)
        img.save("./qr.png")
        
        image = Image.open("./qr.png")
        image = image.resize((200, 200))
        QRcode = customtkinter.CTkImage(dark_image=image,size=(200,200))
        
        label2.configure(image=QRcode)
        label2.image = QRcode

button = customtkinter.CTkButton(app, fg_color="blue", command=voir_lien, text="Afficher le QR code")
button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

label2 = customtkinter.CTkLabel(app, text="")
label2.grid(pady=10, sticky="nsew")

app.mainloop()
