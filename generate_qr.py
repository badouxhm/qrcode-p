import customtkinter
from tkinter import *
def change_apparence(mot):
   customtkinter.set_appearance_mode(mot)


app = customtkinter.CTk()

menu_bar = Menu(app)

app.title("Génerateur de  QR code")
app.geometry("400x180")

app.config(menu=menu_bar)

apparence = Menu(menu_bar,tearoff=0)
apparence.add_command(label="system",command=lambda: change_apparence("system"))
apparence.add_command(label="dark",command=lambda: change_apparence("dark"))
apparence.add_command(label="light",command=lambda: change_apparence("light"))



menu_bar.add_cascade(label="Appaarences", menu=apparence)
menu_bar.add_command(label="Exit",command=app.quit)


label = customtkinter.CTkLabel(app, text="Gérateure de code QR",font=("arial",20), fg_color="transparent")
label.grid(row=0,column=0,padx=10,pady=(10,0))


entry = customtkinter.CTkEntry(app, placeholder_text="CTkEntry")
entry.grid(row=1,column=0,padx=10,pady=10 ,sticky="ns")
entry.configure(placeholder_text="Entrez votre lien")

lien = entry.get()   
print(lien) 

def voir_lien():
    lien = entry.get()   
    print(lien) 

button = customtkinter.CTkButton(app,fg_color="blue", command=voir_lien,text="Afficher le lien")
button.grid(row=2, column=0, padx=10, pady=10)

app.mainloop()