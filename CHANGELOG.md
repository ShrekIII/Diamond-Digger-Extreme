# 📜 CHANGELOG

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/).

---

## [1.0.0] - 2025-01-XX

### 🎉 Erste vollständige Version!

#### ✨ Hinzugefügt
- **Vollständiges Menü-System**
  - Hauptmenü mit Menu.png Hintergrund
  - "Spiel Starten" Button
  - "Level Editor" Button
  - Highscore-Liste (Top 10)

- **Highscore-System**
  - Automatischer Highscore-Check bei Game Over
  - Automatischer Highscore-Check bei Level-Completion
  - Name-Eingabe Dialog
  - LocalStorage Persistenz
  - Beispiel-Highscores beim ersten Start
  - Sortierung: Diamanten → Level → Zeit → Distanz
  - Automatische Migration alter Daten

- **Automatisches Level-System**
  - Level laden automatisch von GitHub
  - Fallback auf lokale Dateien
  - Manueller Upload-Dialog als letzte Option
  - Level-Caching für wiederholtes Spielen
  - 3 voll funktionsfähige Level

- **Level-Editor Integration**
  - Button im Hauptmenü
  - Öffnet in neuem Tab
  - Vollständiger visueller Editor

- **Game Over Screen**
  - Zwei Buttons: "Neustart" und "Menü"
  - Highscore-Check
  - Statistik-Anzeige

- **Completion Screen**
  - Erscheint nach allen Levels
  - Final-Statistiken
  - Zwei Buttons: "Neu Starten" und "Zurück zum Menü"

#### 🎮 Spielmechanik
- Spieler kann sich durch Erde graben
- Steine fallen realistisch
- Diamanten fallen wie Steine
- 2 Monster-Typen:
  - Diamant-Monster (erzeugt Diamant bei Tod)
  - TNT-Monster (explodiert bei Tod)
- Abbaubare Mauern (3 Treffer mit Schaufel)
- Timer-System: 60s + 10s pro Level
- Ausgang öffnet sich bei genug Diamanten
- Kamera folgt Spieler

#### 📁 Projekt-Struktur
- `index.html` - Hauptspiel
- `level_editor.html` - Level-Editor
- `level/` - Level-Dateien (level_01.json bis level_03.json)
- `img/` - Bilder (Menu.png)
- `docs/` - Dokumentation

#### 📖 Dokumentation
- README.md - Haupt-Dokumentation
- CONTRIBUTING.md - Mitwirkungs-Guide
- LICENSE - MIT Lizenz
- docs/README_GITHUB.md - GitHub-spezifische Anleitung
- docs/SCHNELLSTART.md - Schnellstart-Guide
- docs/INSTALLATION.md - Installations-Checkliste

#### 🌐 GitHub Pages
- Spiel direkt spielbar unter GitHub Pages URL
- Automatisches Laden aller Assets von GitHub

---

## [Unreleased] - Geplante Features

### 🔮 In Planung für v1.1.0

#### Features
- [ ] Pause-Menü (ESC-Taste)
- [ ] Sound-Effekte
- [ ] Partikel-Effekte beim Graben
- [ ] Gamepad-Support
- [ ] Touch-Steuerung für Mobile
- [ ] Mehrsprachigkeit (EN/DE)
- [ ] Mehr Level (4-10)

#### Verbesserungen
- [ ] Bessere Grafiken
- [ ] Animationen
- [ ] Level-Vorschau vor dem Start
- [ ] Schwierigkeitsgrade
- [ ] Achievements-System
- [ ] Globale Online-Highscores

#### Bugfixes
- [ ] Performance-Optimierung bei vielen Objekten
- [ ] Browser-Kompatibilität verbessern

---

## Versionsformat

- **MAJOR** - Grundlegende Änderungen, Breaking Changes
- **MINOR** - Neue Features, abwärtskompatibel
- **PATCH** - Bugfixes, kleine Verbesserungen

Aktuelles Format: `[MAJOR].[MINOR].[PATCH]`

---

## Kategorien

- **✨ Hinzugefügt** - Neue Features
- **🔄 Geändert** - Änderungen an bestehenden Features
- **❌ Entfernt** - Entfernte Features
- **🐛 Bugfixes** - Behobene Fehler
- **🔒 Sicherheit** - Sicherheits-Patches
- **📝 Dokumentation** - Docs-Änderungen

---

[1.0.0]: https://github.com/ShrekIII/Diamond-Digger/releases/tag/v1.0.0
