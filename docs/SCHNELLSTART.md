# 🚀 SCHNELLSTART - GitHub Edition

## ⚡ 3 WEGE ZUM SPIELEN

### Option 1: Mit GitHub (öffentliches Repository)
1. Repository ist öffentlich (public)
2. `tunnel_game.html` herunterladen
3. Datei im Browser öffnen
4. **Fertig!** Level laden automatisch von GitHub ✨

### Option 2: Manueller Upload
1. `tunnel_game.html` herunterladen
2. Datei im Browser öffnen
3. "▶ Spiel Starten" klicken
4. Falls Level nicht laden → Dialog erscheint
5. Alle 3 Level-Dateien auswählen (level_01.json bis level_03.json)
6. **Fertig!** Spiel startet automatisch 🎮

### Option 3: Lokale Installation
1. Alle Dateien herunterladen:
   ```
   📂 Ordner/
     ├── tunnel_game.html
     ├── level_01.json
     ├── level_02.json
     └── level_03.json
   ```
2. `tunnel_game.html` öffnen
3. **Fertig!** Level laden lokal ⚡

---

## 🎯 WAS PASSIERT BEIM START?

```
1. Klick auf "▶ Spiel Starten"
   ↓
2. Spiel versucht Level zu laden:
   ✓ GitHub (https://raw.githubusercontent.com/.../level/level_01.json)
   ✓ Lokal (level_01.json)
   ✓ Unterordner (level/level_01.json)
   ↓
3a. Erfolgreich → Spiel startet! 🎉
3b. Fehlgeschlagen → Upload-Dialog erscheint
   ↓
4. Wähle alle 3 Level-Dateien aus
   ↓
5. Spiel startet! 🎮
```

---

## 📁 LEVEL-DATEIEN HERUNTERLADEN

### Von GitHub:
1. Gehe zu: https://github.com/ShrekIII/Diamond-Digger
2. Klicke auf Ordner `level/`
3. Für jedes Level:
   - Klicke auf `level_01.json`
   - Klicke auf "Raw" Button
   - Rechtsklick → "Speichern unter..."
   - Speichere als `level_01.json`
4. Wiederhole für level_02.json und level_03.json

### Schnell-Download (falls Repository öffentlich):
```bash
# Mit wget:
wget https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/refs/heads/main/level/level_01.json
wget https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/refs/heads/main/level/level_02.json
wget https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/refs/heads/main/level/level_03.json

# Mit curl:
curl -O https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/refs/heads/main/level/level_01.json
curl -O https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/refs/heads/main/level/level_02.json
curl -O https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/refs/heads/main/level/level_03.json
```

---

## 🔧 PROBLEMLÖSUNG

### ❌ "Level konnte nicht geladen werden"

**Ursache:** GitHub-Repository ist privat oder Dateien fehlen

**Lösung:**
1. Dialog erscheint: "Möchtest du die Level-Dateien manuell hochladen?"
2. Klicke "OK"
3. Wähle alle 3 Level-Dateien aus (Mehrfachauswahl mit Strg/Cmd)
4. Spiel startet automatisch!

**Alternative:**
- Lade Level-Dateien herunter
- Lege sie neben tunnel_game.html
- Spiel neu starten

### ⚠️ Repository ist privat

**Problem:** GitHub-Raw-URLs geben 403 Forbidden

**Lösung 1:** Repository öffentlich machen
- GitHub → Settings → Danger Zone → Change visibility → Public

**Lösung 2:** Level lokal bereitstellen
- Dateien in gleichen Ordner wie tunnel_game.html
- Spiel lädt dann lokal

**Lösung 3:** Manueller Upload
- Siehe Option 2 oben

---

## 💡 TIPPS

### Für beste Erfahrung:
✅ Repository öffentlich machen → Level laden automatisch  
✅ GitHub Pages aktivieren → Spiel direkt im Browser  
✅ Alle Dateien lokal → Funktioniert offline  

### Cache-Vorteil:
Nach dem ersten Laden werden Level gecached!
- Beim nächsten Mal: Sofortiger Start
- Auch ohne Internet (nach erstem Laden)

### Debugging:
Öffne Browser-Konsole (F12) um zu sehen:
- Welche URLs probiert werden
- Welche URL erfolgreich war
- Warum etwas fehlgeschlagen ist

**Beispiel Console-Output:**
```
Versuche Level 1 zu laden von: https://raw.githubusercontent.com/.../level/level_01.json
❌ Fehlgeschlagen (...): HTTP 403
Versuche Level 1 zu laden von: level_01.json
✅ Level 1 erfolgreich geladen von: level_01.json
```

---

## 📊 SYSTEM-STATUS PRÜFEN

Öffne Browser-Konsole (F12) und gib ein:

```javascript
// Zeige geladene Level
console.log('Geladene Level:', customLevels);

// Zeige maxLevel
console.log('Max Level:', maxLevel);

// Teste GitHub-URL
fetch('https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/refs/heads/main/level/level_01.json')
  .then(r => console.log('GitHub Status:', r.status))
  .catch(e => console.log('GitHub Fehler:', e));
```

---

## ✅ CHECKLISTE

Vor dem Spielen:
- [ ] tunnel_game.html heruntergeladen
- [ ] Browser ist modern (Chrome, Firefox, Edge)
- [ ] JavaScript ist aktiviert
- [ ] **ENTWEDER:**
  - [ ] Repository ist öffentlich (automatic loading)
  - [ ] Level-Dateien heruntergeladen (manual loading)
  - [ ] Level-Dateien liegen lokal (offline mode)

---

## 🎮 JETZT SPIELEN!

1. **Öffne** `tunnel_game.html`
2. **Klicke** "▶ Spiel Starten"
3. **Warte** auf automatisches Laden ODER wähle Level manuell
4. **Spiele!** ⛏️💎

**VIEL SPAẞ!** 🎉
