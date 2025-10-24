# 🚀 GITHUB SETUP ANLEITUNG

Komplette Anleitung zum Einrichten des Diamond Digger Spiels auf GitHub.

---

## 📋 VORAUSSETZUNGEN

- ✅ GitHub Account
- ✅ Git installiert (optional, für Kommandozeile)
- ✅ Alle Spiel-Dateien verfügbar

---

## 🌐 METHODE 1: WEB-INTERFACE (EINFACH)

### Schritt 1: Repository erstellen

1. Gehe zu [GitHub](https://github.com)
2. Klicke auf **"+" → "New repository"**
3. Einstellungen:
   ```
   Repository name: Diamond-Digger
   Description: Ein Boulder Dash-Klon mit Highscore-System
   Public: ✅ (wichtig für GitHub Pages!)
   Initialize: ☐ Kein README (wir haben schon eins)
   ```
4. Klicke **"Create repository"**

### Schritt 2: Dateien hochladen

1. Im neuen Repository klicke **"uploading an existing file"**
2. Wähle ALLE Dateien aus:
   ```
   ✅ index.html
   ✅ level_editor.html
   ✅ README.md
   ✅ LICENSE
   ✅ CONTRIBUTING.md
   ✅ CHANGELOG.md
   ✅ .gitignore
   ```
3. Klicke **"Commit changes"**

### Schritt 3: Ordner erstellen & Dateien hochladen

#### Level-Ordner:
1. Klicke **"Add file" → "Create new file"**
2. Im Dateinamen-Feld schreibe: `level/level_01.json`
3. Füge Inhalt von level_01.json ein
4. Klicke **"Commit new file"**
5. Wiederhole für level_02.json und level_03.json

#### Img-Ordner:
1. Klicke **"Add file" → "Upload files"**
2. Im Pfad-Feld schreibe: `img/`
3. Wähle Menu.png
4. Klicke **"Commit changes"**

#### Docs-Ordner:
1. Erstelle `docs/` Ordner (wie oben)
2. Lade Dokumentations-Dateien hoch

### Schritt 4: GitHub Pages aktivieren

1. Gehe zu **"Settings" → "Pages"**
2. Einstellungen:
   ```
   Source: Deploy from a branch
   Branch: main
   Folder: / (root)
   ```
3. Klicke **"Save"**
4. Warte 2-5 Minuten
5. Spiel ist verfügbar unter:
   ```
   https://DEIN-USERNAME.github.io/Diamond-Digger/
   ```

---

## 💻 METHODE 2: GIT KOMMANDOZEILE (FORTGESCHRITTEN)

### Schritt 1: Repository erstellen

```bash
# Auf GitHub neues Repository erstellen (siehe Methode 1, Schritt 1)
# Dann lokal:

cd pfad/zu/deinen/dateien
git init
git add .
git commit -m "Initial commit - v1.0.0"
git branch -M main
git remote add origin https://github.com/DEIN-USERNAME/Diamond-Digger.git
git push -u origin main
```

### Schritt 2: GitHub Pages aktivieren

Siehe Methode 1, Schritt 4

### Schritt 3: Zukünftige Updates

```bash
# Änderungen machen
git add .
git commit -m "Beschreibung der Änderung"
git push

# GitHub Pages aktualisiert automatisch!
```

---

## 📁 EMPFOHLENE ORDNERSTRUKTUR

Nach dem Upload sollte dein Repository so aussehen:

```
Diamond-Digger/
├── .github/
│   └── workflows/
│       └── pages.yml          # Automatisches Deployment
├── docs/
│   ├── README_GITHUB.md
│   ├── SCHNELLSTART.md
│   └── INSTALLATION.md
├── img/
│   └── Menu.png
├── level/
│   ├── level_01.json
│   ├── level_02.json
│   └── level_03.json
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── index.html                 # WICHTIG: Nicht tunnel_game.html!
├── level_editor.html
├── LICENSE
└── README.md
```

⚠️ **Wichtig:** Die Haupt-Datei muss `index.html` heißen (nicht tunnel_game.html)!

---

## 🔧 KONFIGURATION

### Repository-Einstellungen:

1. **General:**
   - ✅ Public (für GitHub Pages erforderlich)
   - ✅ Issues aktiviert
   - ✅ Discussions optional

2. **Pages:**
   - ✅ Source: Deploy from a branch
   - ✅ Branch: main / (root)

3. **Actions:**
   - ✅ Read and write permissions
   - ✅ Allow GitHub Actions

### Repository-Beschreibung:

```
🎮 Ein Boulder Dash-Klon mit automatischem Level-System
Topics: game, javascript, html5, boulder-dash, puzzle-game
Website: https://ShrekIII.github.io/Diamond-Digger/
```

---

## ✅ CHECKLISTE

Nach dem Setup prüfen:

- [ ] Repository ist öffentlich (Public)
- [ ] Alle Dateien hochgeladen
- [ ] Ordnerstruktur korrekt
- [ ] GitHub Pages aktiviert
- [ ] Warten 2-5 Minuten
- [ ] URL öffnen: `https://DEIN-USERNAME.github.io/Diamond-Digger/`
- [ ] Spiel lädt und funktioniert
- [ ] Level laden erfolgreich
- [ ] Menu.png wird angezeigt
- [ ] Highscore-System funktioniert

---

## 🐛 PROBLEMLÖSUNG

### "404 - Page not found"

**Ursache:** GitHub Pages noch nicht fertig deployed

**Lösung:**
1. Warte weitere 5 Minuten
2. Prüfe Settings → Pages → Status
3. Hard-Reload: Ctrl+Shift+R

### "Repository nicht öffentlich"

**Ursache:** Repository ist privat

**Lösung:**
1. Settings → Danger Zone
2. "Change repository visibility"
3. "Make public"

### "Level nicht gefunden"

**Ursache:** Ordnerstruktur falsch oder Dateien fehlen

**Lösung:**
1. Prüfe dass `/level/` Ordner existiert
2. Prüfe Dateinamen: level_01.json (mit 0!)
3. Öffne Browser-Console (F12) für Details

### "Menu-Bild fehlt"

**Ursache:** img/Menu.png fehlt oder falscher Pfad

**Lösung:**
1. Prüfe dass `/img/Menu.png` existiert
2. Groß-/Kleinschreibung beachten
3. Dateiformat: PNG

---

## 🔄 UPDATES VERÖFFENTLICHEN

### Via Web-Interface:

1. Datei bearbeiten → Klicke auf Stift-Icon
2. Änderungen machen
3. "Commit changes"
4. GitHub Pages aktualisiert automatisch

### Via Git:

```bash
git pull                        # Hole neueste Änderungen
# Dateien bearbeiten
git add .
git commit -m "Update: Beschreibung"
git push
```

### Neue Level hinzufügen:

```bash
# Erstelle Level mit Editor
# Speichere als level_04.json

git add level/level_04.json
git commit -m "Add level 4: [Level-Name]"
git push

# In index.html:
# Ändere: let maxLevel = 3; → let maxLevel = 4;
```

---

## 📊 ANALYTICS (OPTIONAL)

### GitHub Traffic ansehen:

Settings → Insights → Traffic
- Seitenaufrufe
- Unique Visitors
- Verweise

---

## 🎉 FERTIG!

Dein Spiel ist jetzt live!

- **🎮 Spielen:** `https://DEIN-USERNAME.github.io/Diamond-Digger/`
- **📖 README:** Wird automatisch auf GitHub angezeigt
- **🐛 Issues:** Nutzer können Bugs melden
- **⭐ Stars:** Andere können dein Projekt liken

### Nächste Schritte:

1. ⭐ Repository selbst "starren" (für Sichtbarkeit)
2. 🔗 URL teilen mit Freunden
3. 📝 Dokumentation lesen
4. 🎨 Eigene Level erstellen
5. 🤝 Community einladen mitzuwirken

---

## 🆘 HILFE BENÖTIGT?

- 📖 [GitHub Docs](https://docs.github.com/pages)
- 💬 [GitHub Community](https://github.community)
- 🐛 [Issues erstellen](https://github.com/ShrekIII/Diamond-Digger/issues)

**VIEL ERFOLG!** 🚀
