# 🚀 GitHub Repository Setup Guide

Diese Anleitung erklärt, wie du das Diamond Digger Repository auf GitHub veröffentlichst.

---

## 📋 Voraussetzungen

- ✅ GitHub Account
- ✅ Git installiert
- ✅ Repository lokal vorhanden

---

## 🔧 Schritt-für-Schritt Anleitung

### 1️⃣ Neues GitHub Repository erstellen

1. Gehe zu https://github.com/new
2. **Repository Name:** `Diamond-Digger` (oder ein anderer Name)
3. **Beschreibung:** `Boulder Dash-inspired puzzle game with level editor and highscores`
4. **Visibility:** Public ✅
5. **Initialize:** NICHTS auswählen (kein README, .gitignore, License)
   - ❗ Wichtig: Wir haben bereits alle Dateien lokal!
6. Klicke auf **"Create repository"**

### 2️⃣ Lokales Repository mit GitHub verbinden

```bash
# Navigiere zum Projekt-Verzeichnis
cd /pfad/zum/diamond-digger-fixed

# Füge Remote-Repository hinzu (ersetze USERNAME mit deinem GitHub-Benutzernamen)
git remote add origin https://github.com/USERNAME/Diamond-Digger.git

# Überprüfe Remote
git remote -v
```

### 3️⃣ Code zu GitHub pushen

```bash
# Push main branch
git push -u origin main

# Push Tag
git push origin v1.14.1
```

### 4️⃣ GitHub Pages aktivieren

1. Gehe zu Repository Settings
2. Scrolle zu **"Pages"**
3. **Source:** 
   - Branch: `main`
   - Folder: `/ (root)`
4. Klicke **"Save"**
5. Warte 1-2 Minuten
6. Deine Website ist live unter: `https://USERNAME.github.io/Diamond-Digger/`

---

## 🎯 Alternative: GitHub Actions verwenden

Das Repository enthält bereits eine GitHub Actions Workflow-Datei (`.github/workflows/deploy.yml`).

### Workflow aktivieren:

1. Gehe zu Repository → **Actions**
2. Aktiviere Workflows (falls deaktiviert)
3. Der Workflow läuft automatisch bei jedem Push auf `main`

### Workflow-Features:
- ✅ Automatisches Deployment bei jedem Commit
- ✅ Build und Deployment über GitHub Actions
- ✅ Keine manuelle Konfiguration nötig

---

## 📦 Release erstellen (Optional)

### Über GitHub Web Interface:

1. Gehe zu **"Releases"** → **"Create a new release"**
2. **Tag:** `v1.14.1` (wähle existierenden Tag)
3. **Release title:** `v1.14.1 - Critical Collision Bugfix`
4. **Description:** Kopiere aus `RELEASE_NOTES.md`
5. **Assets:** Lade `index.html` hoch (optional)
6. Klicke **"Publish release"**

### Über Git CLI:

```bash
# Tag wurde bereits erstellt
git tag -l

# Push alle Tags
git push origin --tags
```

---

## 🔐 SSH statt HTTPS (Empfohlen)

Für häufiges Pushen ohne Passwort-Eingabe:

### 1. SSH-Key erstellen (falls nicht vorhanden):
```bash
ssh-keygen -t ed25519 -C "deine-email@example.com"
```

### 2. SSH-Key zu GitHub hinzufügen:
```bash
# Public Key anzeigen
cat ~/.ssh/id_ed25519.pub

# Kopiere den Output und füge ihn hinzu unter:
# GitHub → Settings → SSH and GPG keys → New SSH key
```

### 3. Remote URL ändern:
```bash
git remote set-url origin git@github.com:USERNAME/Diamond-Digger.git
```

---

## 🎨 Repository verschönern

### Badges hinzufügen (README.md)

Die README.md enthält bereits Badges:
```markdown
[![Version](https://img.shields.io/badge/Version-1.14.1-blue?style=for-the-badge)](https://github.com/USERNAME/Diamond-Digger/releases)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
```

### About-Section konfigurieren:

1. Gehe zu Repository → ⚙️ (oben rechts)
2. **Description:** Boulder Dash-inspired puzzle game
3. **Website:** https://USERNAME.github.io/Diamond-Digger/
4. **Topics:** `game` `javascript` `html5-canvas` `puzzle-game` `boulder-dash` `level-editor`
5. Speichern

### Social Preview Image:

1. Settings → General → Social preview
2. Lade ein Screenshot des Spiels hoch (1280x640px empfohlen)

---

## 📝 Wichtige Dateien im Repository

| Datei | Zweck |
|-------|-------|
| `README.md` | Projekt-Übersicht und Dokumentation |
| `CHANGELOG.md` | Versionshistorie |
| `CONTRIBUTING.md` | Anleitung für Contributors |
| `LICENSE` | MIT License |
| `CODE_OF_CONDUCT.md` | Community-Richtlinien |
| `SECURITY.md` | Sicherheitsrichtlinien |
| `.github/workflows/deploy.yml` | Auto-Deployment |
| `.github/ISSUE_TEMPLATE/` | Issue-Vorlagen |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR-Vorlage |

---

## 🔧 Weitere Konfigurationen

### Branch Protection Rules:

1. Settings → Branches → Add rule
2. **Branch name pattern:** `main`
3. Aktiviere:
   - ✅ Require pull request reviews before merging
   - ✅ Require status checks to pass
   - ✅ Require branches to be up to date
   - ✅ Include administrators

### Discussions aktivieren:

1. Settings → General
2. Features → ✅ Discussions
3. Ermöglicht Community-Diskussionen

### Projects erstellen (optional):

1. Projects → New project
2. Board-Typ wählen
3. Tasks und Roadmap verwalten

---

## 📊 Repository Statistics

Nach dem Push siehst du:
- 📁 **34 Files**
- 📝 **~13,000 Lines of Code**
- 🏷️ **1 Release** (v1.14.1)
- 🎮 **Game**, **Level Editor**, **Tutorials**

---

## 🚀 Nach dem Deployment

### Überprüfen:

1. **GitHub Pages:** https://USERNAME.github.io/Diamond-Digger/
2. **Spiel testen:** Alle Level durchspielen
3. **Level Editor:** Funktionalität prüfen
4. **Browser-Console:** Auf Fehler prüfen

### Teilen:

```markdown
🎮 [Spiel auf GitHub Pages](https://USERNAME.github.io/Diamond-Digger/)
📂 [Source Code](https://github.com/USERNAME/Diamond-Digger)
🎨 [Level Editor](https://USERNAME.github.io/Diamond-Digger/level_editor.html)
```

---

## 🆘 Troubleshooting

### Problem: "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/USERNAME/Diamond-Digger.git
```

### Problem: GitHub Pages zeigt 404
- Warte 2-5 Minuten nach Aktivierung
- Prüfe ob Branch `main` und Ordner `/` gewählt ist
- Hard-Refresh im Browser (Ctrl + Shift + R)

### Problem: Push wird rejected
```bash
git pull origin main --rebase
git push origin main
```

### Problem: Große Dateien (music/)
Falls Git die MP3-Dateien ablehnt:
```bash
# Git LFS installieren
git lfs install

# Große Dateien tracken
git lfs track "*.mp3"

# .gitattributes committen
git add .gitattributes
git commit -m "Add Git LFS for audio files"
git push
```

---

## 📞 Support

Bei Problemen:
- 📖 [GitHub Docs](https://docs.github.com)
- 💬 [GitHub Community](https://github.community)
- 🐛 Issue erstellen im Repository

---

## ✅ Checkliste

- [ ] GitHub Repository erstellt
- [ ] Remote hinzugefügt
- [ ] Code gepusht
- [ ] Tags gepusht
- [ ] GitHub Pages aktiviert
- [ ] Release erstellt
- [ ] About-Section konfiguriert
- [ ] Topics hinzugefügt
- [ ] Social Preview Image hochgeladen
- [ ] Branch Protection aktiviert (optional)
- [ ] Discussions aktiviert (optional)
- [ ] Spiel auf GitHub Pages getestet
- [ ] README Links aktualisiert (USERNAME ersetzen)

---

**Viel Erfolg mit deinem Repository!** 🚀

*Letzte Aktualisierung: 26. Oktober 2025*
