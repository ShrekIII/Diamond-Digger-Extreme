# 🎮 TUNNEL GRABER - GitHub Edition

## 🌐 ONLINE SPIELEN

Das Spiel lädt automatisch Level und Bilder von GitHub!

### Option 1: Direkt im Browser öffnen
1. Download `tunnel_game.html`
2. Doppelklick auf die Datei
3. Spiel lädt automatisch von GitHub
4. **Keine weiteren Dateien nötig!** ✨

### Option 2: GitHub Pages
Wenn das Repository GitHub Pages aktiviert hat:
- Direkt im Browser spielen unter der GitHub Pages URL
- Alles wird automatisch geladen

---

## 📦 WAS DAS SPIEL AUTOMATISCH LÄDT

### Von GitHub (automatisch):
- ✅ **Menu.png** - Menü-Hintergrund
- ✅ **level_01.json** - Level 1
- ✅ **level_02.json** - Level 2  
- ✅ **level_03.json** - Level 3

### URLs:
```
Menü:  https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/refs/heads/main/img/Menu.png
Level: https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/refs/heads/main/level/level_XX.json
```

⚠️ **Wichtig:** 
- GitHub-Ordner heißt `/level/` (singular), nicht `/levels/`
- URLs verwenden `/refs/heads/main/` für den Branch

---

## 🔧 FALLBACK-SYSTEM

Das Spiel versucht automatisch mehrere Quellen:

1. **GitHub Raw** (Hauptquelle)
   - `https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/refs/heads/main/level/level_01.json`
   - `https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/main/level/level_01.json` (Fallback)
   - `https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/refs/heads/main/level_01.json` (Fallback)

2. **Lokale Dateien** (Fallback)
   - `level_01.json` (gleicher Ordner)
   - `level/level_01.json` (Unterordner)

3. **Gecachte Daten** (wenn bereits geladen)

→ **Funktioniert in den meisten Fällen automatisch!**

---

## 🐛 FEHLERBEHEBUNG

### Problem: "Level nicht gefunden"

**Lösung 1: Browser-Konsole prüfen**
1. F12 drücken
2. Tab "Console" öffnen
3. Schau welche URLs fehlschlagen
4. URLs im Browser direkt testen

**Lösung 2: Level lokal ablegen**
1. Erstelle Ordner `level/` neben `tunnel_game.html`
2. Download `level_01.json`, `level_02.json`, `level_03.json` von GitHub
3. In `level/` Ordner legen
4. Spiel neu starten

**Lösung 3: CORS-Problem**
Wenn im Browser "CORS" Fehler erscheinen:
- Verwende einen lokalen Webserver (z.B. Python)
- `python -m http.server 8000`
- Dann öffne: `http://localhost:8000/tunnel_game.html`

### Problem: "Menü-Hintergrund fehlt"

**Lösung 1: GitHub-URL prüfen**
Öffne direkt im Browser:
```
https://raw.githubusercontent.com/ShrekIII/Diamond-Digger/refs/heads/main/img/Menu.png
```
Sollte das Bild zeigen!

**Lösung 2: Lokal ablegen**
1. Download `Menu.png` von GitHub
2. In gleichen Ordner wie `tunnel_game.html`
3. Öffne `tunnel_game.html` im Editor
4. Suche nach `menuScreen.style.backgroundImage`
5. Ändere zu: `'url(Menu.png)'`

---

## 📁 EMPFOHLENE ORDNERSTRUKTUR

### Minimale Version (nur 1 Datei!):
```
📂 Spielordner/
  └── tunnel_game.html          ← Lädt alles von GitHub
```

### Lokale Version:
```
📂 Spielordner/
  ├── tunnel_game.html
  ├── Menu.png                   ← Optional: Lokal
  └── level/                     ← Optional: Lokal (singular!)
      ├── level_01.json
      ├── level_02.json
      └── level_03.json
```

### Vollständige Version:
```
📂 Spielordner/
  ├── tunnel_game.html
  ├── level_editor.html
  ├── Menu.png
  └── level/                     ← Wichtig: singular!
      ├── level_01.json
      ├── level_02.json
      ├── level_03.json
      ├── level_04.json          ← Eigene Level
      └── level_05.json
```

---

## 🎨 EIGENE LEVEL ERSTELLEN

1. Öffne `level_editor.html` im Browser
2. Gestalte dein Level
3. Klicke "Level speichern"
4. Speichere als `level_04.json` (oder höher)
5. Lege in `level/` Ordner (nicht `levels/`!)
6. Ändere in `tunnel_game.html` die Zeile:
   ```javascript
   let maxLevel = 3;  // → Ändere auf 4 (oder mehr)
   ```

---

## 🌐 GITHUB PAGES SETUP

### Für Repository-Besitzer:

1. **Repository Settings** → **Pages**
2. Source: `main` branch
3. Folder: `/ (root)` oder `/docs`
4. Save

Das Spiel ist dann verfügbar unter:
```
https://ShrekIII.github.io/Diamond-Digger/tunnel_game.html
```

### Ordnerstruktur für GitHub Pages:
```
Repository/
├── tunnel_game.html          (Hauptspiel)
├── level_editor.html         (Editor)
├── img/
│   └── Menu.png              (Menü-Bild)
├── level/                    ⚠️ Singular!
│   ├── level_01.json
│   ├── level_02.json
│   └── level_03.json
└── README.md
```

---

## 🔒 SICHERHEIT & DATENSCHUTZ

### Was wird geladen?
- Nur Bilder und JSON-Dateien von GitHub
- Keine externe Analytics
- Keine Cookies (außer LocalStorage für Highscores)
- Keine Tracking-Scripts

### LocalStorage:
- Speichert nur Highscores lokal im Browser
- Key: `tunnel_game_highscores`
- Kann jederzeit gelöscht werden (F12 → Console):
  ```javascript
  localStorage.removeItem('tunnel_game_highscores')
  ```

---

## 📊 STATISTIKEN

### Aktuelles Spiel:
- **3 Level** verfügbar
- **Level-Dateien** auf GitHub gehostet
- **Automatisches Laden** von Level
- **Offline-Fähig** wenn Dateien gecacht

---

## 💡 TIPPS & TRICKS

### Performance:
- Level werden nach dem ersten Laden gecacht
- Browser cached automatisch GitHub-Dateien
- Bei langsamer Verbindung: Level lokal ablegen

### Entwicklung:
- Browser-Konsole (F12) zeigt welche URLs geladen werden
- Bei Änderungen: Hard-Reload (Ctrl+Shift+R)
- Test verschiedener URLs in Console

### Debugging:
```javascript
// In Browser-Console:
console.log(customLevels);        // Zeigt geladene Level
console.log(usingCustomLevels);   // Sollte true sein
console.log(maxLevel);            // Sollte 3 sein
```

---

## ✅ CHECKLISTE

Vor dem Spielen:
- [ ] GitHub-Repository ist public
- [ ] Level-Dateien sind im `/level/` Ordner (singular!)
- [ ] Menu.png ist im `/img/` Ordner
- [ ] Browser erlaubt CORS (oder nutze Webserver)
- [ ] Internet-Verbindung vorhanden (für ersten Load)

---

## 🎯 NÄCHSTE SCHRITTE

1. **Testen:** Öffne `tunnel_game.html` direkt
2. **Prüfen:** Schau Browser-Console für Fehler
3. **Anpassen:** Ändere GitHub-URLs falls nötig
4. **Spielen:** Viel Spaß! 🎮

---

## 📞 SUPPORT

Bei Problemen:
1. Browser-Console (F12) prüfen
2. GitHub-URLs direkt im Browser testen
3. CORS-Fehler? → Lokalen Webserver nutzen
4. Immer noch Probleme? → Issue auf GitHub erstellen

**VIEL SPAẞ!** ⛏️💎
