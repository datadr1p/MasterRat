<div align="center">
  <img src="https://readme-typing-svg.demolab.com/?font=Roboto+Slab&pause=1000&color=0e37eff&center=true&random=true&lines=Master+Rat;%26" width="55%" />
  <br><br>
  <div style="background-color: black; color: #00FF00; padding: 20px; border-radius: 5px; font-family: 'Courier New', monospace;">

    <p>🔎 MasterRat permet de prendre l'accès au pc d'une victime à distance.</p>
    
    <p><button class="copy-btn" data-command="+sys">💻 +sys - Afficher les informations du PC</button></p>
    <p><button class="copy-btn" data-command="+clear">🧹 +clear - Effacer les logs du MasterRat</button></p>
    <p><button class="copy-btn" data-command="+disable_wd">🛡️ +disable_wd - Désactiver Windows Defender</button></p>
    <p><button class="copy-btn" data-command="+screenshot">📷 +screenshot - Prendre une capture d'écran du PC</button></p>
    <p><button class="copy-btn" data-command="+video">📹 +video - Enregistrer une vidéo depuis le PC de la victime</button></p>
    <p><button class="copy-btn" data-command="+cam">📷 +cam - Prendre une photo de la caméra</button></p>
    <p><button class="copy-btn" data-command="+listen">👻 +listen - Met le pc sous écoute</button></p>
    <p><button class="copy-btn" data-command="+installer">🪲 +installer - Installer et ouvrir des fichiers</button></p>
    <p><button class="copy-btn" data-command="+reverse_ps">🖥️ +reverse_ps - Session PowerShell inversée</button></p>
    <p><button class="copy-btn" data-command="+reverse_cmd">🖥️ +reverse_cmd - Session Command Prompt inversée</button></p>
    <p><button class="copy-btn" data-command="+keylogger">⌨️ +keylogger - Keylogger avancé</button></p>
    <p><button class="copy-btn" data-command="+ghost">👻 +ghost - Envoie des msgbox discrètes comme un fantôme</button></p>
    <p><button class="copy-btn" data-command="+Bipper">🚨 +Bipper - Fait bipper le pc</button></p>
    <p><button class="copy-btn" data-command="+close_process">❌ +close_process - Ferme tous les programmes</button></p>
    <p><button class="copy-btn" data-command="+wallpaper">☘️ +wallpaper - Fait entendre une voix dans le pc</button></p>
  
  </div>
</div>

<script>
  document.querySelectorAll('.copy-btn').forEach(button => {
    button.addEventListener('click', function() {
      const command = this.getAttribute('data-command');
      navigator.clipboard.writeText(command).then(() => {
        alert('Commande copiée : ' + command);
      });
    });
  });
</script>
