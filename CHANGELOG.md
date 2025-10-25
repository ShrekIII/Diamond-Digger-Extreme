# 📋 CHANGELOG - DIAMOND DIGGER EXTREME

## Versionshistorie

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

## 🔄 NÄCHSTE VERSION: v1.6.3

### Geplant:
- Diamond Monster Bewegungslogik testen
- Weitere Optimierungen

---

## 📥 AKTUELLE VERSION

**Stabil:** v1.6.2
**Debug:** v1.6.2-debug

**Download:**
- [tunnel_game.html](computer:///mnt/user-data/outputs/tunnel_game.html) - v1.6.2
- [tunnel_game_debug.html](computer:///mnt/user-data/outputs/tunnel_game_debug.html) - v1.6.2-debug
- [github-release.zip](computer:///mnt/user-data/outputs/github-release.zip) - v1.6.2

---

**Letzte Aktualisierung:** 25.10.2025
