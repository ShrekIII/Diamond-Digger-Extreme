# 📋 CHANGELOG - DIAMOND DIGGER EXTREME

## Versionshistorie

---

## v1.6.6 (25.10.2025) - Level-Editor Spieler-Rendering Fix

### 🐛 Bug Fix:
- **Spieler-Icon wird nur noch gezeichnet wenn Tile 'empty' ist**
- Wenn Erde über Spieler-Position gemalt wird, verschwindet Spieler-Icon
- "Alles löschen" übermalt jetzt korrekt die Spieler-Position mit Erde

### 📝 Änderungen:
- `drawLevel()`: Prüft Tile an Spieler-Position vor dem Zeichnen
- Spieler nur sichtbar wenn `tiles[playerY][playerX] === 'empty'`

### 🎯 Verhalten:
- Spieler-Tool setzt Tile auf 'empty' und Position
- Erde-Tool übermalt Spieler-Position → Icon verschwindet
- "Alles löschen" füllt mit Erde → Spieler nicht mehr sichtbar

---

## v1.6.5 (25.10.2025) - Border-Mauern & Level-Editor Fix

### ✨ Neue Features:
- **Zwei Mauer-Typen:** `wall` (zerstörbar) und `border` (unzerstörbar)
- **Level-Editor:** Neues "Rand" Tool (🟥) für unzerstörbare Mauern
- **Visuelle Unterscheidung:** Border-Mauern sind rot, normale Mauern grau

### 🐛 Bug Fixes:
- **Level-Editor:** Unterer Rand jetzt 2 statt 3 Zeilen (Zeile 425: `levelHeight - 3` → `- 2`)
- **Level-Editor:** Verwendet `border` statt `wall` für Rand-Generierung

### 📝 Änderungen:
- **Level-Editor:** `initLevel()` erstellt `border` für Rand
- **Hauptspiel:** `levelTiles` Variable für border-Tracking
- **Hauptspiel:** `isInWall()` erkennt border-Tiles
- **Hauptspiel:** `drawWalls()` rendert border-Tiles (rot)
- **Hauptspiel:** Border-Tiles sind unzerstörbar (keine health)

### 🎯 Verhalten:
- Border (🟥): Unzerstörbar, stoppt alles
- Wall (🧱): Zerstörbar (3 Health), kann durch Explosion zerstört werden

---

## v1.6.4 (25.10.2025) - Level-Dateien Fix

### 🐛 Kritischer Bug Fix:
- **Alle Level-Dateien korrigiert** (untere Wand-Grenze)
- level_01.json, level_02.json, level_03.json: 3→2 Wand-Zeilen
- level_00.json: War bereits korrekt (2 Zeilen)

### 📝 Änderungen:
- Level 1: Height 20→19, untere Wand-Zeilen 3→2
- Level 2: Height 20→19, untere Wand-Zeilen 3→2
- Level 3: Height 20→19, untere Wand-Zeilen 3→2
- Level 0: Bereits korrekt (Height 11, 2 Wand-Zeilen)

### 🎯 Resultat:
- ✅ Alle Level haben jetzt 2 Wand-Zeilen unten
- ✅ Konsistent mit v1.6.2 Code-Fix
- ✅ 1 zusätzliche Zeile spielbare Fläche pro Level!

### ⚠️ Wichtig:
- v1.6.2 fixte nur CODE (prozedurale Generierung)
- v1.6.4 fixt LEVEL-DATEIEN (JSON)
- **Beide Fixes sind notwendig!**

---

## v1.6.3 (25.10.2025) - Level Editor Version Badge

### ✨ Neue Features:
- **Version Badge im Level Editor** hinzugefügt
- Zeigt aktuelle Version unten rechts an
- Konsistentes Design mit Hauptspiel

### 📝 Änderungen:
- Level Editor: Version Badge CSS hinzugefügt
- Level Editor: Badge-Element eingefügt (unten rechts)
- Version Badge zeigt "v1.6.3"

### 📁 Dateien:
- `level_editor.html` - Version Badge hinzugefügt
- `index.html` - Version zu v1.6.3 aktualisiert

---

## v1.6.2 (25.10.2025) - Wand-Grenze Fix

### 🐛 Bug Fix:
- **Untere Wand-Grenze von 3 auf 2 Felder reduziert**
- Konsistenz mit anderen Rändern (alle jetzt 2 Felder breit/hoch)
- Betrifft: prozedurale Level-Generierung

### 📝 Änderungen:
- `WORLD_HEIGHT - 3` → `WORLD_HEIGHT - 2` (6 Stellen)
- isInWall(): Untere Grenze korrigiert
- Fallende Steine: Boundary-Check korrigiert
- Fallende Diamanten: Boundary-Check korrigiert
- Spieler-Bewegung: Grenze korrigiert

### 🎯 Betroffene Bereiche:
- Level-Generierung (mehr spielbare Fläche)
- Stein-Physik (korrekter Boundary-Check)
- Diamant-Physik (korrekter Boundary-Check)
- Spieler-Bewegung (kann bis 2 Felder vom Rand)

---

## v1.6.1 (25.10.2025) - isObject Fix

### 🐛 Kritischer Bug Fix:
- **Diamond Monster Bewegung repariert**
- `isWallOrEarth()` → `isObject()` (prüft ALLE Objekte)
- `hasWallNeighbor()` → `hasObjectNeighbor()`
- Monster bewegen sich jetzt entlang Wänden, Erde, Steinen, Diamanten, etc.

### 📝 Änderungen:
- Funktion `isObject()` implementiert (prüft 7 Objekttypen)
- Funktion `hasObjectNeighbor()` verwendet `isObject()`
- Version Badge hinzugefügt (unten rechts im Menu)

### 📁 Dateien:
- `index.html` - Hauptspiel v1.6.1
- `tunnel_game_debug.html` - Debug-Version v1.6.1-debug

---

## v1.6.0.2 (24.10.2025) - Position Fix

### 🐛 Bug Fix:
- Diamond Monster Position wird jetzt korrekt gesetzt
- `monster.gridX/Y` wird direkt nach `moveAlongWall()` aktualisiert
- `return` nach Bewegung verhindert weitere Prüfungen

### 📝 Änderungen:
- Diamond Monster Logik überarbeitet
- Position-Update direkt in updateMonsters()
- Spieler-Kollision geprüft

---

## v1.6.0.1 (24.10.2025) - Debug Version

### 🔍 Debug:
- Ausführliche Console-Logs hinzugefügt
- Monster-Bewegung debugging
- moveAlongWall() Logs

### 📝 Änderungen:
- Logs in updateMonsters()
- Logs in moveAlongWall()
- hasWallNeighbor und isEmpty Logs

---

## v1.6.0 (24.10.2025) - Diamond Monster

### ✨ Neue Features:
- **Diamond Monster Bewegungslogik** (moveAlongWall)
- 3 Regeln implementiert:
  1. Vermeide vorheriges Feld
  2. Bewegung im Uhrzeigersinn
  3. Entlang Wänden/Erde (später korrigiert zu "alle Objekte")

### 📝 Änderungen:
- Level_00 mit 5 Steinen
- Game Loop Timing korrigiert
- Dynamisches Level-Laden von GitHub
- 0-basierte Level-Nummerierung

### 🎨 UI:
- Version Badge im Menu (unten rechts)

---

## v1.5.3 (23.10.2025) - Array Fix

### 🐛 Bug Fix:
- 0-basierte Level-Nummerierung
- Array-Index Fehler behoben

---

## v1.5.2 (23.10.2025) - Game Loop

### 🐛 Bug Fix:
- Game Loop Timing korrigiert
- requestAnimationFrame optimiert

---

## v1.5.1 (22.10.2025) - Dateinamen

### 📝 Änderungen:
- Konsistente Dateinamen (level_00.json)
- Kleinschreibung für alle Level-Dateien

---

## v1.5.0 (22.10.2025) - Dynamic Loading

### ✨ Neue Features:
- **Dynamisches Level-Laden von GitHub**
- Level-Cache System
- Fehlerbehandlung für fehlende Level

### 📝 Änderungen:
- loadLevelFromGitHub() Funktion
- LEVELS_URL Konstante
- Level-Caching in customLevels Object

---

## v1.4.x - Frühere Versionen

### Features:
- Grundlegendes Gameplay
- Steine, Diamanten, Monster
- Highscore-System
- Level-Editor
- Menu-System

---

## 📋 VERSIONS-SCHEMA

**Format:** `MAJOR.MINOR.PATCH[-suffix]`

- **MAJOR:** Große Änderungen, Breaking Changes
- **MINOR:** Neue Features, Verbesserungen
- **PATCH:** Bug Fixes, kleine Änderungen
- **Suffix:** `-debug` für Debug-Versionen

**Beispiele:**
- `v1.6.1` - Release-Version
- `v1.6.1-debug` - Debug-Version
- `v2.0.0` - Major Update

---

## 🔄 NÄCHSTE VERSION: v1.6.5

### Geplant:
- Diamond Monster Bewegungslogik finalisieren
- Weitere Optimierungen

---

## 📥 AKTUELLE VERSION

**Stabil:** v1.6.6
**Debug:** v1.6.6-debug

**Download:**
- [tunnel_game.html](computer:///mnt/user-data/outputs/tunnel_game.html) - v1.6.6
- [tunnel_game_debug.html](computer:///mnt/user-data/outputs/tunnel_game_debug.html) - v1.6.6-debug
- [level_editor.html](computer:///mnt/user-data/outputs/level_editor.html) - v1.6.6
- [github-release.zip](computer:///mnt/user-data/outputs/github-release.zip) - v1.6.6

---

**Letzte Aktualisierung:** 25.10.2025
