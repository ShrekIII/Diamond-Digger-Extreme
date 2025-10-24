# ⛏️ TUNNEL GRABER - Diamond Digger Game

Ein Boulder Dash-inspiriertes Puzzle-Spiel mit automatischem Level-System und Highscore-Liste.

[![Spielen](https://img.shields.io/badge/🎮_Jetzt_Spielen-GitHub_Pages-success?style=for-the-badge)](https://ShrekIII.github.io/Diamond-Digger/)
[![Level Editor](https://img.shields.io/badge/🎨_Level_Editor-Öffnen-blue?style=for-the-badge)](https://ShrekIII.github.io/Diamond-Digger/level_editor.html)

---

## 🎮 ONLINE SPIELEN

**Direkt im Browser spielen:**
👉 [https://ShrekIII.github.io/Diamond-Digger/](https://ShrekIII.github.io/Diamond-Digger/)

Keine Installation nötig! Funktioniert in jedem modernen Browser.

---

## ✨ FEATURES

### 🎯 Spielmechanik
- **Boulder Dash-Gameplay** - Grabe Tunnel, sammle Diamanten
- **3 Level** - Automatisches Level-System
- **Fallende Objekte** - Steine und Diamanten fallen realistisch
- **Monster** - Zwei Typen: Diamant-Monster und TNT-Monster
- **Timer-System** - 60s Basis + 10s pro Level
- **Abbaubare Mauern** - Mit Schaufel (3 Treffer)

### 🏆 Highscore-System
- **Top 10 Bestenliste** - Bleibt gespeichert
- **Name-Eingabe** - Bei neuem Highscore
- **Sortierung** - Nach Diamanten → Level → Zeit → Distanz
- **LocalStorage** - Persistente Speicherung

### 🎨 Level-Editor
- **Visueller Editor** - Erstelle eigene Level
- **Export/Import** - JSON-Format
- **Alle Elemente** - Wände, Erde, Diamanten, Steine, Monster

---

## 📦 INSTALLATION (LOKAL)

### Schnell-Download:
```bash
git clone https://github.com/ShrekIII/Diamond-Digger.git
cd Diamond-Digger
```

Dann öffne `index.html` im Browser!

### Oder einzelne Datei:
Lade nur `index.html` herunter - Level laden automatisch von GitHub!

---

## 🎯 STEUERUNG

| Taste | Aktion |
|-------|--------|
| **↑ ↓ ← →** | Bewegung |
| **ESC** | Pause (geplant) |

### Spielziel pro Level:
1. ✅ Sammle genug Diamanten 💎
2. ✅ Ausgang öffnet sich 🚪
3. ✅ Erreiche den Ausgang
4. ✅ Nächstes Level lädt automatisch!

---

## 📁 REPOSITORY-STRUKTUR

```
Diamond-Digger/
├── index.html              # Hauptspiel (direkt spielbar)
├── level_editor.html       # Level-Editor
├── level/                  # Level-Dateien
│   ├── level_01.json      # Level 1 - Tutorial
│   ├── level_02.json      # Level 2 - Steine
│   └── level_03.json      # Level 3 - Monster
├── img/                    # Bilder
│   └── Menu.png           # Menü-Hintergrund
└── docs/                   # Dokumentation
    ├── README_GITHUB.md   # GitHub-Anleitung
    ├── SCHNELLSTART.md    # Schnellstart-Guide
    └── INSTALLATION.md    # Installations-Anleitung
```

---

## 🎨 EIGENE LEVEL ERSTELLEN

### 1. Level-Editor öffnen:
👉 [Level-Editor starten](https://ShrekIII.github.io/Diamond-Digger/level_editor.html)

### 2. Level gestalten:
- Platziere Wände, Erde, Diamanten, Steine
- Setze Spieler-Start und Ausgang
- Füge Monster hinzu (optional)

### 3. Level speichern:
- Klicke "Level speichern"
- Speichere als `level_04.json`

### 4. Ins Repository hochladen:
```bash
# Fork das Repository
# Füge dein Level in /level/ hinzu
# Erstelle Pull Request
```

### 5. maxLevel erhöhen:
In `index.html` Zeile ~519:
```javascript
let maxLevel = 3;  // → Ändere auf 4
```

---

## 🌐 GITHUB PAGES SETUP

### Für Mitwirkende:

1. **Fork** dieses Repository
2. **Settings** → **Pages**
3. Source: `main` branch → **Save**
4. Spiel verfügbar unter:
   ```
   https://DEIN-USERNAME.github.io/Diamond-Digger/
   ```

---

## 🛠️ ENTWICKLUNG

### Lokaler Webserver (empfohlen):
```bash
# Python 3
python -m http.server 8000

# Node.js
npx serve

# PHP
php -S localhost:8000
```

Dann öffne: `http://localhost:8000`

### Direkt im Browser (file://):
Funktioniert auch! Level laden von GitHub oder lokal.

---

## 🐛 BEKANNTE PROBLEME & LÖSUNGEN

### Level laden nicht automatisch
**Problem:** Repository ist privat  
**Lösung:** Repository auf "Public" setzen oder Level manuell hochladen

### CORS-Fehler
**Problem:** Browser blockiert GitHub-Requests  
**Lösung:** Lokalen Webserver verwenden (siehe oben)

### Highscores verschwinden
**Problem:** Browser-Cache gelöscht  
**Lösung:** Normal - LocalStorage wurde geleert

### Namen fehlen in Bestenliste
**Problem:** Alte Daten im LocalStorage  
**Lösung:** 
```javascript
// In Browser-Console (F12):
localStorage.removeItem('tunnel_game_highscores')
// Dann Seite neu laden
```

---

## 📊 LEVEL-FORMAT (JSON)

```json
{
  "name": "Level Name",
  "width": 20,
  "height": 20,
  "playerStart": {"x": 2, "y": 2},
  "exit": {"x": 17, "y": 16},
  "tiles": [
    ["wall", "earth", "empty", ...],
    ...
  ],
  "objects": {
    "stones": [{"x": 10, "y": 10}],
    "diamonds": [{"x": 12, "y": 13}],
    "monsters": [
      {"type": "diamond", "x": 5, "y": 5},
      {"type": "tnt", "x": 15, "y": 15}
    ]
  },
  "requiredDiamonds": 15
}
```

### Tile-Typen:
- `"wall"` - Unzerstörbare Mauer (abbaubar mit 3 Treffern)
- `"earth"` - Normale Erde (ausgrabbar)
- `"empty"` - Leeres Feld / Tunnel

### Monster-Typen:
- `"diamond"` - Erzeugt Diamant bei Tod
- `"tnt"` - Explodiert bei Tod

---

## 🤝 MITWIRKEN

Wir freuen uns über Beiträge!

### Pull Requests für:
- 🆕 Neue Level
- 🐛 Bugfixes
- ✨ Neue Features
- 📝 Dokumentation
- 🎨 Grafik-Verbesserungen

### Level einreichen:
1. Erstelle Level mit dem Editor
2. Fork dieses Repository
3. Füge Level in `/level/` hinzu
4. Erstelle Pull Request mit:
   - Level-Name
   - Schwierigkeitsgrad
   - Screenshot (optional)

---

## 📜 LIZENZ

MIT License - Siehe [LICENSE](LICENSE) Datei

---

## 👥 CREDITS

### Entwicklung:
- **ShrekIII** - Original-Konzept und Entwicklung
- **Claude (Anthropic)** - Code-Optimierung und Features

### Inspiration:
- **Boulder Dash** (1984) - Das Original-Spiel von Peter Liepa

---

## 🔗 LINKS

- **🎮 Spiel:** [https://ShrekIII.github.io/Diamond-Digger/](https://ShrekIII.github.io/Diamond-Digger/)
- **🎨 Level-Editor:** [https://ShrekIII.github.io/Diamond-Digger/level_editor.html](https://ShrekIII.github.io/Diamond-Digger/level_editor.html)
- **📖 Dokumentation:** [/docs/README_GITHUB.md](/docs/README_GITHUB.md)
- **🐛 Issues:** [GitHub Issues](https://github.com/ShrekIII/Diamond-Digger/issues)

---

## 📈 VERSIONEN

### v1.0.0 (Aktuell)
- ✅ Vollständiges Menü-System
- ✅ Highscore mit Namen
- ✅ Automatisches Level-Laden
- ✅ Level-Editor Integration
- ✅ 3 spielbare Level
- ✅ GitHub Pages Support

### Geplant (v1.1.0):
- ⏸️ Pause-Menü (ESC-Taste)
- 🔊 Sound-Effekte
- ✨ Partikel-Effekte
- 🎮 Gamepad-Support
- 🌍 Mehrsprachigkeit

---

## 💬 SUPPORT

Bei Fragen oder Problemen:
1. 📖 Lies die [Dokumentation](/docs/)
2. 🔍 Durchsuche [Issues](https://github.com/ShrekIII/Diamond-Digger/issues)
3. 🆕 Erstelle ein neues Issue

---

## ⭐ GEFÄLLT DIR DAS SPIEL?

- ⭐ **Star** dieses Repository
- 🔀 **Fork** und erstelle eigene Level
- 🐦 **Teile** mit Freunden
- 💬 **Feedback** via Issues

---

<div align="center">

**VIEL SPAẞ BEIM GRABEN!** ⛏️💎

Made with ❤️ by ShrekIII

[▶️ Jetzt Spielen](https://ShrekIII.github.io/Diamond-Digger/) | [🎨 Level Editor](https://ShrekIII.github.io/Diamond-Digger/level_editor.html) | [📖 Docs](docs/)

</div>
