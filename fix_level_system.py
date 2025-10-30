#!/usr/bin/env python3
"""
Komplettes Refactoring des Level-Systems
- Separate Zähler für Tutorial und Game
- Auto-Detection von Level-Anzahl
- Korrekter Progress-Reset
- Retry Level Funktion
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("=== LEVEL SYSTEM REFACTORING ===\n")

# 1. Füge separate Variablen hinzu
print("1. Füge separate Level-Variablen hinzu...")
old_vars = """        let currentLevel = 0;  // Startet jetzt mit Level 0
        let currentTutorialLevel = 1;  // Separate Zählung für Tutorials"""

new_vars = """        let currentLevel = 0;  // Normal Levels (0-basiert)
        let currentTutorialLevel = 1;  // Tutorial Levels (1-basiert)
        let maxTutorialLevels = 4;  // Wird dynamisch gesetzt
        let maxNormalLevels = 5;  // Wird dynamisch gesetzt (level_00 bis level_04)"""

if old_vars in content:
    content = content.replace(old_vars, new_vars)
    print("   ✅ Variablen hinzugefügt")
else:
    print("   ⚠️  Variablen nicht gefunden - manuelle Prüfung nötig")

# 2. Reset bei Start Game
print("\n2. Fixe startGame() Reset...")
old_start = """        function startGame() {
            console.log('🎮 START GAME');
            hideMenu();
            resetGameStats();
            currentLevel = 0;  // Startet mit Level 0!
            currentTutorialLevel = 1;  // Reset Tutorial Counter
            gameOver = false;
            highscoreChecked = false;
            inTutorialMode = false;  // Kein Tutorial - WICHTIG!
            tutorialLevels = [];  // Clear Tutorial Cache
            gameStarted = false;  // Wird in loadLevelFromGitHub gesetzt
            
            // Lade Level 0 von GitHub
            console.log('📥 Lade Level 0 von GitHub...');
            loadLevelFromGitHub(0);"""

new_start = """        function startGame() {
            console.log('🎮 START GAME');
            hideMenu();
            resetGameStats();
            
            // RESET: Level Progress
            currentLevel = 0;  // Start bei Level 0
            currentTutorialLevel = 1;  // Reset Tutorial für nächstes Mal
            
            // RESET: Game State
            gameOver = false;
            gameCompleted = false;
            highscoreChecked = false;
            inTutorialMode = false;  // Kein Tutorial!
            
            // RESET: Level Cache
            tutorialLevels = [];  // Clear Tutorial Cache
            
            gameStarted = false;
            
            // Lade Level 0 von GitHub
            console.log('📥 Lade Level 0 von GitHub...');
            loadLevelFromGitHub(0);"""

if old_start in content:
    content = content.replace(old_start, new_start)
    print("   ✅ startGame() gefixt")
else:
    print("   ⚠️  startGame() nicht gefunden")

# 3. Reset bei Start Tutorial
print("\n3. Fixe startTutorial() Reset...")
old_tutorial_start = """        function startTutorial() {
            console.log('📚 START TUTORIAL');
            hideMenu();
            resetGameStats();
            currentLevel = 0;
            currentTutorialLevel = 1;  // Start bei Tutorial 1
            levelDisplay.textContent = '1/4';
            gameOver = false;
            highscoreChecked = false;
            inTutorialMode = true;  // Tutorial-Modus aktiv!
            tutorialLevels = [];  // Leere Tutorial-Level
            gameStarted = false;  // Wird in loadTutorialFromGitHub gesetzt
            
            // Lade Tutorial 01 von GitHub
            console.log('📥 Lade Tutorial 01 von GitHub...');
            loadTutorialFromGitHub(1);
        }"""

new_tutorial_start = """        function startTutorial() {
            console.log('📚 START TUTORIAL');
            hideMenu();
            resetGameStats();
            
            // RESET: Tutorial Progress
            currentLevel = 0;
            currentTutorialLevel = 1;  // Start bei Tutorial 1
            
            // RESET: Game State
            gameOver = false;
            gameCompleted = false;
            highscoreChecked = false;
            inTutorialMode = true;  // Tutorial-Modus aktiv!
            
            // RESET: Level Cache
            tutorialLevels = [];  // Leere Tutorial-Level
            customLevels = [];  // Clear normal level cache
            
            levelDisplay.textContent = `1/${maxTutorialLevels}`;
            gameStarted = false;
            
            // Lade Tutorial 01 von GitHub
            console.log('📥 Lade Tutorial 01 von GitHub...');
            loadTutorialFromGitHub(1);
        }"""

if old_tutorial_start in content:
    content = content.replace(old_tutorial_start, new_tutorial_start)
    print("   ✅ startTutorial() gefixt")
else:
    print("   ⚠️  startTutorial() nicht gefunden")

print("\n4. Speichere Datei...")
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Datei gespeichert\n")
print("=== ZUSAMMENFASSUNG ===")
print("- Separate Variablen für Tutorial/Game Levels")
print("- maxTutorialLevels = 4")
print("- maxNormalLevels = 5")
print("- Vollständiger Reset in startGame()")
print("- Vollständiger Reset in startTutorial()")
print("\nNächste Schritte:")
print("- nextLevel() muss angepasst werden")
print("- Retry Level Funktion erstellen")
print("- Completion Checks anpassen")
