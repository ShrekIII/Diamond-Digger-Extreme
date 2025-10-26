# 🔒 Security Policy

## Unterstützte Versionen

Folgende Versionen werden aktuell mit Security-Updates unterstützt:

| Version | Unterstützt          |
| ------- | -------------------- |
| 1.14.x  | ✅ Ja                |
| 1.13.x  | ⚠️ Teilweise        |
| < 1.13  | ❌ Nein             |

## 🐛 Sicherheitslücke melden

Wenn du eine Sicherheitslücke in Diamond Digger findest, bitte **NICHT** ein öffentliches Issue erstellen.

### Meldeprozess

1. **Privat melden:**
   - Sende eine E-Mail an: [security@project-email.com]
   - Oder erstelle ein privates Security Advisory auf GitHub
   
2. **Informationen bereitstellen:**
   - Beschreibung der Sicherheitslücke
   - Schritte zur Reproduktion
   - Betroffene Versionen
   - Mögliche Auswirkungen
   - (Optional) Lösungsvorschläge

3. **Antwort erwarten:**
   - Wir bestätigen den Empfang innerhalb von 48 Stunden
   - Wir analysieren das Problem innerhalb von 7 Tagen
   - Wir halten dich über den Fortschritt auf dem Laufenden

### Was qualifiziert als Sicherheitsproblem?

#### ✅ Sicherheitsrelevant
- XSS (Cross-Site Scripting) Schwachstellen
- Code Injection Möglichkeiten
- Unbefugter Zugriff auf LocalStorage
- Manipulation von Spielständen oder Highscores (wenn kritisch)
- Denial of Service Angriffe
- Zugriff auf sensible Daten

#### ❌ Nicht sicherheitsrelevant
- Normale Gameplay-Bugs
- UI/UX Probleme
- Performance-Issues
- Feature-Anfragen
- Highscore-Manipulation (für Single-Player OK)

## 🛡️ Sicherheitsmaßnahmen

### Aktuelle Sicherheitsfeatures

1. **Content Security Policy (CSP)**
   - Keine Inline-Scripts (geplant)
   - Sichere externe Ressourcen

2. **Input Validation**
   - Namen in Highscore werden validiert
   - Level-JSON wird geprüft

3. **LocalStorage**
   - Nur spielrelevante Daten
   - Keine sensiblen Informationen

4. **External Resources**
   - GitHub CDN für Level-Dateien
   - Vertrauenswürdige Audio-Dateien

### Geplante Verbesserungen

- [ ] Implementierung von CSP Headers
- [ ] Code-Minifizierung und Obfuskation
- [ ] Subresource Integrity (SRI) für externe Ressourcen
- [ ] HTTPS-Only Enforcement

## 📊 Schweregrad-Einstufung

Wir verwenden das CVSS (Common Vulnerability Scoring System):

- **Kritisch (9.0-10.0):** Sofortiger Hotfix
- **Hoch (7.0-8.9):** Fix innerhalb von 7 Tagen
- **Mittel (4.0-6.9):** Fix im nächsten Release
- **Niedrig (0.1-3.9):** Fix wenn möglich

## 🏆 Hall of Fame

Wir danken folgenden Personen für verantwortungsvolle Offenlegung:

<!-- Wird aktualisiert wenn Sicherheitslücken gemeldet werden -->
*Noch keine Einträge*

## 📝 Security-Checkliste für Contributors

Wenn du Code beiträgst, stelle bitte sicher:

- [ ] Keine sensiblen Daten im Code
- [ ] Input wird validiert und sanitized
- [ ] Keine eval() oder Function() Konstruktoren
- [ ] LocalStorage wird sicher verwendet
- [ ] Externe URLs sind vertrauenswürdig
- [ ] Keine console.log() mit sensiblen Daten

## 🔗 Ressourcen

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Web Security Best Practices](https://developers.google.com/web/fundamentals/security)
- [GitHub Security Guidelines](https://docs.github.com/en/code-security)

## 📧 Kontakt

Für Security-bezogene Fragen:
- GitHub Security Advisory (bevorzugt)
- E-Mail: [security@project-email.com]
- Keine öffentlichen Issues für Sicherheitsprobleme!

---

**Vielen Dank für die Hilfe, Diamond Digger sicherer zu machen!** 🛡️

*Letzte Aktualisierung: 26. Oktober 2025*
