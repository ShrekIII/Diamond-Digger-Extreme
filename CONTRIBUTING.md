# 🤝 MITWIRKEN - Contributing Guide

Vielen Dank für dein Interesse an Diamond Digger! Wir freuen uns über jeden Beitrag.

## 📋 ARTEN VON BEITRÄGEN

### 🆕 Neue Level
Die einfachste Art mitzuwirken!
- Verwende den [Level-Editor](https://ShrekIII.github.io/Diamond-Digger/level_editor.html)
- Erstelle ein kreatives, herausforderndes Level
- Reiche es via Pull Request ein

### 🐛 Bug Reports
Gefunden einen Fehler?
- Suche erst in [Issues](https://github.com/ShrekIII/Diamond-Digger/issues)
- Erstelle ein neues Issue mit:
  - Beschreibung des Problems
  - Schritte zum Reproduzieren
  - Browser & Version
  - Screenshots (falls relevant)

### ✨ Feature-Vorschläge
Hast du eine Idee?
- Erstelle ein Issue mit Tag `enhancement`
- Beschreibe die Funktion detailliert
- Erkläre den Nutzen

### 📝 Dokumentation
Verbessere die Docs!
- Rechtschreibfehler
- Unklare Erklärungen
- Fehlende Informationen
- Übersetzungen

---

## 🎨 LEVEL EINREICHEN

### Schritt-für-Schritt:

1. **Level erstellen:**
   ```
   Öffne: https://ShrekIII.github.io/Diamond-Digger/level_editor.html
   Gestalte dein Level
   Speichere als level_XX.json (XX = nächste freie Nummer)
   ```

2. **Repository forken:**
   ```
   Klicke auf "Fork" oben rechts
   ```

3. **Level hinzufügen:**
   ```
   Gehe zu deinem Fork
   Öffne /level/ Ordner
   Klicke "Add file" → "Upload files"
   Wähle dein level_XX.json
   Commit mit Message: "Add level XX: [Dein Level-Name]"
   ```

4. **Pull Request erstellen:**
   ```
   Gehe zu "Pull Requests"
   Klicke "New Pull Request"
   Titel: "New Level: [Dein Level-Name]"
   Beschreibung:
   - Level-Nummer
   - Schwierigkeitsgrad (Leicht/Mittel/Schwer)
   - Besonderheiten
   - Screenshot (optional)
   ```

### Level-Qualitätskriterien:
✅ Spielbar (Start → Diamanten → Exit erreichbar)  
✅ Fair (genug Zeit, kein Glück nötig)  
✅ Interessant (nicht zu simpel)  
✅ Getestet (selbst durchgespielt)  
✅ JSON-Format korrekt  

---

## 💻 CODE-BEITRÄGE

### Setup:

1. **Fork & Clone:**
   ```bash
   git clone https://github.com/DEIN-USERNAME/Diamond-Digger.git
   cd Diamond-Digger
   ```

2. **Branch erstellen:**
   ```bash
   git checkout -b feature/mein-feature
   # oder
   git checkout -b bugfix/mein-bugfix
   ```

3. **Lokalen Webserver starten:**
   ```bash
   python -m http.server 8000
   # Öffne http://localhost:8000
   ```

4. **Entwickeln & Testen:**
   - Ändere index.html oder andere Dateien
   - Teste im Browser
   - Prüfe Browser-Console auf Fehler

5. **Commit & Push:**
   ```bash
   git add .
   git commit -m "Beschreibung der Änderung"
   git push origin feature/mein-feature
   ```

6. **Pull Request:**
   - Gehe zu GitHub
   - Erstelle Pull Request von deinem Branch
   - Beschreibe Änderungen detailliert

### Code-Stil:
- **JavaScript:** 4 Spaces Einrückung
- **Kommentare:** Auf Deutsch oder Englisch
- **Funktionen:** Sprechende Namen
- **Variablen:** camelCase
- **Konstanten:** UPPER_CASE

### Testen:
- ✅ In Chrome/Firefox/Edge testen
- ✅ Browser-Console auf Fehler prüfen
- ✅ Alle Level durchspielen
- ✅ Highscore-System testen
- ✅ Level-Editor testen (falls geändert)

---

## 🐛 BUG-FIX WORKFLOW

1. **Issue erstellen** (falls nicht vorhanden)
2. **Branch:** `bugfix/issue-nummer-kurzbeschreibung`
3. **Fix implementieren**
4. **Testen:**
   - Bug reproduzieren (vorher)
   - Fix anwenden
   - Prüfen dass Bug weg ist
   - Prüfen dass nichts anderes kaputt ist
5. **Pull Request** mit Referenz zum Issue

---

## 📝 DOKUMENTATION VERBESSERN

### Was verbessern:
- README.md - Hauptdokumentation
- docs/*.md - Detaillierte Guides
- Code-Kommentare in index.html
- Level-Format-Dokumentation

### Wie:
1. Fork Repository
2. Datei bearbeiten
3. Pull Request mit klarer Beschreibung

---

## ❓ FRAGEN?

- 💬 Erstelle ein [Issue](https://github.com/ShrekIII/Diamond-Digger/issues)
- 📧 Kontaktiere @ShrekIII

---

## ✅ CHECKLISTE VOR PULL REQUEST

- [ ] Code funktioniert lokal
- [ ] Keine Console-Fehler
- [ ] In mehreren Browsern getestet
- [ ] Dokumentation aktualisiert (falls nötig)
- [ ] Commit-Messages sind klar
- [ ] Branch ist aktuell mit main

---

## 🎉 NACH DEM MERGE

Dein Beitrag wird Teil des Spiels!
- Erscheint auf GitHub Pages
- Name in README Credits (bei größeren Beiträgen)
- Unser Dank! ❤️

---

## 📜 CODE OF CONDUCT

### Wir erwarten:
✅ Respektvoller Umgang  
✅ Konstruktive Kritik  
✅ Hilfsbereitschaft  
✅ Geduld mit Anfängern  

### Nicht toleriert:
❌ Beleidigungen  
❌ Diskriminierung  
❌ Spam  
❌ Destruktives Verhalten  

---

**Danke für deine Unterstützung!** 🙏

Jeder Beitrag, ob klein oder groß, macht Diamond Digger besser! ⛏️💎
