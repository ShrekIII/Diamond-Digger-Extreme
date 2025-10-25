# 📋 CHANGELOG - DIAMOND DIGGER EXTREME

## Versionshistorie

---

## v1.14.0 (25.10.2025) - Bugfixes & Visual Feedback

### 🐛 Bugfixes:

**1. Menü-Musik Autoplay verbessert:**
- Aggressiverer Ansatz: `play()` + `unmute`
- Promise-basierte Fehlerbehandlung
- Fallback bei Autoplay-Blockierung
- `{ once: true }` für Event-Listener (verhindert Mehrfach-Start)

**2. "Wiederholen" Button Fix:**
- **Problem**: Lud falsches Level beim Wiederholen
- **Tutorial**: Verwendet jetzt `loadLevel(currentLevel - 1)` (0-basiert)
- **Normal**: Verwendet `loadLevelByNumber(currentLevel)` (1-basiert)
- Console-Log: Zeigt Level-Nummer und Tutorial-Status

**3. Level-Start Blink-Effekt:**
- Bildschirm blinkt alle 250ms während Wartezeit
- Weißer Overlay (30% Opacity)
- Countdown-Text: "Bereit? 2..." → "Bereit? 1..."
- Visuelles Feedback für 2-Sekunden-Freeze

### 📝 Änderungen:
- Musik-Init: `play().then().catch()` mit Fallback
- `canvas.click`: Tutorial verwendet `loadLevel()`, Normal verwendet `loadLevelByNumber()`
- `gameLoop()`: Blink-Effekt wenn `!playerCanMove`

### 🎯 Verhalten:

**Musik-Start:**
```javascript
menuMusic.play()
  .then(() => console.log('Musik läuft'))
  .catch(() => {
    // Fallback: Bei erstem Click
    document.addEventListener('click', startMusic, { once: true });
  });
```

**Wiederholen:**
```
Tutorial Level 3:
  currentLevel = 3 (1-basiert)
  → loadLevel(2) (0-basiert) ✅

Normal Level 5:
  currentLevel = 5 (1-basiert)
  → loadLevelByNumber(5) ✅
```

**Blink-Effekt:**
```
Level startet → 2 Sekunden Wartezeit
├─ 0.00s: Blink (weiß)
├─ 0.25s: Normal
├─ 0.50s: Blink (weiß)
├─ 0.75s: Normal
├─ 1.00s: Blink (weiß)
├─ 1.25s: Normal
├─ 1.50s: Blink (weiß)
├─ 1.75s: Normal
└─ 2.00s: Spieler kann sich bewegen ✅
```

---

## v1.13.0 (25.10.2025) - Menü-Vereinfachung & Auto-Music

### ✨ UI/UX-Verbesserungen:

**1. "Level Laden" Button entfernt:**
- ❌ Removed: "📂 Level Laden" Button
- Grund: Vereinfachung des Hauptmenüs
- Nur noch 2 Buttons:
  - ▶ Spiel Starten
  - 📚 Tutorial Starten

**2. Menü-Musik startet automatisch:**
- **OHNE User-Interaktion** erforderlich
- Autoplay-Trick: `<audio autoplay muted>` + sofortiges unmute
- Funktioniert in den meisten modernen Browsern
- Musik startet beim ersten Laden der Seite

### 📝 Änderungen:
- `<audio id="menuMusic">`: `autoplay muted` hinzugefügt
- Initialisierung: `menuMusic.muted = false` (sofortiges unmute)
- `showMenu()`: Prüft ob Musik pausiert ist
- `hideMenu()`: Pausiert statt reset (Position bleibt)
- HTML: "Level Laden" Button entfernt

### 🎯 Verhalten:
```
SEITE LÄDT:
  ✅ Menü-Musik startet SOFORT (20%)
  ✅ OHNE Click/Key erforderlich
  ✅ Autoplay-Trick umgeht Browser-Blockierung

SPIEL STARTEN:
  ❌ Menü-Musik pausiert
  ✅ Ingame-Musik startet (15%)

ZURÜCK ZUM MENÜ:
  ❌ Ingame-Musik stoppt
  ✅ Menü-Musik fortsetzt
```

### 🎵 Autoplay-Technik:
```html
<!-- Startet muted (erlaubt Autoplay) -->
<audio id="menuMusic" loop autoplay muted>

<!-- JavaScript unmuted sofort -->
menuMusic.muted = false;  // 🎵 Musik läuft!
```

---

## v1.12.0 (25.10.2025) - Ingame Music & Audio Balance

### 🎵 Audio-Features:

**1. Ingame-Musik hinzugefügt:**
- Neue Datei: `/music/ingame.mp3` (2.6 MB)
- Spielt während Spiel/Tutorial
- Loop: Endlosschleife
- Lautstärke: **15%**

**2. Menü-Musik Lautstärke angepasst:**
- Alt: 30%
- Neu: **20%**
- Angenehmer für längeres Hören

**3. Automatischer Musik-Wechsel:**
- **Menü öffnen**: 
  - Menü-Musik startet (20%)
  - Ingame-Musik stoppt
- **Spiel starten**: 
  - Ingame-Musik startet (15%)
  - Menü-Musik stoppt

### 📁 Neue Dateien:
- `music/ingame.mp3` - Gameplay-Hintergrundmusik (2.6 MB)

### 📝 Änderungen:
- `showMenu()`: Startet Menü-Musik (20%), stoppt Ingame-Musik
- `hideMenu()`: Startet Ingame-Musik (15%), stoppt Menü-Musik
- Initialisierung: Beide Tracks mit korrekten Volumes

### 🎯 Audio-Verhalten:
```
MENÜ → SPIEL:
  ❌ menu_background.mp3 (stoppt)
  ✅ ingame.mp3 (startet @ 15%)

SPIEL → MENÜ:
  ❌ ingame.mp3 (stoppt)
  ✅ menu_background.mp3 (startet @ 20%)
```

### 📊 Package-Größe:
- **Alt**: 3.6 MB
- **Neu**: 6.1 MB (+2.5 MB durch ingame.mp3)

---

## v1.11.0 (25.10.2025) - Polish & Tutorial-Erweiterung

### ✨ UX-Verbesserungen:

**1. Menü-Musik beim ersten Laden:**
- Musik startet automatisch beim ersten Öffnen
- Fallback: Bei Autoplay-Blockierung startet nach erstem Click/Tastendruck
- Smooth User Experience

**2. Versionsnummer im Hauptmenü:**
- Version "v1.11.0" direkt unter dem Titel sichtbar
- Goldene Farbe (#FFD700)
- Immer aktuell und prominent platziert

**3. "Wiederholen" merkt sich Level-Typ:**
- Wiederholen lädt korrekt:
  - Tutorial: `inTutorialMode = true`
  - Custom Level: `usingCustomLevels = true`
  - Normal Level: Standard-Modus
- `currentLevel` bleibt erhalten

**4. 2 Sekunden Wartezeit bei Level-Start:**
- Spieler kann sich erst nach 2 Sekunden bewegen
- Zeit zum Orientieren und Level anschauen
- `playerCanMove = false` beim Start
- Nach 2000ms: `playerCanMove = true`

**5. Tutorial 05 ersetzt:**
- Neu: "Learn to Grab Without Moving"
- Monster: 1x TNT
- Diamanten: 4
- Required: 12 Diamanten

**6. Tutorial 06 hinzugefügt:**
- Neu: "Learn About Magic Walls"
- 44 Steine über Magic Wall
- Required: 40 Diamanten
- 6 Tutorials gesamt!

### 📁 Geänderte/Neue Dateien:
- `tutorials/tutorial_05.json` - Ersetzt
- `tutorials/tutorial_06.json` - Neu hinzugefügt

### 📝 Änderungen:
- `movePlayer()`: Prüft `playerCanMove` vor Bewegung
- `loadLevel()`: Setzt `levelStartTime` und `playerCanMove = false`
- Menü: Versionsnummer hinzugefügt
- Musik: Auto-Start mit Fallback

### 🎯 Verhalten:
- **Level-Start**: 2 Sekunden freeze
- **Wiederholen**: Lädt exakt gleiches Level
- **Musik**: Spielt sofort (oder nach Click)
- **Version**: Immer sichtbar

---

## v1.10.0 (25.10.2025) - Diamond Digger Rebranding & Menu Music

### ✨ UI/UX-Features:

**1. "Level wiederholen" Button bei Game Over:**
- Neuer Button "🔄 WIEDERHOLEN" links neben "HAUPTMENÜ"
- Level wird neu geladen OHNE Highscore-Eintrag
- `highscoreChecked = true` verhindert Bestenlisten-Eintrag
- Perfekt zum Üben ohne Statistik zu verfälschen

**2. Titel-Rebranding:**
- ❌ Alt: "⛏️ TUNNEL GRABER ⛏️"
- ✅ Neu: "💎 DIAMOND DIGGER 💎"
- Browser-Tab: "Diamond Digger - Extreme Edition"

**3. Menü-Hintergrundmusik:**
- Neue Datei: `/music/menu_background.mp3` (3.0 MB)
- Lautstärke: 30%
- Loop: Endlosschleife
- Auto-Start: Beim Menü öffnen
- Auto-Stop: Beim Spiel/Tutorial starten

### 📁 Neue Dateien:
- `music/menu_background.mp3` - Menü-Hintergrundmusik

### 📝 Änderungen:
- `drawGameOver()`: Zwei Buttons (Wiederholen + Hauptmenü)
- `canvas.click`: Handler für beide Buttons
- `showMenu()`: Startet Musik (30% Volume)
- `hideMenu()`: Stoppt Musik
- HTML: Audio-Element hinzugefügt
- Titel überall geändert

### 🎯 Verhalten:
- **Wiederholen**: Kein Highscore, nur Übung
- **Hauptmenü**: Wie bisher, mit Stats
- **Musik**: Spielt nur im Menü (nicht im Spiel)

---

## v1.9.0 (25.10.2025) - UX-Verbesserungen & ESC-Funktion

### ✨ Gameplay-Features:

**1. Kein Highscore im Tutorial-Modus:**
- Tutorial-Level generieren KEINEN Highscore-Eintrag
- Gilt sowohl für Completion als auch Game Over
- Nur echte Level (level_00.json, level_01.json, etc.) erzeugen Highscores

**2. Level-Zentrierung:**
- Kleine Level werden automatisch zentriert
- Wenn Level schmaler als Browser: horizontal zentriert
- Wenn Level kleiner als Browser: vertikal zentriert
- Beispiel: level_00.json (13x11) wird zentriert dargestellt

**3. ESC-Taste zum Aufgeben:**
- ESC drücken → Spieler stirbt sofort
- Game Over Grund: "🚪 Aufgegeben (ESC)"
- Funktioniert nur während aktivem Spiel (nicht im Menü)

### 📝 Änderungen:
- `drawGameOver()`: Prüft `!inTutorialMode` vor Highscore-Check
- `updateCamera()`: Zentriert Level wenn kleiner als Canvas
- `keydown` Event: ESC-Taste löst Game Over aus

### 🎯 Verhalten:
- Tutorial: Kein Highscore bei Abschluss oder Tod
- Kleine Level: Zentriert in großen Browsern
- ESC: Schnelles Aufgeben ohne Warten

---

## v1.8.2 (25.10.2025) - Level & Tutorial Updates

### 📁 Level-Dateien aktualisiert:

**Tutorial-Level:**
- ✅ `tutorial_01.json` - Collect Diamonds (aktualisiert)
- ✅ `tutorial_02.json` - Learn the Physics of Rocks (aktualisiert)
- ✅ `tutorial_03.json` - Use of Exploding Monsters (aktualisiert)
- ✅ `tutorial_04.json` - Watch Out for Traps (aktualisiert, requiredDiamonds: 24)
- ✅ `tutorial_05.json` - Learn About Magic Walls (aktualisiert)

**Game-Level:**
- ✅ `level_00.json` - Level_00 (aktualisiert, 13x11, requiredDiamonds: 5)

### 📝 Änderungen:
- Alle Tutorial-Level mit neuesten Versionen ersetzt
- Level_00 komplett überarbeitet (kleineres Level)
- Level_00 enthält Diamond-Monster

### 🎯 Neue Features in Level_00:
- **Größe:** 13x11 (kleiner, kompakter)
- **Start:** (2,2)
- **Exit:** (10,2)
- **Steine:** 5 Steine in Reihe
- **Monster:** 1 Diamond-Monster
- **Diamanten:** 0 am Start (werden durch Monster-Tod erstellt)
- **Benötigt:** 5 Diamanten

---

## v1.8.1 (25.10.2025) - Monster-Bewegung Fix & Explosions-Physik

### ✨ Gameplay-Features:

**1. Tutorial-Level aktualisiert:**
- `tutorial_04.json` aktualisiert (Watch Out for Traps)
- `tutorial_05.json` aktualisiert (Learn About Magic Walls)

**2. Keine diagonale Monster-Bewegung:**
- Diamond-Monster: nur N, O, S, W (im Uhrzeigersinn)
- TNT-Monster: nur O, S, W, N (gegen Uhrzeigersinn)
- Monster bewegen sich NUR vertikal/horizontal

**3. Fallende Steine + Explosion:**
- Fallende Steine im Explosionsradius werden zu Diamanten
- Explosion wandelt fallenden Stein → Diamant (fallend)
- Diamant fällt weiter nach Transformation

### 📝 Änderungen:
- `moveAlongWall()`: 4 Richtungen statt 8 (keine Diagonalen)
- `moveAlongWallCounterClockwise()`: 4 Richtungen statt 8
- `handleMonsterDeath()`: Prüft auf fallende Steine, wandelt zu Diamanten
- Tutorial 04 & 05 ersetzt

### 🎯 Verhalten:
- Monster: nur 4-Richtungen (↑→↓←)
- Explosion + fallender Stein = fallender Diamant
- TNT-Monster Explosion transformiert Steine korrekt

---

## v1.8.0 (25.10.2025) - Monster-Bewegung & Magische Wand Physik

### ✨ Gameplay-Features:

**1. TNT-Monster Bewegung (GEGEN Uhrzeigersinn):**
- TNT-Monster bewegen sich jetzt entlang Wänden
- Reihenfolge: rechts → unten → links → oben
- Diamant-Monster: weiterhin im Uhrzeigersinn (links → oben → rechts → unten)

**2. Wände sind zerstörbar:**
- Explosionen (TNT-Monster) zerstören jetzt auch `wall` Tiles
- `border` und `magic_wall` bleiben unzerstörbar

**3. Magische Wand - Stein→Diamant:**
- Wenn Stein auf `magic_wall` fällt UND unten leer ist:
  - Stein verschwindet
  - Diamant erscheint unterhalb der magischen Wand
  - Diamant fällt weiter

**4. Magische Wand - Diamant→Stein:**
- Wenn Diamant auf `magic_wall` fällt UND unten leer ist:
  - Diamant verschwindet
  - Stein erscheint unterhalb der magischen Wand
  - Stein fällt weiter

### 📝 Änderungen:
- `moveAlongWallCounterClockwise()` Funktion für TNT-Monster
- TNT-Monster verwenden neue Bewegungslogik
- Explosions-Code zerstört walls
- `updateFallingStones()`: Magic Wall Transformation
- `updateFallingDiamonds()`: Magic Wall Transformation

### 🎯 Verhalten:
- TNT-Monster folgen Wänden in umgekehrter Richtung
- Keine diagonale Bewegung für Monster
- Magic Wall transformiert nur wenn Platz unten frei ist
- Transformierte Objekte fallen sofort weiter

---

## v1.7.0 (25.10.2025) - Tutorial-System

### ✨ Neue Features:
- **Tutorial-System:** 5 Tutorial-Level zum Lernen
- **Tutorial-Button** im Hauptmenü (📚 Tutorial Starten)
- Tutorials werden von GitHub geladen
- Keine Highscore-Einträge im Tutorial-Modus

### 📁 Neue Struktur:
- `/tutorials/` Verzeichnis erstellt
- `tutorial_01.json` - Collect Diamonds
- `tutorial_02.json` - Learn the Physics of Rocks
- `tutorial_03.json` - Use of Exploding Monsters
- `tutorial_04.json` - Watch Out for Traps
- `tutorial_05.json` - Learn About Magic Walls

### 📝 Änderungen:
- `inTutorialMode` Variable für Tutorial-Status
- `tutorialLevels` Array für Tutorial-Level
- `startTutorial()` lädt Tutorial 01 von GitHub
- `loadTutorialFromGitHub()` lädt Tutorial-Level
- `nextLevel()` unterscheidet Tutorial/Normal-Modus
- `showCompletionScreen()` prüft Tutorial-Modus

### 🎯 Verhalten:
- Tutorial-Button → Startet Tutorial 01
- Nach Tutorial-Abschluss: Kein Highscore-Eintrag
- Tutorial-Level: URLs von `/tutorials/tutorial_XX.json`

---

## v1.6.7 (25.10.2025) - Editor-Fixes & Magische Wand

### ✨ Neue Features:
- **Magische Wand (🟪):** Neuer Tile-Typ im Editor
- Visuell: Lila/Magenta mit Glanz-Effekt
- Verhalten: Unzerstörbar wie border (derzeit)

### 🐛 Bug Fixes:
- **"Mit Erde füllen":** Überschreibt jetzt auch Spieler-Position
- **"Mit Erde füllen":** Korrigiert auf `levelHeight - 2` (statt -3)
- **"Mit Erde füllen":** Prüft nur border (statt wall)

### ✨ Validierung beim Speichern:
- ❌ Fehler wenn Spieler nicht platziert ist
- ❌ Fehler wenn Ausgang nicht platziert ist
- ❌ Fehler wenn Spieler nicht auf 'empty' Tile ist
- ❌ Fehler wenn Ausgang nicht auf 'empty' Tile ist
- ✅ Klare Fehlermeldungen mit Anweisungen

### 📝 Änderungen:
- **Level-Editor:** `fillEarth()` überschreibt alle Tiles außer border
- **Level-Editor:** `saveLevel()` validiert Level vor Speichern
- **Level-Editor:** Neue Tool: "Magie" (🟪) für magic_wall
- **Hauptspiel:** magic_wall wie border behandelt (unzerstörbar)
- **Hauptspiel:** magic_wall Rendering (lila mit Glanz)

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

**Stabil:** v1.14.0
**Debug:** v1.14.0-debug

**Download:**
- [tunnel_game.html](computer:///mnt/user-data/outputs/tunnel_game.html) - v1.14.0
- [tunnel_game_debug.html](computer:///mnt/user-data/outputs/tunnel_game_debug.html) - v1.14.0-debug
- [level_editor.html](computer:///mnt/user-data/outputs/level_editor.html) - v1.7.0
- [github-release.zip](computer:///mnt/user-data/outputs/github-release.zip) - v1.14.0 (6.1 MB)

---

**Letzte Aktualisierung:** 25.10.2025
