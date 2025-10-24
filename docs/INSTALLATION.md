# 🚀 INSTALLATIONS- UND TEST-ANLEITUNG

## 📦 INSTALLATION

### Benötigte Dateien:
Alle Dateien befinden sich im Output-Ordner:

```
📁 Spielordner/
  ├── tunnel_game.html      (Das Hauptspiel - 2767 Zeilen)
  ├── Menu.png              (Menü-Hintergrundbild)
  ├── level_01.json         (Level 1)
  ├── level_02.json         (Level 2)
  └── level_03.json         (Level 3)
```

### Schritte:
1. ✅ Erstelle einen neuen Ordner (z.B. "TunnelGraber")
2. ✅ Kopiere alle 5 Dateien in diesen Ordner
3. ✅ Öffne `tunnel_game.html` in einem modernen Browser
   - Chrome/Edge (empfohlen)
   - Firefox
   - Safari

**WICHTIG:** Alle Dateien müssen im gleichen Ordner sein!

---

## 🧪 TEST-CHECKLISTE

### ✅ 1. Menü-Test
- [ ] Menü wird angezeigt mit Menu.png als Hintergrund
- [ ] Titel "⛏️ TUNNEL GRABER ⛏️" ist sichtbar
- [ ] Zwei Buttons sind vorhanden: "▶ Spiel Starten" und "📂 Level Laden"
- [ ] Rechts ist die Highscore-Liste sichtbar (anfangs leer)

### ✅ 2. Spiel-Start Test
- [ ] Klick auf "▶ Spiel Starten"
- [ ] Menü verschwindet
- [ ] Level 1 wird geladen (mit level_01.json)
- [ ] Spieler ist sichtbar (Position aus JSON)
- [ ] Diamanten sind sichtbar
- [ ] Timer läuft (60 Sekunden für Level 1)
- [ ] Status-Leiste zeigt: Level 1, Timer, 0/X Diamanten

### ✅ 3. Gameplay Test
- [ ] Spieler bewegt sich mit Pfeiltasten
- [ ] Spieler gräbt automatisch durch Erde
- [ ] Diamanten können gesammelt werden
- [ ] Steine fallen herunter
- [ ] Counter aktualisiert sich (Diamanten, Distanz)
- [ ] Timer zählt herunter

### ✅ 4. Level-Wechsel Test
- [ ] Sammle genügend Diamanten (siehe Status-Leiste)
- [ ] Ausgang öffnet sich (blinkt grün)
- [ ] Gehe zum Ausgang
- [ ] Level 2 wird automatisch geladen
- [ ] Timer setzt sich zurück (70 Sekunden für Level 2)
- [ ] Level-Counter zeigt "Level: 2"

### ✅ 5. Game Over Test
- [ ] Lasse einen Stein auf den Spieler fallen
- [ ] "GAME OVER" erscheint mit Grund
- [ ] Statistiken werden angezeigt (Diamanten, Level, Distanz)
- [ ] Zwei Buttons: "🔄 NEUSTART" und "🏠 MENÜ"
- [ ] Nach 2 Sekunden: Name-Eingabe erscheint (wenn Highscore)

### ✅ 6. Highscore Test
- [ ] Gib einen Namen ein (z.B. "TestUser")
- [ ] Klicke "💾 Speichern" oder drücke Enter
- [ ] Name-Eingabe schließt sich
- [ ] Klicke "🏠 MENÜ"
- [ ] Zurück im Hauptmenü
- [ ] Highscore-Liste zeigt den neuen Eintrag an!

### ✅ 7. Highscore-Persistenz Test
- [ ] Schließe den Browser komplett
- [ ] Öffne `tunnel_game.html` erneut
- [ ] Highscore-Liste zeigt immer noch die Einträge! ✨

### ✅ 8. Completion Test (Optional - alle 3 Level spielen)
- [ ] Spiele alle 3 Level durch
- [ ] "🎉 GRATULATION!" Screen erscheint
- [ ] Final-Statistiken werden angezeigt
- [ ] Highscore-Check wird durchgeführt
- [ ] Name-Eingabe erscheint (wenn Highscore)
- [ ] Zwei Buttons: "🔄 Neu Starten" und "🏠 Zurück zum Menü"

### ✅ 9. Level-Laden Test
- [ ] Klicke im Menü auf "📂 Level Laden"
- [ ] Wähle alle 3 Level-Dateien aus (level_01.json, level_02.json, level_03.json)
- [ ] Bestätigung: "3 Level geladen!"
- [ ] Spiel startet automatisch mit Level 1

---

## 🐛 FEHLERSUCHE

### Problem: Menü-Hintergrund wird nicht angezeigt
**Lösung:** Stelle sicher, dass `Menu.png` im gleichen Ordner wie `tunnel_game.html` liegt.

### Problem: Level können nicht geladen werden
**Lösung:** Stelle sicher, dass die JSON-Dateien im gleichen Ordner liegen und die Namenskonvention `level_01.json`, `level_02.json`, etc. einhalten.

### Problem: Highscores werden nicht gespeichert
**Lösung:** 
- Prüfe ob LocalStorage im Browser aktiviert ist
- Bei File-Protocol (file:///) kann es Einschränkungen geben
- Empfohlen: Verwende einen lokalen Webserver oder öffne direkt

### Problem: Spiel läuft zu langsam
**Lösung:** 
- Verwende Chrome oder Edge (beste Performance)
- Schließe andere Browser-Tabs
- Prüfe Hardware-Beschleunigung im Browser

---

## 📊 ERWARTETE ERGEBNISSE

### Hauptmenü:
- Hintergrundbild mit Maus, Helm und Diamanten
- Goldener Titel
- Zwei große goldene Buttons
- Schwarze Box rechts mit Highscore-Liste

### Spiel:
- Erde (braun), Mauern (grau), Tunnel (dunkel)
- Diamanten (blau/cyan, glitzernd)
- Steine (grau, rund)
- Spieler (als Punkt oder Kreis sichtbar)
- Status-Leiste unten (schwarz mit weißem Text)

### Game Over:
- Halbtransparenter schwarzer Overlay
- Roter "GAME OVER" Text
- Orange Grund-Text (warum gestorben)
- Weiße Statistiken
- Zwei Buttons (grün und orange)

### Highscore:
- Top 10 Einträge
- Sortiert nach Diamanten → Level → Zeit → Distanz
- Platz 1 hat goldene Umrandung
- Zeigt: Rang, Name, Diamanten, Level, Zeit, Distanz

---

## ✅ ERFOLG!

Wenn alle Tests bestanden sind, ist das Spiel vollständig funktionsfähig! 🎉

### Nächste Schritte:
1. 🎮 Erstelle eigene Level mit dem Level-Editor
2. 🏆 Versuche in die Top 10 zu kommen
3. 👥 Teile das Spiel mit Freunden
4. ⭐ Füge eigene Features hinzu (siehe PROJEKT_STATUS.md)

---

## 📞 SUPPORT

Bei Problemen:
1. Prüfe die Browser-Konsole (F12) für Fehler
2. Stelle sicher alle Dateien im richtigen Ordner sind
3. Verwende einen modernen Browser
4. Prüfe dass JavaScript aktiviert ist

**Viel Spaß beim Spielen!** ⛏️💎
